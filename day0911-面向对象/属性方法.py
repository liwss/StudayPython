# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 20:24
# @describe : property


class Test(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):    # 获取属性
        print ("%s is eating %s ......" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):     # 设置属性
        self.__food = food
        print ("set %s is ok" % food)

    @eat.deleter
    def eat(self):          # 删除属性
        del self.__food
        print ("删除属性")

a = Test('lws')
a.eat
a.eat = 'banana'
a.eat
del a.eat