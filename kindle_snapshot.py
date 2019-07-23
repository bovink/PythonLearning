# 列表的特点
# 有序
# 可修改

# 以下是列表常用的方法
# 创建空列表
import win32gui
import time
from PIL import ImageGrab
from win32.lib import win32con

handle = win32gui.FindWindow(None, 'bovink的 Kindle for PC - 麻雀テクニック')
if handle > 0:
    print('存在')

    path = 'G:\Project\PyCharmProjects\PythonLearning\pic'
    it  = iter(range(0, 260))
    for i in it:
        im = ImageGrab.grab()
        file = path + '\\image' + str(i + 1) + '.jpg'
        im.save(file, 'jpeg')
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_LEFT, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_LEFT, 0)
        time.sleep(0.25)


else:
    print('不存在')