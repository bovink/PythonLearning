import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = '1234567890123456'
iv = '1234567890123456'

obj = AES.new(key, AES.MODE_CBC, iv)
msg = 'something encrypt by python'
chphier = obj.encrypt(pad(msg))
print(base64.b64encode(chphier))
print(len(chphier))
print(chphier)

f = open('test.enc', 'wb')
f.write(chphier)
f.close()

