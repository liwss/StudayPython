# -*- coding: gbk -*-

# @Author   : lws
# @Time     : 2018/9/5 15:31
# @describe : 协程

import time


def consumer(name):
    print("%s 准备吃包子了" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer("ChenRonghua")
c.next()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.next()
    c2.next()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(5)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)

producer("alex")
