# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/19 21:37
# @describe : kazoo的异步用法,异步使用官网文档的回调及CURD操作有问题，待后续学习？

import sys
from kazoo.client import KazooClient
from kazoo.handlers.gevent import SequentialGeventHandler
# from kazoo.handlers.eventlet import SequentialEventletHandler
from kazoo.exceptions import ConnectionLossException
from kazoo.exceptions import NoAuthException

# 建立连接，Kazoo不依赖于gevent的monkey补丁，并且要求传入适当的处理程序，默认为SequentialGeventHandler()
# eventlet也同上
zk = KazooClient(hosts='39.107.88.145:2181', timeout=1, handler=SequentialGeventHandler())
event = zk.start_async()

event.wait(timeout=1)  # wait()方法等待start_async()返回的事件对象

if not zk.connected:   # 由于可能永远连接失败，因此判断连接状态，做异常情况处理
    zk.stop()
    raise Exception("Unable to connect")


def my_callback(async_obj):
    try:
        print '-------------------------'
        children = async_obj.get()
        do_something(children)
    except (ConnectionLossException, NoAuthException):
        sys.exit(1)

zk.create_async("/lws/test/1", b"test")
data = zk.get_async("/lws/test/1")
print data

async_obj = zk.get_children_async("/lws/test/1")
# print async_obj
async_obj.rawlink(my_callback)

# data = zk.exists_async("/lws/test/1")
# print data
