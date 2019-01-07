#! /usr/bin/env python
# -*- coding:utf-8 -*-
import types


# types模块
# 包含了标准解释器定义的所有类型的类型对象
# 同一类型的所有对象共享一个类型对象

class A(object):
    pass

def check(obj):
    print obj,
    
    if type(obj) is types.IntType:
        print "Integer"
    elif type(obj) is types.FloatType:
        print "Float"
    elif type(obj) is types.StringType:
        print "String"
    elif isinstance(obj,types.ClassType): #???
        print "Class"
    elif type(obj) is types.InstanceType: #???
        print "Instance"
    else:
        print "Unknown"
        
check(0)
check(0.0)
check('0')
check(A)
check(A())