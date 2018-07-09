# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/7/9 9:07
# @describe : 解析配置文件

import ConfigParser

configfile = "D:\code\python\StudayPython\day0709-ConfigParser\config\config.properties"


class ManagerConfig:
    def __init__(self):
        try:
            self.config = ConfigParser.ConfigParser()
            self.config.read(configfile)
        except Exception:
            print configfile + " error!"

    def getInstance(self):
        return self.config


if __name__ == '__main__':
    a = ManagerConfig().getInstance()
    print a.get("s3979Inter", "url")
    inputxml = a.get("s3979Inter", "xml")
    aa = ("a", "b", "c")
    print inputxml % aa
