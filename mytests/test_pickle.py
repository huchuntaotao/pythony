#! /user/bin/env python
# -*- coding: utf-8 -*-
import datetime

try:
    import cPickle as pickle #python2
except ImportError as e:
    print "It's python3, ", e.message, ", So import pickle."
    import pickle #python3
    
    
src_dic = {"date": datetime.date.today(), "other":([1, "a"], None, True, False)}
a = pickle.dumps(src_dic) #序列化对象到变量
print type(a), a

with open(r"pickle.txt", 'w') as f:
    pickle.dump(src_dic, f) #序列化对象到文件
    
with open(r"pickle.txt", 'r') as f:
    b = pickle.load(f) #序列化对象到文件
    print type(b), b
    
    
class Person(object):
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        
    def display(self):
        print "Name: %s, Age: %d" % (self.name, self.age)
        
        
person = Person('Lucy',18)
a_person = pickle.dumps(person) #序列化对象到变量
print type(a_person), a_person
b_person = pickle.loads(a_person) #反序列化
print type(b_person), b_person.display()