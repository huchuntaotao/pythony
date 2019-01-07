# -*- coding: utf-8 -*-
import time
import threading

def music(name):  #音乐电影播放器(歌曲名称)
    for i in range(2):  
        print "I was listening to music %s. %s" % (name, time.ctime())
        time.sleep(2) #1
        
def movie(name):  #电影播放器(电影名称)
    for i in range(2): 
        print "I was at the movies! %s. %s" % (name, time.ctime())
        time.sleep(2)
        
        
threads = []
t1 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
t2 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
t3 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
t4 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
t5 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
t6 = threading.Thread(target=movie, args=('A Fan Da!',)) #创建线程
t7 = threading.Thread(target=movie, args=('A Fan Da!',)) #创建线程
t8 = threading.Thread(target=movie, args=('A Fan Da!',)) #创建线程
t9 = threading.Thread(target=movie, args=('A Fan Da!',)) #创建线程
t10 = threading.Thread(target=music, args=('Go go go!',)) #创建线程
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
threads.append(t5)
threads.append(t6)
threads.append(t7)
threads.append(t8)
threads.append(t9)
threads.append(t10)
print "threads=", threads
    
    
if __name__ == '__main__':
    #顺序执行
    music("<Go go go!>")
    movie("<A Fan Da!>")
    print "all over %s" % time.ctime()
    print ""
    
    #多线程执行
    for t in threads:
        t.setDaemon(True) #声明为守护线程,否则程序会被无限挂起
        t.start() #开始线程活动 子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()没有等待子线程后直接退出，同时子线程也一同结束。
  
    print "all over %s" % time.ctime()