import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = '123'
key = pad(key)
iv = Random.new().read(16)
# iv = pad(iv)
obj = AES.new(key, AES.MODE_CBC, iv)

# message = "The answer is no"
# 读图
file = open('button.png','rb')
filecontent = file.read()
file.close()

ciphertext = obj.encrypt(filecontent)
print(ciphertext)

f2 = open('a.txt','wb')
f2.write(base64.b64encode(iv+ciphertext))
f2.close()





# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# a = obj2.decrypt(ciphertext)
# print(a)
# print(type(a))

# 存图
s = open('a.txt','rb')
sc= s.read()
s.close()

h = base64.b64decode(sc)
iv = h[:16]
aa = h[16:]
obj2 = AES.new(key, AES.MODE_CBC, iv)

n = obj2.decrypt(aa)

f2 = open('a.png','wb')
f2.write(n)
f2.close()
