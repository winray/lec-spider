# -*- coding: utf-8 -*-
import urllib
import urllib2
import re 
import os

#本地存储的文件夹
dest = "lecture-1"
if not os.path.exists(r'D:\Users\61742\Desktop\pachong\%s' %dest):
	os.mkdir(r'D:\Users\61742\Desktop\pachong\%s' %dest)
path = r'D:\Users\61742\Desktop\pachong\%s' %dest 

#想要下载网页的url
url = "http://eden.sysu.edu.cn/m/lecture/142/"

#抓取课件的图片&下载到本地
def getJpg(html):
	#正则匹配文件格式
    r=r'src="(http.*page-\d+\.jpg)"'
    re_jpg=re.compile(r)  
    jpgList=re.findall(re_jpg,html)

    #把图片下载到本地文件夹 
    filename=1  
    for jpgUrl in jpgList:
    	#print jpgUrl
    	loc = os.path.join(path, str(filename)+".jpg")
        urllib.urlretrieve(jpgUrl, loc)  
        print  'file "%s.jpg" done' %filename  
        filename+=1

#利用已登录的Cookies等请求头信息模拟登录网站
headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'safedog-flow-item=2F2468A0E6D7EC8F2C046D1CA1E54967; csrftoken=zIdiRUkpdber3wVXXmBAcKkUsKqUYq8s; sessionid=t427dhajocsa7ay8tj5gmq2dwvd4c2ml',
    'Host': 'eden.sysu.edu.cn',
    'Referer': 'http://eden.sysu.edu.cn/m/cw/14/',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
}

request = urllib2.Request(url=url, headers=headers)

response = urllib2.urlopen(request)
tar = response.read()

getJpg(tar)