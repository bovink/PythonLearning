from collections import deque

# 创建列表
myList = []
print(myList)

# 在列表尾部添加数据
myList.append(1)
print(myList)
# 插入数据
myList.insert(1, 5)
print(myList)

# 获取列表的长度
length = myList.__len__()
print('length is {}'.format(length))
length = len(myList)
print('length is {}'.format(length))

# 向列表中添加列表
addList = [1, 2, 3, 1, 2, 3, 1, 2, 3]
myList.extend(addList)
print(myList)

# 通过对象删除数据
myList.remove(2)
print(myList)
# 通过索引删除数据
del myList[0]
print(myList)
# 通过索引弹出数据
pop = myList.pop(2)
print(pop)
print(myList)

# 查询列表中指定对象的数量
count = myList.count(1)
print(count)

# 查询列表中对象的索引，可以设置查询的起点与终点
index = myList.index(1)
print(index)

# 颠倒列表
myList.reverse()
print(myList)

# 将列表当做堆栈使用，堆栈的特点为后进先出
# 关键方法为append和pop

stack = [1, 2, 3, 4]
stack.append(5)
stack.append(6)
print(stack)
last = stack.pop()
print(last)
last = stack.pop()
print(last)

# 将列表当做队列使用，队列的特点先进先出
queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)
print(queue)
last = queue.popleft()
print(last)
last = queue.popleft()
print(last)
