#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os  # 导入os模块

from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import requests  # 导入requests 模块

from myutils import myutil_file
import logging

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
        
                
    def get_picture_urls(self): ##get url(str) list
        response = requests.get(self.web_url, headers=self.headers)
        a_tags = BeautifulSoup(response.text, 'lxml').find_all('img', itemprop='thumbnailUrl')
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