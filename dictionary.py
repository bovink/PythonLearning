import os
import zipfile
from os import listdir
from Crypto.Cipher import AES

# 资源路径
resource_path = 'time/waste1'

# 免费页面索引
free_pages = [1, 2]

# 免费页面过滤
free_pages_filter = []

# 免费页面
free_pages_name = []

# 收费页面
purchase_pages_name = []

for i in free_pages:
    free_pages_filter.append('page' + str(i) + '_')
    free_pages_filter.append('page' + str(i) + '.fui')

print(free_pages_filter)

for file in listdir(resource_path):
    for f in free_pages_filter:
        if f in file:
            if file not in free_pages_name:
                free_pages_name.append(file)

purchase_pages_name = set(listdir(resource_path)).difference(set(free_pages_name))
print('====================free page:%d====================' % free_pages_name.__len__())
for i in free_pages_name:
    print(i)

print('====================purchase page:%d====================' % purchase_pages_name.__len__())

# for i in purchase_pages_name:
#     print(i)

##############################加密部分代码##############################

key = '1234567890123456'
iv = '1234567890123456'

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE).encode(encoding="utf-8")
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(name):
    f = open(name, 'rb')
    content = f.read()
    f.close()
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(pad(content))


def output(data, name):
    f = open(name, 'wb')
    f.write(data)
    f.close()


# 创建免费文件夹和收费文件夹
free_dir = 'test/free/'
purchase_dir = 'test/purchase/'
try:
    os.makedirs(free_dir)
    os.makedirs(purchase_dir)
except:
    pass

for i in free_pages_name:
    output(encrypt('time/waste1/' + i), free_dir + i)

for i in purchase_pages_name:
    output(encrypt('time/waste1/' + i), purchase_dir + i)


def compress_file(zipfilename, dirname):  # zipfilename是压缩包名字，dirname是要打包的目录
    if os.path.isfile(dirname):
        with zipfile.ZipFile(zipfilename, 'w') as z:
            z.write(dirname)
    else:
        with zipfile.ZipFile(zipfilename, 'w') as z:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    if single_file != zipfilename:
                        filepath = os.path.join(root, single_file)
                        z.write(filepath)


compress_file('a.zip', 'test')
