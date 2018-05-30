# coding=utf-8

import heapq

# heapq模块的: nlargest()和nsmallest()函数,可以快速获取集合中最大最小的几个   值，并返回列表，且可以对复杂集合接受关键字参数当作筛选条件

date = [1, 34, 23, 9, 12, 29,9]

print(heapq.nlargest(1, date))
print(heapq.nsmallest(1, date))

nums = [
	{'name': 'lws', 'age': 25},
	{'name': 'zh', 'age': 27},
	{'name': 'liws', 'age': 29}
]

print(heapq.nsmallest(2, nums, key=lambda s: s['age'])) # 以age的值为条件
print(heapq.nlargest(2, nums, key=lambda s: s['age']))

date1 = [1, 34, 23, 9, 12, 29,9]
heapq.heapify(date1) # heapq.heapqify():将列表原地转换为堆，且heap[0]永远是最元素
print(date1)
print(heapq.heappop(date1)) # heap.heappop():弹出排序好后堆中最小的元素
print(heapq.heappop(date1))
print(heapq.heappop(date1))


