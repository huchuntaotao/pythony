#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys

print os.environ #return dict
print os.environ.get('NLS_LANG', 'UTF-8')

print "__name__ = ", __name__ #模块名, __main__ ???
print "__file__ = ", __file__ #一般是绝对路径

curr_file = os.path.abspath(__file__) #绝对路径
print "curr_file = ", curr_file

curr_dir = os.path.dirname(curr_file) #所属目录
print "curr_dir = ", curr_dir

print "sys.path = ", sys.path #模块搜索路径, 列表
print (curr_dir in sys.path) #True


#变量是拥有匹配对象的名字（标识符）。
#命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。
#作用域: 模块>>类/函数>>方法
# dir([模块名])  返回一个排好序的字符串列表，内容是一个模块里定义过的名字。
# globals() 和 locals() 返回命名空间字典
print dir()
print globals()
print locals()


#cmd> python 执行参数.py arg1 arg2 arg3
script, first, second, third = sys.argv
print "%s,%s,%s,%s" % (script, first, second, third)