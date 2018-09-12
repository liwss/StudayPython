# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/11 9:01
# @describe :

import time


class Test:
    num = 1  # 类变量
    print num

    def __init__(self, name, age):   # 构造函数，在类实例化时完成初始化
        self.name = name   # 实例变量，作用域就是实例本身
        self.age = age

    def show(self):
        print (self.name, self.age)

    def __del__(self):
        print "------析构函数------"

a = Test('lws', 20)
# del a
# time.sleep(1)
# print ("------------------")
# b = Test('820', 18)

b = a
del a
time.sleep(1)
print "________________"
b.show()

