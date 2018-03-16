# py -3
# -*- coding:utf-8 -*- 

import os
import time
import wget
import utils
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


domain = "http://thzvv.com/"
main_url = domain + "forum.php"
annex_url = domain + "forum-220-1.html"


def get_article_list(url):
	'''
	传入某模块的 URL，返回该页面的所有可用链接
	以列表形式返回
	'''
	html = utils.download(url)
	soup = bs(html, 'lxml')
	list = soup.find_all('a', class_='xst')
	del list[0]
	link_list = []
	for tag in list:
		link_list.append(domain + tag['href'])
		
	return link_list 

def get_resource(url, browser=None):
	browser.get(url)
	title_ = browser.title
	video_num = title_[:title_.index(']')+1] # 获得番号，[abc-123]
	format_video_num = video_num[1:-1] # 格式化番号，abc-123
	target_dir = 'resource/' + format_video_num[:format_video_num.index('-')] + '/' # 指定目录
	if not os.path.exists(target_dir): # 判断目录是否存在，否则创建
		os.mkdir(target_dir)
	else:
		pass
	
	img_name = target_dir + format_video_num + '.jpg'
	tnt_name = target_dir + format_video_num + '.torrent'
	print (type(img_name), ':', img_name)
	print (type(tnt_name), ':', tnt_name)
	'''
	下载封面
	'''
	img_list = browser.find_elements_by_class_name('zoom')
	img_src = img_list[0].get_attribute('src')
	print ('downloading: ', img_src)
	wget.download(img_src, out=img_name)
	'''
	下载种子
	'''
	annex_link = browser.find_element_by_xpath("//*[starts-with(@id,'aid')]")
	annex_link.send_keys(Keys.RETURN)
	torrent = browser.find_element_by_xpath("//*[starts-with(@href, url)]")
	torrent_href = torrent.get_attribute('href')
	print ('downloading: ', torrent_href)
	wget.download(torrent_href, out=tnt_name)
	

def main():
	chrome = wd.Chrome()
	article_list = get_article_list(annex_url) 
	for link in article_list:
		get_resource(link, browser=chrome)# flag=true, 需要创建一个浏览器对象

if __name__ == "__main__":
	main()

