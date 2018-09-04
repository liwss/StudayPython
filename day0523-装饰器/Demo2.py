# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/4 10:31
# @describe : 装饰器（高阶函数+函数嵌套）

import time


def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print ("run func %s" % (stop_time-start_time))
    return deco


@timer  # test1 = timer(test1)
def test1():
    time.sleep(1)
    print ("in the test1")


@timer  # test2 = timer(test2)
def test2():
    time.sleep(1)
    print ("in the test2")

# test1 = timer(test1)
test1()
# test2 = timer(test2)
test2()
