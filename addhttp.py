import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse


def http_face(url):
	if 'http' in url:
		url= urlparse(url)
		return url.netloc
	else:
		return url

def req(url):
	url = "http://" + url
	try:
		url_ = requests.get(url, timeout=3)
		code = url_.status_code
		if code == 200 :
			return url
		else:
			return False
	except :
		pass


def real_url(url):
	try:
		chrome_options=Options()
		chrome_options.add_argument('--headless')
		browser = webdriver.Chrome(options=chrome_options)
		browser.get(url)
		sleep(1)
		url = browser.current_url
	except:
		pass
	finally:
		browser.close()
		browser.quit()		
		return url

f = open('test.txt') 

for url in f:
	url =url.strip('\n')
	url = http_face(url)
	url = req(url)
	if url != False:
		url = real_url(url)
		print (url)
		with open("url.csv","a") as mon:
			mon.write(url + '\n')

print 'Finish!!!'
