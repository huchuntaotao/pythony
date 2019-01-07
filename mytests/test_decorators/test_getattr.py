#! /usr/bin/env python
# -*- coding:utf-8 -*-

# __getattribute__ 拦截点号运算,所有的属性
# __getattr__方法 拦截点号运算,未定义的属性
# __setattr__方法 拦截属性赋值,所有的属性.

# 1.object.__getattr__(self, name)
# 当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。
#
# 2.object.__getattribute__(self, name)
# 无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常）
#
# 3.object.__get__(self, instance, owner)
# 如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。
# （descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）


class A(object):
    a = 'AAA'

    def __init__(self, name):
        self.name = name  # __setattr__

    def __getattr__(self, key):
        print "__getattr__"

    def __setattr__(self, key, value):
        print "__setattr__"

    def __get__(self, instance, owner):
        print "__get__ : ", instance, owner
        return self


class C(object):
    foo = A('Hanmeimei')


print A.a  # AAA
# print A.b  # AttributeError: type object 'A' has no attribute 'b'

print '-----------------------'
obj = A('Lucy')  # __setattr__
print obj.a      # AAA
print obj.b     # __getattr__ None

print '-----------------------'
A.a = 100        #
A.b = 300        #

print '-----------------------'
obj.a = 200      # __setattr__
obj.b = 400      # _setattr__


C().foo  # __get__ :  <__main__.C object at 0x000000000257B2E8> <class '__main__.C'>
