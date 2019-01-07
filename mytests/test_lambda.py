#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
lambda [arg1[, arg2, ... argN]]: expression
map(f, list) 把函数 f 依次作用在list 的每个元素上，得到一个新的 list并返回, 但是不改变原有的 list。
filter(f, list) 过滤
sorted(f, list) 排序
reduce(f2,list) 二元处理

☆sorted(iterable, cmp=None, key=None, reverse=False)
    terable：是可迭代类型; 
    cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项; 
    key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项; 
    reverse：排序规则. reverse = True 或者 reverse = False，有默认值。
    返回值：是一个经过排序的可迭代类型，与iterable一样。
'''

print range(10)
print map(lambda x: x*x, range(10))
print map(lambda x: x*x, [y for y in range(10)])

print map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,3])    #[(1, 2), (4, 4), (27, 6)]
print map(int,'1234')                               #[1, 2, 3, 4]

print map(None, [3,2,1])
print map(None, [2,4,6],[3,2,1])                    #合并 [(2, 3), (4, 2), (6, 1)]

print filter(lambda x: x % 2 == 0, [1,2,3,4]) # [2, 4]
print reduce(lambda x, y: x * y, [1,2,3,4]) #1*2*3*4 = 24

print sorted([5,2,1,4,3])  #[1, 2, 3, 4, 5]  #升序