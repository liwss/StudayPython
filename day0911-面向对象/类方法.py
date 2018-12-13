# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/13 9:25
# @describe : 类方法是将类本身作为对象进行操作的方法


class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    def __new__(cls):
        ClassTest.addNum()
        return super(ClassTest, cls).__new__(cls)


class Student(ClassTest):
    def __init__(self):
        self.name = ''


a = Student()
b = Student()
print(ClassTest.getNum())
