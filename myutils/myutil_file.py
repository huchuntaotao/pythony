#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

# https://www.cnblogs.com/zhengyuxin/articles/1940954.html 

         
def mkdir(path): ##创建文件夹
    path = path.strip() #移除字符串头尾指定的字符（默认为空格）
    if os.path.exists(path):
        return 0 #目录已有,跳过.
    else:
        os.makedirs(path)
        return 1 #创建成功

        
if __name__ == '__main__':
    fname,fename=os.path.split("E:/lpthw/zedshaw/ex19.py")
    print fname,'---------', fename  #返回文件的路径和文件名
    
    a = os.path.split("E:/lpthw/zedshaw/ex19.py")
    print type(a)
    
    
    fname,fename=os.path.splitext('/home/ubuntu/python_coding/split_func/split_function.py')#将文件名和扩展名分开
    print fname,'---------', fename
    
    
    mkdir("11")