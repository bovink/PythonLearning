import os

s = os.listdir('json_file/')


def sort_list(elem: str):
    s: str = elem.split('.')[0]
    n = s[1:]
    if '_' in n:
        n2 = n.split('_')
        m = float(n2[0]) + float(n2[1]) * 0.1
    else:
        m = float(n)

    return m


s.sort(key=sort_list)
for i in s:
    print(i)



