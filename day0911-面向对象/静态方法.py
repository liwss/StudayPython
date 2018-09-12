# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 17:17
# @describe : 


class Person(object):
    age1 = '820'
    a = 'zh'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(name):
        print ("%s is eating......" % name)

    @classmethod
    def eat1(cls):
        print ("%s is eating......" % cls.age1)


a = Person('lws')
a.eat1()
