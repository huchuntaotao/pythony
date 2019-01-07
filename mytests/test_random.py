# -*- coding: utf-8 -*-
import random

print random.random()  # [0,1)

print random.randint(0,9) #[0,9]

print random.uniform(1,3) # [MIN,MAX]
print random.uniform(3,1) # [MIN,MAX]

print "random.randrange(start,stop,step=1)"
print random.randrange(1, 10)  # [1,10) 随机取1个整数 
print random.randrange(10, 1, -2) #(1, 10] 随机取1个偶数

nums = ['one', 'two', 'three', 'four', 'five']
print random.sample(nums, 3) # 随机抽3个元素组成新列表  , sample 取样
print random.choice(nums)  #随机抽1个元素

print "random.shuffle(x, random=None)"
a = list(range(10)) #[0,10)的列表
random.shuffle(a)  #随机打乱
print a

    
random.seed(1) #设置随机函数的初始状态, 其作用效果只有一次
for _ in range(10):
    print random.randint(1,10),
 
print ''
print '=================================='
 
for _ in range(10):
    random.seed(1) #设置随机函数的初始状态
    print random.randint(1, 10),