#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
 
class Date(object):
    def __init__(self,year,month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @staticmethod
    def now(): #静态方法 
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    
    @classmethod
    def yesterday(cls): #类方法
        t=time.localtime(time.time()-86400)
        return cls(t.tm_year,t.tm_mon,t.tm_mday) #哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    #__str__定义在类内部，必须返回一个字符串类型，
    #什么时候会出发它的执行呢？打印由这个类产生的对象时，会触发执行
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)
    
if __name__ =='__main__':
    t1 = Date.now()
    t2 = Date.tomorrow()
    print t1.day,t2.day
    
    print EuroDate.yesterday()