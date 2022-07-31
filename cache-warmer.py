#!/usr/bin/env python
"""
Warm the caches of your website by crawling each page defined in sitemap.xml.
To use, download this file and make it executable. Then run:
./cache-warmer.py --url https://example.com/sitemap.xml -p "http://username:password@myproxy.host.com:8080"
"""
import sys
import argparse
import re
import requests
import asyncio
import aiohttp
import time

def parse_options():
    parser = argparse.ArgumentParser(description="""Cache crawler""")
    parser.add_argument('-u', '--url', help='The sitemap xml url', required=True, type=str)
    parser.add_argument('-p', '--proxy', help='HTTP proxy string', required=True, type=str)
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()
    return args

def get_sitemap_urls(url):
    a = requests.get(url, headers={"user-agent": "cache_warmer"})
    return re.findall('<loc>(.*?)</loc>?', a.text)

def get_url_list(url):
    a = requests.get(url, headers={"user-agent": "cache_warmer"})
    return re.findall('<loc>(.*?)</loc>?', a.text)


async def get(url, session, proxy, no_output):
    try:
        async with session.get(url=url,proxy=proxy,timeout=5) as response:
            resp = await response.read()
            if not no_output:
                print(f"{url} -> {response.status} {response.headers['CF-Cache-Status']}")
    except Exception as e:
        print(f"{url} -> {str(e)}")



async def warmup(urls, proxy, no_output):
    async with aiohttp.ClientSession(headers={"user-agent": "cache_warmer"}) as session:
        ret = await asyncio.gather(*[get(url, session, proxy, no_output) for url in urls])
    if not no_output:
        print(f"Warmed up {len(ret)} URLS")

def main():
    args = parse_options()
    sitemap_urls = get_sitemap_urls(args.url)
    http_proxy = args.proxy
    no_output = args.quiet

    for sitemap_url in sitemap_urls:
        url_list = get_url_list(sitemap_url)
        
        if not no_output:
            print(f"{sitemap_url}\nCrawling {len(url_list)} urls...")

        start = time.time()
        asyncio.run(warmup(url_list, http_proxy, no_output))
        end = time.time()

    sys.exit()


if __name__ == "__main__":
    main()
