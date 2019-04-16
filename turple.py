zoo = ('wolf', 'elephant', 'penguin', 'penguin')

index_of_elephant = zoo.index('elephant')
print(index_of_elephant)

count_of_penguin = zoo.count('penguin')
print(count_of_penguin)

for item in zoo:
    print(item)

len = len(zoo)
print(len)

print('==========')
print(zoo[1])
print('==========')

new_zoo = ('monkey', zoo)

print('==========')
print(new_zoo[1])
print('==========')

print('==========')
print(new_zoo[1][0])
print('==========')

