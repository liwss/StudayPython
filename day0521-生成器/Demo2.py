# -*- coding: gbk -*-

# @Author   : lws
# @Time     : 2018/9/5 15:31
# @describe : Э��

import time


def consumer(name):
    print("%s ׼���԰�����" %name)
    while True:
       baozi = yield
       print("����[%s]����,��[%s]����!" %(baozi,name))

c = consumer("ChenRonghua")
c.next()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.next()
    c2.next()
    print("���ӿ�ʼ׼����������!")
    for i in range(10):
        time.sleep(5)
        print("����1������,������!")
        c.send(i)
        c2.send(i)

producer("alex")
