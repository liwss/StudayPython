# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/4 10:31
# @describe : 装饰器（高阶函数+函数嵌套）

import time


def timer(flag):
    def wrapper(func):
        def deco(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            stop_time = time.time()
            print ("run func %s" % (stop_time-start_time))
            return res
        return deco
    return wrapper


@timer  # test1 = timer(test1)
def test1():
    time.sleep(1)
    print ("in the test1")


@timer  # test2 = timer(test2)
def test2(name):
    time.sleep(1)
    print ("name:", name)
    print ("in the test2")
    return name


# 带有参数的装饰器被装饰在某个函数上时，相当于一个函数会被直接调用，不过他的返回值是一个装饰器
@timer(flag="1")   # test3 = timer(flag='1')(test3)
def test3():
    time.sleep(1)
    print ("in the test3")

# test1 = timer(test1)
# test1()
# test2 = timer(test2)
test2("lws")
print (test2("820"))
test3()
