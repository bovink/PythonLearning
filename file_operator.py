s = raw_input("please input something")

print("your input is {}".format(s))

poem = '''\
program is fun
whe the work is done
if you wanna make your work also fun:
    use python!
    '''

f = file('poem.txt', 'w')

f.write(poem)
f.close()

f = file('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,

f.close()
