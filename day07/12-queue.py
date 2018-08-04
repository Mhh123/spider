from queue import Queue

#  创建一个对象，5代表队列长度， 不写无限长
q = Queue(5)

print(q.full())
print(q.empty())
print(q.qsize())


#  向队列添加元素
q.put('勒布朗')
q.put('韦德')
q.put('科比')
q.put('哈登')
q.put('库里')

#  队列满之后，默认一直等待
# q.put('邓肯', False)
# q.put('邓肯', True, 5)

for i in range(6):
    print(q.get(False))

# 队列没有元素，默认等待
# print(q.get(False))
# print(q.get(True, 3))
