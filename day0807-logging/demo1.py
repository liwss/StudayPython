# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/8/7 13:09
# @describe : logging 模块

import logging

LOG_FORMAT = "%(asctime)s %(levelname)s |>>>>> [%(message)s] "  # 配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S '  # 配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=r"D:\code\python\StudayPython\day0807-logging\debug.log"
                    # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

logging.debug("msg1:")
logging.debug("msg1")
logging.debug("msg1")


