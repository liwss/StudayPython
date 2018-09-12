# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 17:17
# @describe : 


class Person(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(name):
        print ("%s is eating......" % name)


Person.eat('lws ')
