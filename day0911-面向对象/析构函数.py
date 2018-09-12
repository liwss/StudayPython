# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 10:32
# @describe : 对象只有引用计数为0时，才会被销毁而调用析构函数

import time


class Test:
    def __init__(self):
        print "构造函数"+"id=%s"%id(self)

    def __del__(self):
        print "-------析构函数---------"


a = Test()   # 实例化一个对象用a引用
b = Test()   # 实例化一个对象用b引用
a = Test()   # 实例化一个对象用a引用，会导致第一个a的指向指向现在的对象地址，之前的地址引用为0，调用一次析构方法
time.sleep(1)
print "------------------"
del b       # 删除b,对象地址的引用变0，调用一次析构方法
time.sleep(1)
print "---------------"   # 程序接收，所有的对象都会被销毁，因此销毁剩下的a对象地址，调用一次析构函数
