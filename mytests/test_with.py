#! /usr/bin/env python
# -*- coding:utf-8 -*-

from contextlib import contextmanager
# contextlib 模块
# 装饰器 contextmanager, 函数 nested, 上下文管理器 closing
# yield


class Sample():  # 上下文管理器类
    def __init__(self):
        print "进入__init__()"

    def __enter__(self):
        print "进入__enter__()"
        return "Foo"

    def __exit__(self, exctype, excvalue, traceback):  # 异常类型, 异常对象, 异常跟踪对象
        print "exctype=%r\nexcvalue=%r\ntraceback=%r" % (exctype, excvalue, traceback)
        print "进入__exit__()\n"
        return True  # 返回True值，则异常不再被抛出

'''
调用__init__()
进入__enter__()
赋值给sample
执行代码块
调用__exit__()
'''
if __name__ == '__main__':
    with Sample() as sp:
        print "执行代码..."
        print sp

    with Sample() as sp2:
        print sp2
        i = 1 / 0
