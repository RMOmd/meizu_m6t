# Скрипт для настройки VoLTE на Meizu M6t под IDC
import subprocess
import os
import time
from tkinter import *

try:
    import Tkinter as tkinter
except ImportError:
    import tkinter
def son1():
    time.sleep(1)
def son7():
    time.sleep(7)
def son60():
    time.sleep(60)

root = tkinter.Tk()
text = tkinter.Text(root)
text.pack()

root.geometry('400x450')
root.config(bg='white')
root.title('Meizu M6t IDC')

quit_button = Button(root, text="Закрыть", bg="blue", fg="white", command=quit)
quit_button.config(height=2, width=15)
quit_button.pack(side=BOTTOM)

text.insert('end', u" копирую build.prop")

subprocess.call("adb push F:\\scriptM6t\\build.prop //sdcard/", shell=True)
root.after(2000, text.insert, 'end', u"\n копирую apns-conf.xml")
subprocess.call("adb push F:\\scriptM6t\\apns-conf.xml //sdcard/", shell=True)
root.after(3000, text.insert, 'end', u"\n копирую spn-conf.xml")
subprocess.call("adb push F:\\scriptM6t\\spn-conf.xml //sdcard/", shell=True)
root.after(5000, text.insert, 'end', u"\n монтирую system")
procId = subprocess.Popen('adb shell', stdin=subprocess.PIPE)
procId.communicate('su\n'
                   'su\n'
                   'mount -o rw,remount /system\n'
                   'cp -r /sdcard/build.prop /system/\n'
                   'cp -r /sdcard/apns-conf.xml /system/etc/\n'
                   'cp -r /sdcard/spn-conf.xml /system/etc/\n'
                   'reboot\n'
                   'exit\n'.encode())
# subprocess.call("adb wait-for-device", shell=True)
root.after(7000, text.insert, 'end', u"\n заменяю build.prop, apns-conf.xml и spn-conf.xml")
root.after(9000, text.insert, 'end', u"\n перегружаю устройство")
root.after(11000, text.insert, 'end', u"\n ждем включения устройства")
# os.system("adb devices")
son60()
root.after(71000, text.insert, 'end', u"\n Заходим в настройки")
son1()
root.after(72000, text.insert, 'end', u"\n Заходим в сим-карты и сети.")
os.system("adb shell input tap 186 262")
son1()
root.after(74000, text.insert, 'end', u"\n Включаю VoLTE")
os.system("adb shell input tap 631 949")
son1()
root.after(76000, text.insert, 'end', u"\n Заходим в точки доступа")
root.after(78000, text.insert, 'end', u"\n Сбрасываем точки доступа.")
os.system("adb shell input tap 290 1228")
os.system("adb shell input tap 615 110")
son7()
root.after(85000, text.insert, 'end', u"\n Выходим на рабочий стол")
os.system("adb shell input tap 343 1390")
son1()
root.after(87000, text.insert, 'end', u"\n Заходим в звонилку.")
os.system("adb shell input tap 99 1250")
son1()
root.after(89000, text.insert, 'end', u"\n Заходим в HiddenMenu")
os.system('adb shell input text "*#*#3646633#*#*"')
root.after(91000, text.insert, 'end', u"\n Теперь можно закрыть окно")
root.mainloop()
