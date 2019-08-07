
import os
from os import listdir

root_path = 'bp'
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


filter_file = '/*.png '

if '.DS_Store' in subdir:
    subdir.remove('.DS_Store')
for i in subdir:
    index = subdir.index(i) +1
    name = 'bp'+str(index)
    command = 'TexturePacker '+image_format+max_size+output_data+name+output_data_suffix+output_sheet+name+output_sheet_suffix+root_path+'/'+i+filter_file
    os.system(command)
