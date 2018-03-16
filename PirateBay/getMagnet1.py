#! python 2
#coding: utf-8

import os
import re
import time
imprt random

import urlparse
import urllib2 as ulb
from bs4 import BeautifulSoup as bs

name_list = ["Mila Azul", "Lena Anderson"]
url = "http://thepiratebay.cd/search/mila%20azul/0/7/"
'''
	获取连接，返回 html Result对象
	用户代理
	重试
'''
def download(url, user_agent='wswp', proxy=None, num_retries=2):
	print ("Downloading: " + url)
	headers = {'User-agent': user_agent}
	request = ulb.Request(url, headers=headers)
	
	opener = ulb.build_opener()
	if proxy:
		proxy_params = {urlparse.urlparse(url).scheme: proxy}
		opener.add_handler(ulb.ProxyHandler(proxy_params))
	try:
		html = opener.open(request).read()
	except ulb.URLError as e:
		print ("Download Error:" + e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, user_agent, num_retries-1)
	if url[-4] == '0':
		soup = bs(html, "html5lib")
		max_href_index = int(soup.find('div',align="center").contents[-4].string) - 1
		return html, max_href_index
	else:
		return html
		
'''
	传入 Result html对象，解析并返回目标 标签对象列表 和 最大页数
'''
def get_links(html):
	soup = bs(html, "html5lib")
	list = soup.find_all('a', href=re.compile(r'^magnet'))
	return list

def main(name_list):	
	for name in name_list:
		page = 0
		f = open(name+'.txt','a')
		magnet_num = 0
		while True:
			url = "http://thepiratebay.cd/search/" + name +"/" + str(page) + "/7/"
			if page == 0:
				html, max_page_index = download(url)
			else:
				html = download(url)
			magnet_list = get_links(html)
			for magnet in magnet_list:
				f.write(magnet['href']+'\n')
				magnet_num += 1
			if page < max_page_index:
				page += 1
				print(r"Sleep for one second...")
				time.sleep(random.random()*2)
			else:
				break
		print("From "+name+" get "+str(magnet_num)+" magnets")
		f.flush()
		f.close()
		os.rename(name+'.txt',name+'-'+str(magnet_num)+'.txt')
		

if __name__ == '__main__':
	main(name_list)