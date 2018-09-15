#! python3
# -*- coding:utf-8 -*- 

import time
import urllib.request as ulb


def download(url, proxy=None, num_retries=2):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    print("Downloading: " + url + "...")
    request = ulb.Request(url=url, headers=headers)
    time.sleep(1)
    try:
        html = ulb.urlopen(request).read()
        html.encoding = 'utf-8'
    except ulb.URLError as e:
        print("Download Error: " + str(e.reason))
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html
