#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import cmp_to_key  # 转比较函数为关键字函数
from functools import partial  # 冻结函数参数
from functools import reduce as freduce  # 累积序列元素
from functools import total_ordering  # 补全排序方法
from functools import update_wrapper  # 更新包裹函数属性 方法
from functools import wraps  # 更新包裹函数属性 装饰器


# comparison function
# 比较函数是可调用的，接受两个参数，比较这两个参数并根据他们的大小关系返回负值、零或者正值中的一个。
# key function
# 关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值。
def compare(x, y):
    return x - y


a = [3, 2, 1]
print sorted(a, key=cmp_to_key(compare))  # [1, 2, 3] 返回一个排序好的序列, 原序列不变
print a  # [3, 2, 1]

f = partial(compare, 100)  # 冻结参数a, a=100
print f(10)  # 100-10=90

print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15
print freduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15


@total_ordering
class Person(object):  # 补全排序方法 __eq__();  __lt__()， __le__()，__gt__()，__ge__()
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return (self.first_name.lower(), self.last_name.lower()) == (other.first_name.lower(), other.last_name.lower())

    def __lt__(self, other):
        return (self.first_name.lower(), self.last_name.lower()) < (other.first_name.lower(), other.last_name.lower())


p1 = Person('A1', 'B1')
p2 = Person('a2', 'a2')
print p1 == p2, p1 < p2, p1 <= p2, p1 > p2, p1 >= p2


# 用被包裹函数的属性(__name__、__module__、__doc__和 __dict__等)更新包裹函数的属性
# 使被包裹函数的属性不丢失
def wrapper(f):  # 自定义装饰器
    def wrapper_function(*args, **kw):  # 包裹函数
        '''
        __doc__:wrapper_function
        '''
        return f(*args, **kw)
    update_wrapper(wrapper_function, f)  # 更新包裹函数
    return wrapper_function  # 返回包裹函数


@wrapper
def wrapped():  # 被包裹函数
    '''
    __doc__:wrapped
    '''
    pass


#----------------------------------------------------------


def wper(f):
    @wraps(f)  # 等价于update_wrapper(wper_f,f)
    def wper_f(*args, **kw):
        return f(*args, **kw)
    return wper_f


@wper
def wped():
    pass


print wrapped.__name__
print wped.__name__
