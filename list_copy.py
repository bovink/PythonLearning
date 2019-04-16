def printList(list):
    for item in list:
        print(item)
    print("print end")


l = []

#
newlist = [1, 2, 3, 4, 5]
l.extend(newlist)
printList(l)

print('==========')
print(l[0])
print('==========')

#
l.append(1)
printList(l)

#
the_count_of_1 = l.count(1)
print(the_count_of_1)

#
the_index_of_1 = l.index(1, 1)
print(the_index_of_1)

print("end")
pop_item = l.pop(3)
print("the pop item is {}".format(pop_item))
printList(l)

l.insert(0, 4)
printList(l)

for i in range(0, the_count_of_1):
    l.remove(1)

printList(l)

l.reverse()
printList(l)

len = len(l)
print(len)