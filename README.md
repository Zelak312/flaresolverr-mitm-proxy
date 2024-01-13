# Flaresolverr Mitm Proxy

## Overview

**Why use another proxy when Flaresolverr is technically already one?**

While Flaresolverr provides a proxy solution, it currently lacks support for headers and JSON payloads. To bridge this gap, Flaresolverr Mitm Proxy has been introduced. This utility allows users to include headers and send JSON, enhancing the overall capability of Flaresolverr.

## How it works

A request will be sent to flaresolverr, as usual, but the proxy url config will be set to point towards flaresolverr-mitm-proxy. What will happen is that the request will be proxied from flaresolverr to flaresolverr-mitm-proxy which will then send it to the website and the returned page will be sent back to flaresolverr for the cloudflare shenanigans

**If you want to support my work**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/zelak)

## Installation & Usage

There are multiple ways to set up and run the Flaresolverr Mitm Proxy:

1. **Docker Compose**:

    - Refer to the provided `docker-compose.yml` as a sample setup.
    - Note: When using the docker-compose.yml, avoid mapping ports directly. Instead, use the container image name and port 8080 for proxy settings in Flaresolverr. Ensure they are on the same Docker network. Mapping ports can still be used, I just prefer not to.

2. **Docker**:

    - Pull the Docker image and run. The Mitm proxy operates on port 8080, so remember to map this port.

3. **Manual Setup**:
    - Clone this repository.
    - Install dependencies.
    - Execute using `mitmdump -s mitm.py`.

#### Without proxy

flaresolverr -> flaresolverr-mitm-proxy -> website

#### With Proxy

