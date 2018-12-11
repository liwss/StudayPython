# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 15:49
# @describe : 


from tornado import gen
import tornado.httpclient
import tornado.ioloop


@gen.coroutine
def call_server():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(request='http://127.0.0.1:8000/index', method='POST', body='test')
    # print response.body                           # python2+使用
    print(str(response.body, encoding='utf-8'))     # python3+使用


async def call_server1():
    """python3.5新增关键字async和await，等价于gen的装饰器写法，也被称为原生协程"""
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = await http_client.fetch(request='http://127.0.0.1:8000/index', method='POST', body='test')
    print(str(response.body, encoding='utf-8'))     # python3+使用


if __name__ == '__main__':
    tornado.ioloop.IOLoop.instance().run_sync(call_server1)


