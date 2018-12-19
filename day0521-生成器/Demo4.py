# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/19 15:51
# @describe : 

"""
generator的嵌套。比如说经常会yield 一个generator。当A生成器yield B生成器时，分两步：
    1 我们首先中止A的执行转而执行B
    2 当B执行完成后，我们需要将B的结果send()至A中止的地方，继续执行A
"""


def run():
    print('start running')
    yield 2     # 跑步用时2小时


def eat():
    print('start eating')
    yield 1     # 吃饭用时1小时


def time():
    run_time = yield run()
    eat_time = yield eat()
    print(run_time+eat_time)


def Runner(gen):
     r = next(gen)
    return r


t = time()
try:
    action = t.send(Runner(next(t)))
    t.send(Runner(action))
except StopIteration:
    pass