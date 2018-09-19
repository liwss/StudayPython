# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 20:16
# @describe : 

import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    QueueManager.register(typeid='get_task_queue')
    QueueManager.register(typeid='get_result_queue')
    manager = QueueManager(address=('127.0.0.1', 55555), authkey='lws')
    manager.connect()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    while True:
        try:
            time.sleep(0.5)
            ret = task.get()
            print "开始处理任务 %d" % ret
            result.put(ret**2)
            print "处理结果 %d" % ret**2
        except Exception as e:
            print e
            break
    print "任务处理完成"