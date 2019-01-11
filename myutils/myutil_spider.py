#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
from myutil_is import is_empty

# https://www.cnblogs.com/zhengyuxin/articles/1940954.html 


if __name__ == '__main__':
    fname,fename=os.path.split("E:/lpthw/zedshaw/ex19.py")
    print fname,'---------', fename  #返回文件的路径和文件名
    
    a = os.path.split("E:/lpthw/zedshaw/ex19.py")
    print type(a)
    
    
    fname,fename=os.path.splitext('/home/ubuntu/python_coding/split_func/split_function.py')#将文件名和扩展名分开
    print fname,'---------', fename
