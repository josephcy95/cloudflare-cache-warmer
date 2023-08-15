# Cloudflare Cache Warmer
Use proxy to send http request to URLs defined by sitemap.xml, helps warming up the main document cache in Cloudflare server.

### Usage:
```
./cache-warmer.py --url https://example.com/sitemap.xml -p "http://username:password@myproxy.host.com:8080"
```

### Params:
```
-u, --url <link to sitemap>
-p, --proxy <HTTP proxy string>
-q, --quiet (No output)
```

### How to use:
Add as many line of proxies or urls into warmcache.sh, then setup cron job to run the script.


---
Credits: @hn-support
