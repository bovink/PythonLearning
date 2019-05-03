def testyield(a):

        yield a
        a += 2


for i in testyield(2):
    print(i)
