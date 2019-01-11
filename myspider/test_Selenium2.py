#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support.ui import Select   #导入Select
 

def scroll_down(self, driver, times,wait=20): ##模拟下拉操作
    for i in range(times):
        print("开始执行第", str(i + 1),"次下拉操作")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #执行JavaScript实现网页下拉倒底部
        print("第", str(i + 1), "次下拉操作执行完毕")
        print("第", str(i + 1), "次等待网页加载......")
        time.sleep(wait)  # 等待20秒（时间可以根据自己的网速而定），页面加载出来再执行下拉操作