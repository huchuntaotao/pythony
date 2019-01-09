#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

# https://www.cnblogs.com/zhengyuxin/articles/1940954.html          
def copyFiles(sourceDir,  targetDir):
    for f in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  f)
        targetFile = os.path.join(targetDir,  f)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)
            

def copyfile(sourceFile,targetFile):
    targetDir = os.path.split(targetFile)[0]
    if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                open(targetFile, "wb").write(open(sourceFile, "rb").read())

def deleteBySize(dirpath, minSize):
    """删除小于minSize的文件（单位：K）"""
    files = os.listdir(dirpath)  #列出目录下的文件
    for f in files:
        if os.path.getsize(file) < minSize * 1000:
            os.remove(file)    #删除文件
            print(f + " deleted")
    return
 
def deleteNullFile(dirpath):
    '''删除所有大小为0的文件'''
    files = os.listdir(dirpath)
    for f in files:
        if os.path.getsize(file)  == 0:   #获取文件大小
            os.remove(file)
            print(f + " deleted.")
    return
 
def create():
    '''根据本地时间创建新文件，如果已存在则不创建'''
    import time
    t = time.strftime('%Y-%m-%d',time.localtime())  #将指定格式的当前时间以字符串输出
    suffix = ".docx"
    newfile= t+suffix
    if not os.path.exists(newfile):
        f = open(newfile,'w')
        print newfile
        f.close()
        print newfile + " created."
    else:
        print newfile + " already existed."
    return


 
        
if __name__ == '__main__':
    fname,fename=os.path.split("E:/lpthw/zedshaw/ex19.py")
    print fname,'---------', fename  #返回文件的路径和文件名
    
    a = os.path.split("E:/lpthw/zedshaw/ex19.py")
    print type(a)
    
    
    fname,fename=os.path.splitext('/home/ubuntu/python_coding/split_func/split_function.py')#将文件名和扩展名分开
    print fname,'---------', fename