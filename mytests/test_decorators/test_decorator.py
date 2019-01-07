#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.cnblogs.com/zh605929205/p/7704902.html

'''
@decorator
def func():
    pass
=> func = decorator(func)
把一个函数当参数传到另一个函数中再回调，
把decorator这个函数的返回值赋值回了原来的func。

@decorator_one
@decorator_two
def func():
    pass
=> func = decorator_one(decorator_two(func))

@decorator(arg1, arg2)
def func():
    pass
=> func = decorator(arg1,arg2)(func)
这意味着decorator(arg1, arg2)这个函数需要返回一个“真正的decorator”。
'''


def hello(msg):  
    def wrapper(fn): 
        print msg 
        print "hello, %s" % fn.__name__
        print "goodbye, %s" % fn.__name__
        return fn
    return wrapper

@hello('wow!')  # foo = hello('wow')(foo)
def foo():
    print "I'm a foo."
    
foo()
