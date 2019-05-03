# 使用yield的原因。
# 方法想返回一个list，方便复用
# 但是直接返回list会占用内存
# 使用yield关键字不会占用内存，而且也能遍历
# 当使用方法时，方法里的代码并没有运行，只是返回的是一个generator对象，包含参数和方法
# 只有当这个generator对象执行for循环时，才会真正运行代码，并且只能运行一次for循环。

# 获取给定范围内的奇数
def getNum(min, max):
    l = []
    for i in range(min, max):
        if (i % 2 == 1):
            l.append(i)
    return l


def getNum2(min, max):
    for i in range(min, max):
        if (i % 2 == 1):
            yield i


num = getNum(0, 100)
generator = getNum2(0,100)
print(num)
print(generator)

for i in num:
    print(i)

print('=====')
for i in num:
    print(i)

