from random import randint
import module

module.sayHi()
print("my module version is {}".format(module.version))

i = randint(0, 99)

if i < 30:
    print("{} is less than 30".format(i))
elif i < 60:
    print("{} is less than 60".format(i))
else:
    print("{} is less than 100".format(i))

while i > 30:
    print("{} will minus 2".format(i))
    i = i - 2
    if i == 55:
        break

for i in range(0, 10):
    if i == 5 or i == 8:
        continue
    print("{}".format(i))