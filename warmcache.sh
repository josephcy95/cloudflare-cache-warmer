#!/usr/bin/bash

/usr/bin/python3 cache-warmer.py --url https://www.seenlyst.com/sitemap_index.xml -p "http://username:password@my-kua.pvdata.host:8080" -q
/usr/bin/python3 cache-warmer.py --url https://www.seenlyst.com/sitemap_index.xml -p "http://username:password@jp-tok.pvdata.host:8080" -q
/usr/bin/python3 cache-warmer.py --url https://www.seenlyst.com/sitemap_index.xml -p "http://username:password@sg-sin.pvdata.host:8080" -q
