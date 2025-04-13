#!/bin/bash

if [ -v PROXY_URL ]; then
    gost -L=:8080 -F="${PROXY_URL:-}" &>/dev/null &
    export PROXY=yes
fi

python3 main.py
