# 单循环
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
# 第二种
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)
# 第三种
squares = [x ** 2 for x in range(10)]
print(squares)

# 双重循环
list = [(x, y) for x in [1, 2, 3] for y in [2, 5, 7] if x != y]
print(list)
# 等价于
list = []
for x in [1, 2, 3]:
    for y in [2, 5, 7]:
        if x != y:
            list.append((x, y))
print(list)
