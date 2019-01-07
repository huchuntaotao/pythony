#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score =score
    
    @property #把getter/setter方法装饰成属性调用
    def score(self):
        return self.__score
        
    @score.setter #@property装饰器衍生品
    def score(self,score):
        if score<0 or score>100:
            raise ValueError('Invalid score.')
        self.__score=score
        
if __name__ == '__main__':
    stu = Student('Lucy', 90)
    stu.score=100
    stu.score=1000