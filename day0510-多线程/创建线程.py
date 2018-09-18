# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 14:15
# @describe : 

import threading
import time


def test(num):
    time.sleep(1)
    print "threading %s" % num

t_obj = []
for i in range(10):     # 使用循环创建线程
    t = threading.Thread(target=test, args=(i,))  # 参数列表是元组，如无参数可以省略
    t.start()           # 开启线程
    t_obj.append(t)     # 把实例化的对象存入列表，方便对所有线程对象做join操作

for i in t_obj:
    t.join()            # 主程序等线程执行完毕再退出，阻塞主程序

print "main stop ....."
