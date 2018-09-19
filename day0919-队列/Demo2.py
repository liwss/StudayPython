# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 11:35
# @describe : task_done和join的用法示例

import threading
import queue
from time import sleep


class MyThread(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.queue = que

    def run(self):
        # while True:
        for i in range(10):  # 如果把for循环改为9，则程序一直阻塞，因为join判断队列元素不为空
            sleep(1)
            if self.queue.empty():
                break
            item = self.queue.get()
            print(item, '!')
            self.queue.task_done()      # 每次取出一个元素，调用task告诉join，join判读是否继续阻塞
        return

que = queue.Queue()
for x in range(10):
    que.put(x)

t = MyThread(que)
t.start()
que.join()      # 阻塞，直到队列元素处理完成，才会执行下面程序
print('---success---')
