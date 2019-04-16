#
def printSomething():
    print("hello world")


printSomething()


#
def caculate(a, b):
    sum = a + b
    print(sum)


caculate(1, 2)
a = 1
b = 5

caculate(a, b)


#
def changeValue():
    global x
    print("x value is {}".format(x))
    x = 2
    print("local x value is {}".format(x))


x = 100
changeValue()
print("external x is {}".format(x))


# default value
def printServaral(string, times=1):
    for i in range(0, times):
        print(string)


printServaral("hello", 3)
printServaral("world")


# key parameter
def caculate(a, b=3, c=4):
    sum = a + b * c
    print("the sum is {}".format(sum))


caculate(1)
caculate(1, 2)
caculate(1, c=5)
caculate(c=10, a=-10)


# return specify value or it will return None

def getName(num):
    '''Prints'''
    if num < 50:
        print("lilei")
    else:
        print("hanmeimei")


getName(20)
print(getName.__doc__)
