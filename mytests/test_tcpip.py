#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

# 打开了一个网络链接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4协议, 面向流的TCP协议
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据(向新浪服务器发送请求，要求返回首页的内容)
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据
buf = []
while True:
    # 每次最多接收1k字节
    d =s.recv(1024)
    if d: #反复接收
        buf.append(d)
    else:
        break
data = b''.join(buf)
#关闭连接
s.close()

#HTTP头和网页分离
header, html = data.split(b'\r\n\r\n',1)
print (header.decode('utf-8'))
#网页内容保存到文件
with open('sina.html', 'wb') as f:
    f.write(html)