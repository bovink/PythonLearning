l = [1, 2, 3, 4, 5, 6]

len = len(l)
print(l[0])
print(l[-1])
print(l[0: len / 2])
print(l[:-2])

m = l[:]

del m[0]
print(l)
print(m)
