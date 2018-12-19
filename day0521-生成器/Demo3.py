# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/19 15:38
# @describe : 

"""
讲解：
1   f = foo()  这句表示生成一个generator对象
    f = foo()
    print(type(f))  #<class 'generator'>
2   f.send(None) 的作用与 next(f) 的作用相同：运行代码到  r = yield 2 处。 r = yield 2 主要分两步：
　　第一步： yield 2 ，也就是先返回2
　　第二步： r = (yield) 这里用括号把yield包起来是为了突出yield是一个表达式expression：可以用来表示某个值。
    f.send(None) 或者说 next(f) 仅仅运行到了第一步，也就是返回了2，然后被print()函数打印到屏幕
3   f.send(1) 运行第二步，将1赋值给r ，然后运行print(r)，再一次运行到 r = yield 2 处时，也仅仅只运行第一步，也就是返回2，然后由print()函数打印到屏幕。
"""


def foo():
    print('starting')
    while True:
        r = yield 2
        print('r:', r)


f = foo()
print(f.send(None))    # 等价于next(f),运行代码到yield
print(f.send(1))       # 如果不把代码运行到yield处而直接send，会报错TypeError: can't send non-None value to a just-started generator
