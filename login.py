#! python2
#encoding: utf-8

import os
import requests as Req

class conn(object):
	def __init__(self):
		self.post_url = "http://10.10.8.2:801/srun_portal_pc.php?ac_id=3&"
		self.ADSL = '鱼丸粗面a'
		self.username = '2015212605'
		self.password = 'mq2020.'
		self.login_headers = {
			'Host': '10.10.8.2:801',
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
				AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;\
				q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'http://10.10.8.2/index_3.html',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYylaKZYk0c%\
				252Fq867bbRsRHvJQZaJnkCcFccbII9J6frGj6wJSCrpp%252Blg9n1pbnr4\
				ywa7fTlPvrkdU62P6Evm5v0udhgtIcVXLjCUfu9%252BDEmyZUVldnmfPop6\
				1pjVIRxZ5KLhArGI9tCOvJNxdTMmLCBU%252Fwukw%252BuvtiKv9J9RYUVP\
				5nAPFqLBoHp12OtUq3dRN%252FIAxfnHsqNeIsQ%253D%253D'
			}
		self.login_data = {
			'action': 'login',
			'username': self.username,
			'password': '{B}bXEyMDIwLg==',
			'ac_id': '3',
			'save_me': '1',
			'ajax': '1'
			}
		self.logout_headers = {
			'Host': '10.10.8.2:801',
			'Proxy-Connection': 'keep-alive',
			'Content-Length': '57',
			'Accept': '*/*',
			'Origin': 'http://10.10.8.2:803',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
				AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'http://10.10.8.2:803/srun_portal_pc.php?ac_id=3&',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYylaKZYk0c%\
				252Fq867bbRsRHvJQZaJnkCcFccbII9J6frGj6wJSCrpp%252Blg9n1pbnr4\
				ywa7fTlPvrkdU62P6Evm5v0udhgtIcVXLjCUfu9%252BDEmyZUVldnmfPop6\
				1pjVIRxZ5KLhArGI9tCOvJNxdTMmLCBU%252Fwukw%252BuvtiKv9J9RYUVP\
				5nAPFqLBoHp12OtUq3dRN%252FIAxfnHsqNeIsQ%253D%253D',
			}
		self.logout_data = {
			'action': 'logout',
			'username': self.username,
			'password': self.password,
			'ajax': '1'
			}
	
	def wifi_connect(self):
		response = Req.post(url=self.post_url, data=self.login_data, headers=self.login_headers)
		print ("状态码: ", response.status_code)
		print ("响应头: ", response.headers)
		print ("响应内容", response.text.encode('UTF-8'))
		os.system('pause')

	def wifi_disconn(self):
		response = Req.post(url=self.post_url, data=self.logout_data, headers=self.logout_headers)
		print ("状态码: ", response.status_code)
		print ("响应头: ", response.headers)
		print ("响应内容", response.text.encode('UTF-8'))
		os.system('pause')

	def ADSL_connect(self):
		adsl = "rasdial 鱼丸粗面a 2015212605 mq2020." # % (self.ADSL, self.username, self.password)
		os.system(adsl)
		os.system('pause')

	def ADSL_disconn(self):
		adsl = "rasdial 鱼丸粗面a /disconnect"
		os.system(adsl)
		os.system('pause')

def main():
	connect = conn()
	detect = os.system('ping baidu.com -n 1')
	# flag = input(u"Which kind of Internet do you want to connect?(0-ADSL, 1-WIFi):")
	try:
		if detect:
			connect.wifi_connect()
		else:
			connect.wifi_disconn()
	except:
		print "proxy:127.0.0.1 should be closed~\n\
			or you havn't connect wifi"
	'''	
	if detect:
		connect.ADSL_connect()
	else:
		connect.ADSL_disconn()
	'''
if __name__ == '__main__':
	main()
	