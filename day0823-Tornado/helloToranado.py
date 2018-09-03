# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/8/23 9:47
# @describe :

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on geiven port", type=int)
# 指定一个默认值，类型为int，如果命令行参数给了值，则使用命令行参数的


class IndexHandler(tornado.web.RequestHandler):
    """响应请求的类里定义同名相应http方法(如get post put ...)"""
    def get(self):  # 定义get方法，处理get请求
        greeting = self.get_argument('greeting', 'Hello')   # 如果查询字符串没有第一个参数值，则使用第二个参数为默认值  127.0.0.1:8000/?greeting=lws
        self.write(greeting + ', friendly user!')  # 以字符串作为参数，将其写入http的响应

    def post(self, *args, **kwargs):
        print '-----------------------'
        return self.write("hello world")
if __name__ == "__main__":
    tornado.options.parse_command_line()   # options模块解析命令行
    app = tornado.web.Application(handlers=[(r"/", IndexHandler), (r"/liws/rest", IndexHandler)])  # 创建Application实例，传递参数handlers，指明那个类来响应请求
    # tornado.web.Application()里可以指定多个类来处理相应,以元组形式，参数1：正则，指定路径，参数2：响应类
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
