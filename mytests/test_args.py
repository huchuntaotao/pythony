#! /usr/bin/env python
# -*- coding:utf-8 -*-

#*args 可变非关键字参数, **kw 可变关键字参数

def show(*args, **kw):
    print type(args), args
    print type(kw), kw

#<type 'tuple'> (1, 'a', 'b')  3个非关键字参数
#<type 'dict'> {'c': '3X', 'd': '4X'} 2个关键字参数
show(1,'a','b',c='3X',d='4X') 

#<type 'tuple'> ([1, 'a', 'b'], {'c': '3X', 'd': '4X'}) 1个非关键字参数
#<type 'dict'> {}  #0个关键字参数
show([1,'a','b'],{'c':'3X', 'd':'4X'})