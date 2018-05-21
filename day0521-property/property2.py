# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/21 20:44
# @describe : property的装饰器方法


class Test(object):
    def __init__(self):
        self.__num = 0

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newnum):
        self.__num = newnum

t = Test()
t.num = 100
print t.num