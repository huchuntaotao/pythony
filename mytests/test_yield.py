#! /usr/bin/env python
# -*- coding:utf-8 -*-
from __builtin__ import type


def addlist(lst):
    print "Hello, I'm here!"
    for i in lst:
        yield i + 1


# <type 'generator'> <generator object addlist at 0x00000000023F4438>
# Hello, I'm here!
# 2 3 4
generator_obj = addlist([1, 2, 3])  # 此时,print未执行!
print type(generator_obj), generator_obj
for x in generator_obj:
    print x,  # 2 3 4


def hello():  # ________________________1
    print '\nHello...!'
    m = yield 5  # ________________________2 返回值5
    print 'm=', m
    d = yield 12  # _______________________3 返回值12
    print 'd=', d
    print 'ByeBye...!'  # ________________________4


h = hello()  # ________________________1
# h.close()  # 中断 Generator, next()/send()不再可用.
# 调用next(), 开始执行hello(), 直到遇到yield,打印Hello...!
m = h.next()  # 相当于h.send(None) # ________________________2
print m

# (yield 5)表达式被赋予了'Fighting...!'
d = h.send('Fighting...!')  # ________________________3
print d

# 没有再遇到yield了，拋出StopIteration异常.
d = h.next()  # ________________________4
