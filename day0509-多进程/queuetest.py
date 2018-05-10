# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 16:51

from multiprocessing import Queue

"""
使用multiprocessing模块的Queue实现多进程之间的数据传递，Queue本身是一个消息列队程序

q = Queue()  1:若括号中没有指明消息最大存储数量或数值为负，那么可接受消息数量没上限，直到内存耗尽
             2:若括号中指明了消息最大数量，则存储数量最大为制定数字

Queue.qsize()  返回队列包含消息数量
Queue.empty()  如果队列为空，返回True,否则返回False
Queue.full()   如果队列满了，返回True,否则返回False

Queue.get([block[, timeout]])
    1：block默认值为True，且没有设置timeout，程序将堵塞直到读到数据
       block默认值为True，设置timeout，程序将堵塞多长时间，若还无数据，则抛出Queue.empty异常
    2：若设置block为False，消息队列如果为空，立即抛出Queue.empty异常
       Queue.get_nowait()：相当Queue.get(False)；

Queue.put(item,[block[, timeout]])
    1：block默认值为True，且没有设置timeout，程序将被阻塞直到队列有空间写入
       block默认值为True，设置timeout，程序将阻塞多长时间后抛出Queue.full异常
    2：如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；
       Queue.put_nowait(item)：相当Queue.put(item, False)

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()
"""


q = Queue(3)

for msg in range(5):
    try:
        q.put(msg, True, 3)
        print msg
    except:
        print "消息队列已满，现有消息数量:%s" % q.qsize()


