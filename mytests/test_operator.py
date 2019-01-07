#! /user/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt
from math import pow
'''
Q: 
'''

#加减乘除取模取整除求幂开平方
a = 10
b = 3
print a + b 
print a - b
print a * b
print a / b #3

print a % b #1
print a // b #3

print a ** b
print pow(a, b)
print sqrt(a)

#0、空、FALSE
if not False:
    print "Flase is False."
if not 0:
    print "0 is False."
if not None:
    print "None is False."

#逻辑与或非
x = 998
y = 0 
print x and y  #0  如果 x 为 True，返回 y 的值。
print x or y   #998 如果 x 为非 0，返回 x 的值
print 0 or 9527 # 9527 如果 x 为 0，返回 y 的值
print not x    #False

#位运算
m = 10
n = 3
l = m & n
o = m << 2 #左移, 越移越大
p = m >> 2 #右移, 越移越小
print "Number = %d, Binary number = %r" % (m, bin(m))
print "Number = %d, Binary number = %r" % (n, bin(n))
print "Number = %d, Binary number = %r" % (l, bin(l))
print "Number = %d, Binary number = %r" % (o, bin(o))
print "Number = %d, Binary number = %r" % (p, bin(p))
