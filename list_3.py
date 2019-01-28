# 第一种
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
