import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64

PADDING = b'{'
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE).encode(encoding="utf-8")
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = '1234567890123456'
iv = '1234567890123456'

obj = AES.new(key, AES.MODE_CBC, iv)
# 获取图片数据
image = open('button.png', 'rb')
content = image.read()
# content = b'this is encrypt by python'
image.close()
print(content)
print(len(content))
content = pad(content)
print(content)
print(len(content))
chphier = obj.encrypt(content)
print(base64.b64encode(chphier))

obj2 = AES.new(key, AES.MODE_CBC, iv)
x = obj2.decrypt(chphier)
print(unpad(x))

f = open('test.enc', 'wb')
f.write(chphier)
f.close()

