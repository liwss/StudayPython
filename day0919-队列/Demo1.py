# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 9:54
# @describe : 


import Queue

# q = Queue.Queue(5)        # fifo队列
#
# for i in range(1, 6):
#     q.put(i)
#
# for i in range(6):
#     if q.empty():
#         break
#     print q.get()
#
# print "done ......"

q = Queue.PriorityQueue()       # 创建优先级队列
q.put((1, "a"))                 # 存入元素
q.put((2, "b"))
q.put((3, "c"))

for i in range(3):
    print q.get()