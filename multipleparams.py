def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
print(powersum(3, 2, 2, 2))

x = 3
assert x == 1