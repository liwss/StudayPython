# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/27 17:12
# @describe : tornado.gen模块执行异步http请求demo

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop


from tornado.options import define, options

define("port", default=8000, type=int, help="run on geiven port")


class IndexHandler(tornado.web.RequestHandler):
    pass


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/lws/test', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
