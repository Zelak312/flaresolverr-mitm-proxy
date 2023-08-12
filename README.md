## This is still in BETA, all pull requests are appreciated

# Flaresolverr Mitm Proxy

## Overview

**Why use another proxy when Flaresolverr is technically already one?**

While Flaresolverr provides a proxy solution, it currently lacks support for headers and JSON payloads. To bridge this gap, Flaresolverr Mitm Proxy has been introduced. This utility allows users to include headers and send JSON, enhancing the overall capability of Flaresolverr.

## Installation & Usage

There are multiple ways to set up and run the Flaresolverr Mitm Proxy:

1. **Docker Compose**:

    - Refer to the provided `docker-compose.yml` as a sample setup.
    - Note: When using the docker-compose.yml, avoid mapping ports directly. Instead, use the container image name and port 8080 for proxy settings in Flaresolverr. Ensure they are on the same Docker network.

2. **Docker**:

    - Pull the Docker image and run. The Mitm proxy operates on port 8080, so remember to map this port.

3. **Manual Setup**:
    - Clone this repository.
    - Install dependencies.
    - Execute using `mitmdump -s mitm.py`.

### Working with Headers

Headers set via special query parameters.

**Example**:

`$headers$[]=Authorization:mytoken`

To set the Authorization header value to `mytoken`. To add multiple headers, chain them:

`https://google.com?$headers$[]=Authorization:mytoken&$headers$[]=otherone:othervalue`

This also applies for POST requests (They are also in the query parameters)

### Sending JSON in POST Request

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
curl -L -X POST 'http://localhost:8191/v1'
    -H 'Content-Type: application/json'
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

The response would look something like:

```json
{
    "status": "ok",
    "message": "Challenge not detected!",
    "startTimestamp": 1691721660615,
    "endTimestamp": 1691721665638,
    "version": "3.3.2",
    "solution": {
        "url": "https://httpbin.org/post?$$headers[]=Authorization:mytoken",
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
                        "url": "https://httpbin.org/post?$$headers[]=Authorization:mytoken"
                    }
                </pre>
            </body>
            </html>
        `
    }
}
```
