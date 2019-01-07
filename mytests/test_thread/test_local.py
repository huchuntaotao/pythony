# -*- coding: utf-8 -*-
import time
import threading

def worker():
    x = 0  #局部变量
    for i in range(100):
        time.sleep(0.000001)
        x += 1
    print "Worker1:", time.ctime(),threading.current_thread(),x
    
    
y = 0 #全局变量
def worker2():
    global y 
    for i in range(100):
        time.sleep(0.000001)
        y += 1
    print "Worker2:", time.ctime(),threading.current_thread(),y


#创建线程并启动   
for i in range(10):
    threading.Thread(target=worker).start()
    
#创建线程并启动    
for i in range(10):
    threading.Thread(target=worker2).start()
    
    
'''
Python提供了 threading.local 类，将这个类实例化得到一个全局对象，
但是不同的线程使用这个对象存储的数据其它线程不可见
(本质上就是不同的线程使用这个对象时为其创建一个独立的字典)。
'''

#每个子线程使用全局对象a，但每个线程定义的属性a.x是该线程独有的。
a = threading.local()

def a_worker():
    a.x=0
    for i in range(100):
        time.sleep(0.000001)
        a.x += 1
    print "a_worker:", time.ctime(),threading.current_thread(),a.x

    
#创建线程并启动    
for i in range(10):
    threading.Thread(target=a_worker).start()