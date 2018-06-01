# coding=utf-8

import heapq


class PriorityQueue(object):
    def __init__(self):
		self._quene = []
		self._index = 0

	def push(self, item, priorty):
		"""队列由（priority, index, item)形式的元祖构成"""
		heapq.heappush(self._quene, (-priorty, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._quene)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item: {!r}'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('grok'), 1)
    for i in range(4):
        print(q._quene)
        print(q.pop())
