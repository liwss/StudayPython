# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/19 9:05
# @describe :

from kazoo.client import KazooClient
from kazoo.client import KazooState
import logging
import time

logging.basicConfig()   # 解决建立连接异常因没有传入log日志对象而产生的报错
zk = KazooClient(hosts='39.107.88.145:2181', timeout=1)  # 建立zk连接，超时时间设置为1s


@zk.add_listener  # my_listener = zk.add_listener(my_listener)
def my_listener(state):
    """监听客户端连接状态
        此函数看似没有显示调用，实际调用在装饰器中，也就是return时"""
    if state == KazooState.LOST:
        print 'lost'
    elif state == KazooState.SUSPENDED:
        print 'suspended'
    else:
        print 'connected'

zk.start()

# zk.set("/lws/test/1", b"some data test")  # 更新给定节点数据，可以提供版本号，更新前需匹配
zk.delete("/lws/test/1", recursive=True)      # 删除zNode节点，可选择递归删除，也可提供版本号删除
time.sleep(2)
zk.create("/lws/test/1", b"value one")


