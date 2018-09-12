# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/12 14:23
# @describe : 


class Person(object):  # 新式类（super是新式类写法）   class Person:  经典类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print ("%s is eating......" % self.name)

    def talk(self):
        print ("%s is talking......" % self.name)

    def sleep(self):
        print ("%s is sleeping......" % self.name)


class Action(object):
    def friend(self, obj):
        print ("%s make friends with %s" % (self.name, obj.name))


class Man(Person):
    def __init__(self, name, age, money):
        # Person.__init__(self, name, age)  # 调用父类的初始化方法，初始化父类属性
        super(Man, self).__init__(name, age)  # 等效类名+方法，新式类写法
        self.money = money                # 子类新增加的属性


class Woman(Person, Action):
    pass


m1 = Man("lws", 20, 1000)
w1 = Woman('820', 15)
w1.friend(m1)




