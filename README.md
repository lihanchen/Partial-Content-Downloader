# Partial Content (HTTP 206) Downloader

Introduction
-----
I had a file to download from a HTTP server. When I use Browser/curl/wget, the server only send a small portion of the file and give an HTTP 206 Partial Content code.
I didn't find any existing tools to download file on these kind of servers so I created this script.

Usage
-----
```bash
python3 partial-content-downloader.py <URL> <output-file-name>
python3 partial-content-downloader.py https://www.python.org/static/img/python-logo@2x.png p.png
```
