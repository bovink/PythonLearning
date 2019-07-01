
import base64

# f = open('button.png','rb')
# c = f.read()
# print(c)
# f.close()
#
# base64data = base64.b64encode(c)
# print(base64data)



f1 = open('content.txt')
c1 = f1.read()
f1.close()

bindata = base64.b64decode(c1)
print(bindata)

f2 = open('a.png','wb')
f2.write(bindata)
f2.close()



