
import os
from os import listdir
from json import JSONEncoder

class Test:
    resource=''
    frameName=''
    frameNum=0
    def __init__(self,resource,frameName,frameNum):
        self.resource =resource
        self.frameName = frameName
        self.frameNum = frameNum
        self.frameTime=0.05

root_path = 'bq'
subdir = os.listdir(root_path)
subdir.sort()
print(subdir)

########命令
image_format = '--opt RGBA4444 '
max_size = '--max-size 4096 '
output_data = '--data output/'
output_data_suffix = '.plist '
output_sheet = '--sheet output/'
output_sheet_suffix = '.pvr.ccz '
texture_format = '--texture-format pvr2ccz '


filter_file = '/*.png '

s = []
if '.DS_Store' in subdir:
    subdir.remove('.DS_Store')
for i in subdir:
    index = subdir.index(i) +1
    name = 'bq'+str(index)
    command = 'TexturePacker '+image_format+texture_format+max_size+output_data+name+output_data_suffix+output_sheet+name+output_sheet_suffix+root_path+'/'+i+filter_file
    files = os.listdir(root_path+'/'+i)
    files.sort()
    if '.DS_Store' in files:
        files.remove('.DS_Store')

    t = Test(name+'.plist',files[0],int(files[-1][-6:-4]))
    s.append(t)
    os.system(command)


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


if __name__ == '__main__':
    a = MyEncoder().encode(s)
    f = open('output/book_avatar.txt', 'w')
    f.write(a)

