# py -2
# -*- coding:utf-8 -*- 

import os
import time
import wget
import utils_py2
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


domain = "http://thzvv.com/"
main_url = domain + "forum.php"
annex_url = domain + "forum-220-1.html"


def get_article_list(url):
	'''
	传入某模块的 URL，返回该页面的所有文章的链接
	以列表形式返回
	'''
	html = utils_py2.download(url)
	soup = bs(html, 'lxml')
	list = soup.find_all('a', class_='xst')
	del list[0]
	link_list = []
	for tag in list:
		link_list.append(domain + tag['href'])
		
	return link_list 

	
def get_cover(browser=None):
	'''
	获得封面链接
	'''
	img_list = browser.find_elements_by_class_name('zoom')
	img_src = img_list[0].get_attribute('src')
	print 'downloading: ' + img_src
	return img_src
	
	
def get_torrent(browser=None):
	'''
	获得种子链接
	'''
	while True:
		try:
			tor_src = browser.find_element_by_xpath("//a[starts-with(@href, 'http://thzvv.com/forum.php')]")
		except:
			time.sleep(1)
		else:
			break
	return tor_src
	
def get_resource(url, browser=None):
	'''
	在文章页面里下载封面和种子
	'''
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
	'''
	下载封面
	'''
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	img_src = get_cover(browser=browser)
	gif_retry = 5
	while str(img_src).endswith('gif'):
		time.sleep(1)
		img_src = get_cover(browser=browser)
		gif_retry = gif_retry - 1
		if gif_retry == 0:
			return

	wget.download(img_src, out=img_name)
	'''
	下载种子
	'''
	annex_link = browser.find_element_by_xpath("//*[starts-with(@id,'aid')]")
	annex_link.send_keys(Keys.RETURN)
	torrent = get_torrent(browser=browser)
	torrent_href = torrent.get_attribute('href')
	print '\ndownloading: ' + torrent_href
	wget.download(torrent_href, out=tnt_name)
	

def main():
	count = 1
	chrome = wd.Chrome()
	
	'''
	下载有码的，页面数为硬编码
	'''
	for i in range(13,354):
		article_list = get_article_list("http://thzvv.com/forum-220-" + str(i) + ".html") 
		for link in article_list:
			print "\ndownloading the " + str(count) + "(st) torrent..."
			get_resource(link, browser=chrome)# flag=true, make the Chrome-Object
			count = count + 1


if __name__ == "__main__":
	main()

