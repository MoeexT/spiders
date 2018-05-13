#py -3
'''
dictionary:
	附件: annex
	
'''
import wget
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

url = 'http://thzvv.com/forum.php'

chrome = wd.Chrome()
# 进入主页
chrome.get(url)
target = chrome.find_element_by_link_text('***')  # 和谐相关板块名
target.send_keys(Keys.RETURN) 
# 进入某模块
list = chrome.find_element_by_class_name('xst') # 在该页面过滤所有文章
del list[0] # 删除第一个不符合要求的文章

for article in list:
	article.send_keys(Keys.RETURN)
	annex_link = chrome.find_element_by_xpath("//*[starts-with(@id,'aid')]")
	annex_link.send_keys(Keys.RETURN)
	torrent = chrome.find_element_by_xpath("//*[starts-with(@href, url)]")
	torrent_href = torrent.get_attribute('href')
	wget.download(torrent_href)
	chrome.back()

list[2].send_keys(Keys.RETURN) # 随便进入某文章内
annex_link = chrome.find_element_by_xpath("//*[starts-with(@id,'aid')]") # 找到附件链接
annex_link.send_keys(Keys.RETURN) # 点击附件链接
torrent = chrome.find_element_by_xpath("//*[starts-with(@href, url)]")
torrent_href = torrent.get_attribute('href')
wget.download(torrent_href))

