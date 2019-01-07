#! /usr/bin/env python
# -*- coding:utf-8 -*-

# object是所有类的超类; 
# type是object的类型,也就是说object是type的实例; 
# 同时,object又是type的超类。

# python是面向对象的语言。在python里面，所有的东西都是对象的概念。
# 在面向对象的体系中,存在两种关系:
# 1. 父子关系: 
# 这种关系存在于某个类（subclass）是另一个类（superclass）的特别版本之中。
# 比如：猫是一种爬行动物。其中，蛇(Cat)是子类,动物(Animal)是父类。猫拥有动物的特征，同时，又拥有标志自己是一只猫的特征。
# 2. 类型实例关系:
# 这种关系存在于两个对象之中，其中一个对象(实例)是另一个对象(类型)的具体实现。
# 比如:我有一条宠物猫叫Tom，那么Tom就是猫的一个实例。
# 还有两个规则:
# 1. 如果X是A的实例，同时A又是B的子类，那么，X也是B的实例。
# 2. 如果B是C的实例，同时A是B的子类，那么，A也是C的实例。



# http://blog.jobbole.com/21351/
# 在大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段。
class ObjectCreator(object):
    pass
# 将在内存中创建一个对象，名字就是ObjectCreator。
# 这个对象（类）自身拥有创建对象（类实例）的能力，而这就是为什么它是一个类的原因。
# 但是，它本质上仍然是一个对象，于是乎你可以对它做如下的操作：
# 1) 你可以将它赋值给一个变量
# 2) 你可以拷贝它
# 3) 你可以为它增加属性
# 4) 你可以将它作为函数参数进行传递


#函数中创建类 
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
MyClass = choose_class('foo')
print type(MyClass),MyClass,MyClass()


#type中创建类
MyShinyClass = type('MyShinyClass',(),{})
print type(MyShinyClass),MyShinyClass, MyShinyClass()

def showinfo(self):
    print "NAME:%s, AGE:%d" %(self.name,self.age)
class Foo(object):
    pass
FooChild = type('FooChild', (Foo,), {'name':'Lucy', 'age': 18, 'showinfo':showinfo})
print type(FooChild),FooChild,FooChild(),FooChild().showinfo()


# class Foo(object): #此时, 类对象Foo还没有在内存中创建。Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。
#     __metaclass__ = something…
# […]

# class Foo(Bar):
#     pass
# Foo中有__metaclass__这个属性吗？
# 如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象。
# 如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
# 如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
# 现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。
# 那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。


# 元类的主要目的就是为了当创建类时能够自动地改变类。1)拦截类的创建2)修改类3)返回修改之后的类
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    print "Enter upper_attr()...!"
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)
 

class Goo(object):
    __metaclass__ = upper_attr
    bar = 'bip'
print hasattr(Goo, 'bar') # 输出: False
print hasattr(Goo, 'BAR') # 输出:True
print hasattr(Goo(), 'bar') # 输出: False
print hasattr(Goo(), 'BAR') # 输出:True  

# 自定义元类
# Python中的一切都是对象，它们要么是类的实例，要么是元类的实例，除了type。type实际上是它自己的元类
# __new__ 是在__init__之前被调用的特殊方法
# __new__是用来创建对象并返回之的方法
# 而__init__只是用来将传入的参数初始化给对象
# 你很少用到__new__，除非你希望能够控制对象的创建
# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
# 如果你希望的话，你也可以在__init__中做些事情
# 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        print "cls=%r\nname=%r\nbases=%r\ndct=%r\n" % (cls, name, bases, dct)
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        #return type.__new__(cls, name, bases, uppercase_attr)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
    
class Uoo(object):
    __metaclass__ = UpperAttrMetaclass
    uoo_attr = 'abcdefg'
    pass

print Uoo().UOO_ATTR
