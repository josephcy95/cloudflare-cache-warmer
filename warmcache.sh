#!/bin/bash

cd /home/ubuntu/cache-warmer

declare -a urls=(
    "https://www.seenlyst.com/sitemap_index.xml"
)

declare -a proxies=(
    ""
    "http://user:pass@host:port"
)

for url in "${urls[@]}"; do
    for proxy in "${proxies[@]}"; do
        if [ -z "$proxy" ]; then
            command="/usr/bin/python3 cache-warmer.py --url $url -q"
        else
            command="/usr/bin/python3 cache-warmer.py --url $url -p \"$proxy\" -q"
        fi
        eval $command
    done
done
