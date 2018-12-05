# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 15:49
# @describe : 


from tornado import gen
import tornado.httpclient


@gen.coroutine
def call_server():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch('www.baidu.com')
    print response.body
    # raise gen.Return(response.body)



