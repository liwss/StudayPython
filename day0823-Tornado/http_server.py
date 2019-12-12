# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 9:49
# @describe : 模拟服务端

import tornado.web
import tornado.httpserver
import tornado.ioloop
import time
import tornado.gen
from concurrent.futures import ThreadPoolExecutor
thread_poll = ThreadPoolExecutor(1)


def test(i):
    print '------------------------'
    print time.time()
    time.sleep(i)
    return str(time.time())


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # print(str(self.request.body, encoding='utf-8'))  # python3+使用
        print self.request.body                        # python2+使用
        # time.sleep(1)
        self.write('{"age":"20","name":"lws","other":{"addr":"china","phone":"123456"}}')

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        print self.request.headers
        print self.request.body
        data = yield thread_poll.submit(test, 10)
        self.write(data)


if __name__ == '__main__':
    app = tornado.web.Application(handlers=[(r'/index', IndexHandler), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
