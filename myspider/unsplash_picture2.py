#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os,time  # 导入os模块

from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import requests  # 导入requests 模块

from myutils import myutil_file
import logging

from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support.ui import Select   #导入Select
from selenium.webdriver.chrome.options import Options

class UnsplashPicture(): 
    def __init__(self):   
        #给请求指定一个请求头来模拟chrome浏览器
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}  
        self.web_url = 'https://unsplash.com'  #要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  #设置图片要存放的文件目录
    
    def prepare(self): ##创建并切换到图片存放目录
        logging.info("Creating: %s" % self.folder_path)
        myutil_file.mkdir(self.folder_path)   
        logging.info("Change to: %s" % self.folder_path) 
        os.chdir(self.folder_path)
        
    def scroll_down(self, driver, times):
        for i in range(times):
            print "开始执行第", str(i + 1),"次下拉操作"
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #执行JavaScript实现网页下拉倒底部
            print "第", str(i + 1), "次下拉操作执行完毕"
            print "第", str(i + 1), "次等待网页加载......"
            time.sleep(30)  # 等待30秒，页面加载出来再执行下拉操作
    
    def get_picture_urls(self): ##get url(str) list
        # 使用selenium通过PhantomJS来进行网络请求
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        self.scroll_down(driver=driver, times=3)  #执行网页下拉到底部操作，执行3次
        a_tags = BeautifulSoup(driver.page_source, 'lxml').find_all('img', itemprop='thumbnailUrl')
        for a in a_tags:
            print "AAAAA:", a
        print [ a['src'] for a in a_tags ]
        return [ a['src'] for a in a_tags ]
       
    def get_picture_name(self,url): ##get pic name from url 
        return url.split('images.unsplash.com/')[1].split('?')[0] + '.jpg'    
    
    def download_picture(self, url, name): ##下载文件 
        img = requests.get(url, headers=self.headers)
        with open(name, 'ab') as fp:
            fp.write(img.content)
            
    def download_pictures(self):
        self.prepare()
        urls = self.get_picture_urls()
        for url in urls:
            name = self.get_picture_name(url)
            if not os.path.exists(self.folder_path+os.sep+name): #文件不存在才下载
                logging.info("Loading picture from %s" % url)
                self.download_picture(url,name)
            else:
                logging.info("The picture of '%s' was existed." % name)


if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unsplash = UnsplashPicture()
    unsplash.download_pictures()