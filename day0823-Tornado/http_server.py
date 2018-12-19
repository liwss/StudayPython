# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 9:49
# @describe : 模拟服务端

import tornado.web
import tornado.httpserver
import tornado.ioloop
import time


class IndexHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        print(str(self.request.body, encoding='utf-8'))  # python3+使用
        # print self.request.body                        # python2+使用
        # time.sleep(1)
        self.write('liws')


if __name__ == '__main__':
    app = tornado.web.Application(handlers=[(r'/index', IndexHandler), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()