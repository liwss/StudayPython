# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/21 22:55
# @describe : 生成器的send方法

def Test():
    i = 0
    while True:
        temp = yield i   # 每次执行都会卡在yeild处
        print temp
        i+=1

t = Test()
t.send(None)
print t.next()
t.send("haha")   # 相当于把haha给yield i的整体





