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