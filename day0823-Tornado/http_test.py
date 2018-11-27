# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/26 16:45
# @describe : 异步http请求，采用回调方式，demo1

import tornado.options
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define


define("port", default=8000, help="run on geiven port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        # print self.request.body   # 打印请求消息
        url = 'http://127.0.0.1:8000/lws/server'
        tornado.httpclient.AsyncHTTPClient().fetch(url, method='POST', body='test', callbak=self.on_response)

    def on_response(self, response):
        self.write(response.body)
        self.finish()
    # 当使用@tornado.web.asynchonous时，不会自动关闭连接，必须调用finish方法关闭
    # 否则请求将可能挂起，无法返回结果


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/lws/test", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
