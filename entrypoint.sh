#!/bin/bash

# Check if the PROXY environment variable is set
if [ -z "${PROXY}" ]; then
    # PROXY not set, run mitmdump without upstream proxy
    mitmdump -s ./mitm.py
else
    if [ -z "${PROXY_AUTH}" ]; then
        # PROXY is set, run mitmdump with the specified upstream proxy
        echo "Running with proxy: ${PROXY}"
        mitmdump -s ./mitm.py --mode upstream:${PROXY}
    else
        echo "Running with proxy: ${PROXY} and PROXY_AUTH"
        mitmdump -s ./mitm.py --mode upstream:${PROXY} --upstream-auth ${PROXY_AUTH}
    fi
fi