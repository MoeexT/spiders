#! python3
# -*- encoding: utf-8 -*-
# filename: bd_image_crawler.py
# @time: 2018/9/15 22:09


import re
import wget
#  from bs4 import BeautifulSoup as bs
from urllib import parse
from util.crawler_util import download

url = """
    https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&
    cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1537020473577_R&pv=&ic=0&nc=1&z=&
    se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1537020473578%
    5E00_1536X728&word="""


def download_images():
    for img_url in url_list:
        wget.download(img_url, out=r"D:\url")  # TODO


def get_img_urls(url_list):
    pass


def main(keyword):
    html = download(url+keyword)
    pattern = '"objURL":"(.*?)",'
    img_list = re.findall(pattern, html, re.S)
    next_page = '<a href="(.*)" class="n">下一页</a>'


if __name__ == '__main__':
    word = "小麦白粉病"
    keyword = parse.quote(word)
    main(keyword)
