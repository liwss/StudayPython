# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 10:25


from multiprocessing import Process


class ProcessNew(Process):
    """因为Process类本身也有__init__方法，这个子类相当于重写了这个方法，
       但这样就会带来一个问题，我们并没有完全的初始化一个Process类，
       所以就不能使用从这个类继承的一些方法和属性，
       最好的方法就是将继承类本身传递给Process.__init__方法，完成这些初始化操作
    """

    def __init__(self):
        Process.__init__(self)

    def run(self):
        print "我是子进程"


if __name__ == "__main__":
    p = ProcessNew()
    p.start()   # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
    p.join()
    print "------end--------"
