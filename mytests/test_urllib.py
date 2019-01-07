#! /usr/bin/env python
# -*- coding:utf-8 -*-
import urllib

# https://www.cnblogs.com/sysu-blackbear/p/3629420.html


# urllib.urlopen(url, [data, proxies, context])
# 打开一个url，返回一个文件对象，进行类似文件对象的操作。
url = 'http://www.baidu.com'

f = urllib.urlopen(url)
print type(f),f #<type 'instance'> 类文件对象

line1 = f.readline()
print type(line1), line1  #<type 'str'>

#lines = f.readlines()
#print type(lines), lines #<type 'list'>

fno = f.fileno()
print type(fno), fno #<type 'long'>

info = f.info() 
print type(info),info #<type 'instance'> 响应头信息

code = f.getcode()
print type(code),code #<type 'int'> 状态码

url2 = f.geturl()
print type(url2),url2 #<type 'str'>,即url

f.close()


# urllib.urlretrieve(url, [filename, reporthook, data, context])
# 定位url到html文件, 下载到本地硬盘中,默认存为临时文件。
# urllib.urlcleanup() 清除由于urllib.urlretrieve()所产生的缓存
url = 'http://www.baidu.com'
htmlfile = urllib.urlretrieve(url)
#<type 'tuple'> ('c:\\users\\fhadmin\\appdata\\local\\temp\\tmp9flt5w', <httplib.HTTPMessage instance at 0x00000000027389C8>)
print '\n\n',type(htmlfile), htmlfile  

htmlfile = urllib.urlretrieve(url,filename='C:\\Users\\fhadmin\\Desktop\\baidu.html')
print type(htmlfile), htmlfile

urllib.urlcleanup()


# urllib.quote(url)和urllib.quote_plus(url)
# 将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。
# urllib.unquote(url)和urllib.unquote_plus(url)
qt = urllib.quote('http://www.baidu.com')
# <type 'str'> http%3A//www.baidu.com
print type(qt),qt
qtp = urllib.quote_plus('http://www.baidu.com') #//
# <type 'str'> http%3A%2F%2Fwww.baidu.com 
print type(qtp),qtp


# urllib.urlencode(query) 将URL中的键值对以连接符&划分
params = urllib.urlencode({'spam':1, 'eggs':2, 'bacon': 0})
# <type 'str'> eggs=2&bacon=0&spam=1
print type(params), params
f = urllib.urlopen("http://python.org/query?%s" % params) #GET
# content = f.read()
# print type(content),content  #<type 'str'>
print f.geturl() #http://www.python.org/query?eggs=2&bacon=0&spam=1

f = urllib.urlopen("http://python.org/query", params) #POST
print f.read()

