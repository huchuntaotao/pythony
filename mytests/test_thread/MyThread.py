# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
     
    '''
    apply(func [, args [, kwargs ]]) 
        func 函数元组或字典
        args 参数元组
        kwargs 关键字参数, 如{a:'A',b:'B'} 
    '''
    def run(self):
        apply(self.func, self.args)
        

def super_play(file, t): #要播放的文件, 放几秒
    print ""
    for i in range(2): #每个文件播放两次
        print 'Start playing:%s! %s' %(file,time.ctime())
        time.sleep(t)

    
#要播放的文件字典    
lst = {'Dreams.mp3':3, 'I have a dream.mp4':4}
files = range(len(lst))

#创建线程
threads = []
for k,v in lst.items():
    t = MyThread(super_play, (k,v))
    threads.append(t)
    
    
if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()
        
    #等待线程终止 
    for i in files:
        threads[i].join()

    #主线程    
    print 'End: %s' % time.ctime()
    
