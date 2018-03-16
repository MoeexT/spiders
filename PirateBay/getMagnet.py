#coding: utf-8
#py -2
import os
import re
import time
import urllib2 as ulb
from bs4 import BeautifulSoup as bs

name_list = ["Mila Azul", "Lena Anderson"]
url = "http://thepiratebay.cd/search/mila%20azul/0/7/"

def download(url):
	html = ulb.urlopen(url)
	soup = bs(html, "html5lib")
	list = soup.find_all('a', href=re.compile(r'^magnet'))
	max_href_index = int(soup.find('div',align="center").contents[-4].string) - 1
	if url[-4] == '0':
		return list, max_href_index
	else:
		return list

for name in name_list:
	page = 0
	f = open(name+'.txt','a')
	magnet_num = 0
	while True:
		url = "http://thepiratebay.cd/search/" + name +"/" + str(page) + "/7/"
		if page == 0:
			mag_list, max_href_index = download(url)
		else:
			mag_list = download(url)
		for magnet in mag_list:
			f.write(magnet['href']+'\n')
			magnet_num += 1
		if page < max_href_index:
			page += 1
			print(r"sleep for a while~")
			time.sleep(1)
		else:
			break
	print("From "+name+" get "+str(magnet_num)+" magnets")
	f.flush()
	f.close()
	os.rename(name+'.txt',name+'-'+str(magnet_num)+'.txt')
	