see [how to use a proxy example](#using-an-upstream-proxy)

flaresolverr-> flaresolverr-mitm-proxy -> http proxy (optional) -> website

## Working with Headers

Headers set via special query parameters.

**Example**:

`$$headers[]=Authorization:mytoken`

To set the Authorization header value to `mytoken`. To add multiple headers, chain them:

`https://google.com?$$headers[]=Authorization:mytoken&$$headers[]=otherone:othervalue`

This also applies for POST requests (They are also in the query parameters)

## How to send cookies

Sending cookies is a bit different then headers. Flaresolverr already can pass cookies so flaresolverr-mitm doesn't integrates this, please see [the flaresolverr docs for cookies](https://github.com/FlareSolverr/FlareSolverr?tab=readme-ov-file#-requestget)

## Sending JSON in POST Request

To send a JSON payload in a POST request, utilize the `$$post` keyword within the postData parameter.

It takes a base64 encoded JSON string (base64 is needed because of how FlareSolverr works)

**Example**:

For sending this JSON

```json
{
    "test": "nice",
    "array": ["lol"],
    "nested": {
        "yeet": "oof"
    },
    "number": 4
}
```

You will first need to base64 it.

The base64 representation of this JSON payload is

```
eyJ0ZXN0IjoibmljZSIsImFycmF5IjpbImxvbCJdLCJuZXN0ZWQiOnsieWVldCI6ICJvb2YifSwibnVtYmVyIjo0fQ==
```

You then need to pass it in the `$$post` parameter from the postData of FlareSolverr

```
$$post=eyJ0ZXN0IjoibmljZSIsImFycmF5IjpbImxvbCJdLCJuZXN0ZWQiOnsieWVldCI6ICJvb2YifSwibnVtYmVyIjo0fQ==
```

## Environment variables

If you need to change `$$headers[]` and `$$post` for whatever reasons you are able to do so with <br>
SPECIAL_PREFIX_TOKEN, the default is `$$` and if changed it will change the prefix<br>

It is also possible to change the split token for headers<br>
HEADER_SPLIT_TOKEN, the default is `:` for `Authorization:mytoken` and can be changed

These can be changed in Docker and Docker compose

## Practical Example

For those using the Docker Compose setup:

1. Start both Flaresolverr and the Mitm proxy:

```bash
docker compose up -d
```

2. Make a request to Flaresolverr:

```bash
curl -L -X POST 'http://localhost:8191/v1' \
-H 'Content-Type: application/json' \
--data-raw '{
    "cmd": "request.post",
    "url": "https://httpbin.org/post?$$headers[]=Authorization:mytoken",
    "maxTimeout": 60000,
    "proxy": {
        "url": "flaresolverr-mitm-proxy:8080"
    },
    "postData": "$$post=eyJ0ZXN0IjoibmljZSIsImFycmF5IjpbImxvbCJdLCJuZXN0ZWQiOnsieWVldCI6ICJvb2YifSwibnVtYmVyIjo0fQ=="
}'
```

Note: It is important here that the proxy.url property is valid and points to the flaresolverr-mitm proxy with the correct port, the one shown in this example matches with the example docker-compose file if the services names haven't been altered and the two services are still in the same docker network. Make sure that it is right, it's crucial for this to work because flaresolverr will proxy the request to the flaresolverr-mitm which will do the changes needed

This request will use httpbin.org which will return the everything from the post so you can see if it worked correctly.
The response would look something like:

```json
{
    "status": "ok",
    "message": "Challenge not detected!",
    "startTimestamp": 1691721660615,
    "endTimestamp": 1691721665638,
    "version": "3.3.2",
    "solution": {
        "url": "https://httpbin.org/post",
        "status": 200,
        "cookies": [],
        "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "headers": {},
        "response": `
            <html>
            <head>
                <meta name="color-scheme" content="light dark">
            </head>
            <body>
                <pre style="word-wrap: break-word; white-space: pre-wrap;">
                    {
                        "args": {},
                        "data": "{\\"test\\": \\"nice\\", \\"array\\": [\\"lol\\"], \\"nested\\": {\\"yeet\\": \\"oof\\"}}",
                        "files": {},
                        "form": {},
                        "headers": {
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Cache-Control": "max-age=0",
                            "Content-Length": "61",
                            "Content-Type": "application/json",
                            "Host": "httpbin.org",
                            "Origin": "null",
                            "Sec-Ch-Ua": "\\"Chromium\\";v=\\"115\\", \\"Not/A)Brand\\";v=\\"99\\"",
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": "\\"Linux\\"",
                            "Sec-Fetch-Dest": "document",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Site": "cross-site",
                            "Authorization": "mytoken",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "X-Amzn-Trace-Id": "Root=1-64d59fbf-3a7a7e743a2c47bb5ab00d3b"
                        },
                        "json": {
                            "test": "nice",
                            "array": ["lol"],
                            "nested": {
                                "yeet": "oof"
                            },
                            "number": 4
                        },
                        "url": "https://httpbin.org/post"
                    }
                </pre>
            </body>
            </html>
        `
    }
}
```

## Using an upstream proxy

Note: socks proxy are not currently supported, if it is desired with docker, please open an issue and I will gladly add it, if you are not using docker, you can setup proxychains (linux) to make this works, I have no alternatives for windows for now<br>
see https://github.com/mitmproxy/mitmproxy/issues/211

it is possible to make mitm use an upstream proxy. To make it do so, will depend how you start flaresolverr-mitm

### Docker

To use a http/https proxy using docker, you need to provide the `PROXY` env variable in this format `http://my-upstream-proxy:port`<br>
if using docker-compose, it will need to be passed in the [environments properties](https://docs.docker.com/compose/environment-variables/set-environment-variables/)<br>
for docker cli, it will need to be passed as the `-e` [parameter](https://docs.docker.com/engine/reference/commandline/run/#env)<br>
If your proxy needs auth, you need to use the `PROXY_AUTH` env variable to pass in `username:password` ex: `PROXY_AUTH=username:password`

### manual python

When running flaresolverr-mitm proxy, instead of `mitmdump -s mitm.py` the --mode parameter can be added like so `mitmdump -s mitm.py --mode upstream:http://my-upstream-proxy:port`<br>
If your proxy needs auth, the `--upstream-auth` parameter, ex: `--upstream-auth username:password`
