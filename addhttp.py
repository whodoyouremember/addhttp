import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urlparse import *


# 若原域名有http或者https则去掉只保留域名
def http_face(url):  
	if 'http' in url:
		url= urlparse(url)
		return url.netloc
	else:
		return url

# 给域名添加http：//并判断是否连接成功
def req(url):
	url = "http://" + url
	for i in range(3):
		try:
			url_ = requests.get(url, timeout=3)
			code = url_.status_code
			if code == 200 :
				return url
			else:
				return False
		except :
			pass
		sleep(0.8)
	return False

# 访问url，获取最终url
def real_url(url):
	chrome_options=Options()
	chrome_options.add_argument('--headless')
	browser = webdriver.Chrome(options=chrome_options)
	browser.get(url)
	sleep(1)
	url = browser.current_url
	return url
	browser.close()
	browser.quit()


f = open('test.txt') 

for url in f:
	url =url.strip('\n')
	url = http_face(url)
	url = req(url)
	if url != False:
		url = real_url(url)
		print url
		with open("test.csv","a") as mon:
			mon.write(url + '\n')

print 11111	
