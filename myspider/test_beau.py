#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://www.cnblogs.com/Albert-Lee/p/6232745.html
# pip install requests
# pip install beautifulsoup4 # https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# pip install lxml # BeautifulSoup可以使用lxml来解析HTML，然后提取内容
import requests
import re

from bs4 import BeautifulSoup
from bs4.element import Comment

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')  #BeautifulSoup ->表示一个文档的全部内容
tag = soup.find('p') #Tag-> 第一个p标签
head_tag = soup.head #查找head标签
p_tag = soup.p #第一个p标签

print type(head_tag)
print("find's return type is ", type(tag))  #输出返回值类型
print("find's content is", tag)  #输出find获取的值
print("find's Tag Name is ", tag.name)  #输出标签的名字
print("find's Attribute(class) is ", tag['class'])  #输出标签的class属性值
print "NavigableString is :" , tag.string  #NavigableString ->标签中的文本内容（不包含标签）

child_of_head = head_tag.children #直接子节点 <type 'listiterator'>
parents_of_first_p = p_tag.parents #所有父节点
# tag.next_siblings  所有的兄弟节点
# tag.next_sibling  后面的兄弟节点
# tag.previous_sibling   前面的兄弟节点
print "直接子节点", type(child_of_head)


print "--------------------------------------------"
print soup.find_all("title") #bs4.element.ResultSet
print soup.find_all("p","title")
print soup.find(string=re.compile("sisters"))
#soup.find(name标签名, attrs属性名, recursive是否深入检索默认True, text搜索文档中字符串的内容)

#  find()  ->bs4.element.Tag

print "--------------------------------------------"

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'lxml')
comment = soup.b.string
print type(comment)  #Comment  ->HTML和XML中的注释

print "该字符是注释" if type(comment)==Comment else "该字符不是注释"




