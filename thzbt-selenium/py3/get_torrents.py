# py -3
# -*- coding:utf-8 -*- 

import time
import wget
import urllib.request as ulb
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

index = 0
url = 'http://thzvv.com/forum.php'

def download(url, proxy=None, num_retries=2):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	print ("Downloading: "+url+"...")
	request = ulb.Request(url=url, headers=headers)
	time.sleep(1)
	try:
		html = ulb.urlopen(request).read()
	except ulb.URLError as e:
		print ("Download Error: " + str(e.reason))
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)
	return html


chrome = wd.Chrome()
print("进入主页......")
chrome.get(url)
print("主页已加载完成")
target = chrome.find_element_by_link_text('')
print("进入某模块......")
target.send_keys(Keys.RETURN)
print("加载某模块完成")
list = chrome.find_elements_by_class_name('xst') # 在该页面过滤所有文章
del list[0] # 删除第一个不符合要求的文章
print("已过滤该页面所有文章")

length = len(list)

for i in range(length):
	list[index].send_keys(Keys.RETURN)
	print ("进入第", index+1, "个页面")
	print ("标题: ", chrome.title)
	annex_link = chrome.find_element_by_xpath("//*[starts-with(@id,'aid')]")
	annex_link.send_keys(Keys.RETURN)
	print ("打开隐藏窗口，睡一秒")
	time.sleep(1)
	torrent = chrome.find_element_by_xpath("//*[starts-with(@href, 'http://thzvv.com/forum.php')]")
	torrent_href = torrent.get_attribute('href')
	print ("链接: ", torrent_href)
	wget.download(torrent_href)
	index = index + 1
	chrome.back()
	list = chrome.find_elements_by_class_name('xst')