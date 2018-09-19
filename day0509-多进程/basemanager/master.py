# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 19:45
# @describe : 


from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from Queue import Queue

task_queue = Queue()
result_queue = Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    QueueManager.register(typeid="get_task_queue", callable=return_task_queue)
    QueueManager.register(typeid="get_result_queue", callable=return_result_queue)

    manager = QueueManager(address=('127.0.0.1', 55555), authkey='lws')
    # freeze_support()
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        print('put task %d...' % i)
        task.put(i)
    # 从result队列读取结果
    print('try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('result:%s' % r)
