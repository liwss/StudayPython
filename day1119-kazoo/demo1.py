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


def my_watch(event):
    """监视器函数，得有一个形参，监视的节点或者子节点变化时被调用"""
    print "event:", event


@zk.ChildrenWatch("/lws")
def watch_children(children):
    """监视节点是否变化"""
    print "Children are now %s" % children


@zk.DataWatch("/lws/test/1")
def watch_node(data, state):
    """监视节点数据是否变化"""
    print "Version:", state.version, "data:", data

# zk.set("/lws/test/1", b"some data", version=5)  # 更新给定节点数据，可以提供版本号，更新前需匹配
# zk.delete("/lws/test/1", recursive=True)        # 删除zNode节点，可选择递归删除，也可提供版本号删除

while True:
    time.sleep(2)
    if zk.exists("/lws/test"):                      # 检测zNode是否存在，如存在，返回True
        # 获取给定节点的子节点列表,且可以注册监视器函数，当节点或者子节点变化时回调,exists()和get()也具备此功能
        children = zk.get_children("/lws/test", watch=my_watch)
        print "There are %s children with names %s" % (len(children), children)
        for child in children:
            data, state = zk.get("lws/test/%s" % child)        # 获取节点数据及节点详细信息
            print 'Version:', state.version, 'Data:', data
    else:
        zk.ensure_path("/lws/test")                 # 递归的创建zNode节点，但不能设置数据，只能设置ACL
        zk.create("/lws/test/1", b"value one")      # 创建zNode节点，可以设置数据
        zk.create("/lws/test/2", b"value two")
        zk.create("/lws/test/3", b"value three")
        print 'create zNode success'

