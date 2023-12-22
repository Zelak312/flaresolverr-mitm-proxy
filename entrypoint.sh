#!/bin/bash

# Check if the PROXY environment variable is set
if [ -z "${PROXY}" ]; then
    # PROXY not set, run mitmdump without upstream proxy
    mitmdump -s ./mitm.py
else
    # PROXY is set, run mitmdump with the specified upstream proxy
    echo "Running with proxy: ${PROXY}"
    mitmdump -s ./mitm.py --mode upstream:${PROXY}
fi