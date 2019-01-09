#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 名称修饰 https://blog.csdn.net/tcx1992/article/details/80105645
class Test(object):
    def __init__(self):
        self.foo = 1
        self._bar = 2
        self.__baz = 3 #触发名称修饰, __baz被解释器改成_Test__baz, 以防止意外修改

class ExtendTest(Test):
    def __init__(self):
        super(ExtendTest,self).__init__() # 找到Test类, 转换self为Test对象, 然后调用构造方法.
        self.foo='overridden'
        self._bar='overridden'
        self.__baz='overridden' # 触发名称修饰, __baz被解释器改成_ExtendedTest__baz, 以防止意外修改

class ManglingTest(object):
    def __init__(self):
        self.__mangled = 'hello' # 触发名称修饰, 双下划线名称修饰对程序员是完全透明的(看不见)。
    
    def get_mangled(self):
        return self.__mangled
    
    
_MangledGlobal__mangled = 23
class MangledGlobal(object):
    def test(self):
        return __mangled
            
print [x for x in dir(Test()) if 'baz' in x]
print [x for x in dir(ExtendTest()) if 'baz' in x]
print ManglingTest().get_mangled()
# print ManglingTest().__mangled #AttributeError: 'ManglingTest' object has no attribute '__mangled'
print MangledGlobal().test()  #23