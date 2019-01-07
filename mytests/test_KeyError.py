#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

'''
KeyError:  请求一个不存在的字典关键字
'''

d = {'a': 1, 'c': 3, 'b': 2, 'd': 4, 'host': '127.0.0.1', 'user': 'root', 'password': 'password'}
print d['user']
print d.get('user')

#get(key[,default]) 如果key存在，则返回其value,否则返回default
print d.get('port',3306) 

#setdefault(key[,default=None]) 如果key存在，则返回其value;否则插入此key，其value为default，并返回default.
print d.setdefault('charset', 'utf8')  
print d['charset']


class MyDict(dict):
    '''
    当key不存在时，会转向__missing__()方法处理，而不触发KeyError
    '''
    def __missing__(self, key):
        print "MyDict > __missing__"
        return key

mydict = MyDict(a=1, b=2, c=3)
print mydict['username']

'''
collections.defaultdict([default_factory[,...]])对象
    继承自dict, 请求一个不存在的字典关键字时, default_factory()方法被调用, 以其返回值作为value.
    如果default_factory为None，则与dict无区别; 请求一个不存在的字典关键字时, 也会触发KeyError错误
    如果default_factory参数是某种数据类型，则会返回其默认值.
'''
dct = {'a': 10, 'c': 30, 'b': 20}
dct = collections.defaultdict(None, dct)
#print dct['d'] #KeyError

def handle():
    print 'handle().........'
    return 'handle_value'
    
dct2 = collections.defaultdict(handle, dct)
print dct2['d']

dct3 = collections.defaultdict(int, dct)
print dct3['d']

