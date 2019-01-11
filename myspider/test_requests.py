#! /usr/bin/env python
# -*- coding:utf-8 -*-

# pip install requests
# pip install beautifulsoup4 # https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# pip install lxml # BeautifulSoup可以使用lxml来解析HTML，然后提取内容
import requests


#向目标url地址发送get请求，返回一个response对象, <class 'requests.models.Response'>
r = requests.get('https://unsplash.com/')
#r.text是http response的网页HTML
print type(r), r.text

#传递参数, 构造网址    http://httpbin.org/get?key1=value1&key2=value2
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)


# post请求
# r = requests.post("http://httpbin.org/post")
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)