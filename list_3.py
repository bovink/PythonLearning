# 可以用简洁的语法创建列表
# 首先是控制语句的执行顺序，按照从左往右的顺序去理解

# 单个循环
list = [x for x in range(10)]
print(list)
# 多个循环
list = [(x, y) for x in range(-3, 0) for y in range(0, 3)]
print(list)
# 添加条件语句
list = [(x, y) for x in range(-3, 0) for y in range(0, 3) if abs(x) != abs(y)]
print(list)

# 其次遍历出来的元素可以对其执行方法，包括多重嵌套方法，如果其本身包含可执行的方法也可以执行
list = [abs(x) for x in range(-4, 5)]
print(list)
list = [str(abs(x)) for x in range(-4, 5)]
print(list)
list = [x.strip() for x in ['aaaaa ', ' bbbbb', ' cc c cc ']]
print(list)
