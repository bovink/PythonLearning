import os
from os import listdir

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

for i in purchase_pages_name:
    print(i)
