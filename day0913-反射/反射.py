# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/13 14:53
# @describe : hasattr()判断对象是否有某个属性或方法
#             getattr()获取对象中的方法或变量的内存地址
#             setattr()为对象添加变量或方法
#             delattr()为对象删除属性,不能删除方法


def talking(self, name):
    print ("%s is talking with %s......" % (self.name, name))


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print ("%s is eating %s......" % (self.name, food))

dog = Dog('lisi')

choice = raw_input(">>>:").strip()
if hasattr(dog, choice):         # hasattr()判断对象是否有某个属性或方法
    print getattr(dog, choice)
    func = getattr(dog, choice)  # getattr()获取对象中的方法或变量的内存地址
    func('apple')                # 调用实例方法
else:
    setattr(dog, 'talk', talking)  # 将talking函数添加到对象中dog中，并命名为talk
    dog.talk(dog, 'lws')                  # 调用talk方法，因为这是额外添加的方法，需手动传入对象
