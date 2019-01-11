#!/usr/bin/env python
# -*- coding: UTF-8 -*-

### selenium能作什么? 个人认为其中比较重要的就是定位，即找到页面中的元素，然后进行相关操作。


from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support.ui import Select   #导入Select

driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
driver.get("https://www.baidu.com/")  #请求网页地址

# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
#assert "百度一下，你就知道" in driver.title  #看看"百度一下，你就知道"关键字是否在网页title中，如果在则继续，如果不在，程序跳出。  raise-if-not
elem = driver.find_element_by_id("kw")  #找到id='kw'的元素，这里是个搜索框
elem.clear()  #清空搜索框中的内容
elem.send_keys("python")  #在搜索框中输入python
elem.send_keys(Keys.RETURN)  #相当于回车键，提交
#assert "No results found." not in driver.page_source  #如果当前页面文本中有“No results found.”则程序跳出
#driver.close()  #关闭webdriver

"""
<select name="cars">
  <option value ="volvo">沃尔沃</option>
  <option value ="bmw">宝马</option>
  <option value="benz">奔驰</option>
  <option value="audi">奥迪</option>
</select>

"""
## 操作下拉框
# from selenium.webdriver.support.ui import Select  
# select = Select(driver.find_element_by_name('cars'))  #找到name为cars的select标签
# select.select_by_index(1)  #下拉框选中沃尔沃
# select.select_by_visible_text("宝马")  #下拉框选中宝马
# select.select_by_value("benz")  #下拉框选中奥迪

# elem.click() 点击操作

##在请求网站的时候添加Cookies。
# driver.get("http://www.example.com") #先请求一个网页
# cookie = {'name' : 'foo', 'value' : 'bar'} #设置cookie内容
# driver.add_cookie(cookie)  #添加cookie
