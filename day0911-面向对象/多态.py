# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 16:29
# @describe : 多态，一个接口，多种实现


class Dog(object):
    def print_self(self):
        print("大家好,我是xxxx,希望以后大家多多关照....")


class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大,我是xxxx")


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
