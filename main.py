import os
os.system("title Data")
from tkinter import *
from Login import *
import tkinter as tk
import platform
import socket

print ("==========运行环境==========")
print('操作系统名称：', platform.system()) #获取操作系统名称
print('操作系统名称及版本号：', platform.platform()) #获取操作系统名称及版本号
print('操作系统版本号：', platform.version()) #获取操作系统版本号
print('操作系统的位数：', platform.architecture()) #获取操作系统的位数
print('计算机类型：', platform.machine()) #计算机类型
print('计算机的网络名称：', platform.node()) #计算机的网络名称
print('计算机处理器信息：', platform.processor()) #计算机处理器信息
print("当前的本地IP地址：",socket.gethostbyname(socket.getfqdn(socket.gethostname())))
print ("============================")
os.system("title Data")
root = tk.Tk()
root.title('学生成绩管理系统')
LoginPage(root)
root.mainloop()

