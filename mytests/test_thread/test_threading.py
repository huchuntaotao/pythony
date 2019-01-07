#! /usr/bin/env python
# -*- coding:utf-8 -*-

from time import ctime, sleep
import threading


def music(name):
    for i in range(2):
        print "%s: 我正在听<<%s>>..." % (ctime(), name)
        sleep(1)


def movie(name):
    for i in range(2):
        print "%s: 我正在看<<%s>>..." % (ctime(), name)
        sleep(2)


def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        movie(name)
    else:
        print "Error: 没有找到合适的播放器!"


def super_player(filename, t):
    for i in range(2):
        print "%s:开始播放<<%s>>, 放[%d]秒." % (ctime(), filename, t)
        sleep(t)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        apply(self.func, self.args)  # apply(func [, args [, kwargs ]])  间接调用函数


# 多任务时代
threads = []  # 创建线程组
t1 = threading.Thread(target=music, args=('爱情买卖',))  # 创建线程
t2 = threading.Thread(target=movie, args=('阿凡达',))  # 创建线程
threads.append(t1)  # 加入线程组
threads.append(t2)  # 加入线程组


lst2 = ['十年.mp3', '夏洛特烦恼.mp4']
threads2 = []
for i in range(len(lst2)):
    t = threading.Thread(target=player, args=(lst2[i],))
    threads.append(t)


lst3 = {'青花瓷.mp3': 3, '喜剧之王.mp4': 4}
threads3 = []
for filename, t in lst3.items():
    t = threading.Thread(target=super_player, args=(filename, t))
    threads3.append(t)

lst4 = {'爱情买卖.mp3': 3, '勇敢者游戏.mp4': 4}
threads4 = []
for k, v in lst4.items():
    t = MyThread(super_player, (k, v), super_player.__name__)
    threads4.append(t)

if __name__ == '__main__':

    # 单任务时代 DOS
    music('我在人民广场吃炸鸡')
    movie('西虹市首富')
    print "%s:时间到了, 该睡觉了..." % ctime()

    # 多任务时代
    for t1 in threads:
        t1.start()
    for t in threads:  # 等待线程终止
        t1.join()
    print "%s:时间到了, 该睡觉了1..." % ctime()

    for t2 in threads2:
        t2.start()
    for t2 in threads2:  # 等待线程终止
        t2.join()
    print "%s:时间到了, 该睡觉了2..." % ctime()

    for t3 in threads3:
        t3.start()
    for t3 in threads3:  # 等待线程终止
        t3.join()
    print "%s:时间到了, 该睡觉了3..." % ctime()

    for t4 in threads4:
        t4.start()
    for t3 in threads4:  # 等待线程终止
        t4.join()
    print "%s:时间到了, 该睡觉了4..." % ctime()
