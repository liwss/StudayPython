# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/3/7 10:05
# @describe : tornado异步客户端连接redis的使用

import tornadoredis


c = tornadoredis.Client(host="39.107.88.145", port=6379, password='liws')
# 测试是否连接成功，写一个key，并查看redis数据库是否存在该key
c.set("name", "zhangsan")
