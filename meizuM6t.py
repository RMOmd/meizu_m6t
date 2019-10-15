# Скрипт для настройки VoLTE на Meizu M6t под IDC
import subprocess
import os
import time
from tkinter import *

try:
    import Tkinter as tkinter
except ImportError: # Python 3
    import tkinter

root = tkinter.Tk()
text = tkinter.Text(root)
text.pack()
text.insert('end', u" копирую build.prop")
root.after(2000, text.insert, 'end', u"\n копирую apns-conf.xml")
root.after(3000, text.insert, 'end', u"\n копирую spn-conf.xml")
root.after(5000, text.insert, 'end', u"\n монтирую system")
root.after(7000, text.insert, 'end', u"\n заменяю build.prop, apns-conf.xml и spn-conf.xml")
root.after(9000, text.insert, 'end', u"\n перегружаю устройство")
root.after(11000, text.insert, 'end', u"\n ждем включения устройства")
root.after(71000, text.insert, 'end', u"\n Заходим в настройки")
root.after(72000, text.insert, 'end', u"\n Заходим в сим-карты и сети.")
root.after(74000, text.insert, 'end', u"\n Включаю VoLTE")
root.after(76000, text.insert, 'end', u"\n Заходим в точки доступа")
root.after(78000, text.insert, 'end', u"\n Сбрасываем точки доступа.")
root.after(85000, text.insert, 'end', u"\n Выходим на рабочий стол")
root.after(87000, text.insert, 'end', u"\n Заходим в звонилку.")
root.after(89000, text.insert, 'end', u"\n Заходим в HiddenMenu")


root.geometry('400x450')
root.config(bg='white')
root.title('Meizu M6t IDC')

quit_button = Button(root, text="Закрыть", bg="blue", fg="white", command=quit)
quit_button.config(height = 2, width = 15)
quit_button.pack(side=BOTTOM)

subprocess.call("adb push F:\\scriptM6t\\build.prop //sdcard/", shell=True)
subprocess.call("adb push F:\\scriptM6t\\apns-conf.xml //sdcard/", shell=True)
subprocess.call("adb push F:\\scriptM6t\\spn-conf.xml //sdcard/", shell=True)
procId = subprocess.Popen('adb shell', stdin=subprocess.PIPE)
procId.communicate('su\n'
                   'su\n'
                   'mount -o rw,remount /system\n'
                   'cp -r /sdcard/build.prop /system/\n'
                   'cp -r /sdcard/apns-conf.xml /system/etc/\n'
                   'cp -r /sdcard/spn-conf.xml /system/etc/\n'
                   'reboot\n'
                   'exit\n'.encode())
subprocess.call("adb wait-for-device", shell=True)
os.system("adb devices")
time.sleep(60)
os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
os.system("adb shell input tap 435 990") #Заходим в настройки
time.sleep(1)
os.system("adb shell input tap 186 262") #сим-карты и сети
time.sleep(1)
os.system("adb shell input tap 631 949") #включаю вольте
time.sleep(1)
os.system("adb shell input tap 290 1228") #apn
os.system("adb shell input tap 615 110") #сброс апн
time.sleep(7)
os.system("adb shell input tap 343 1390") #выход на рабочий стол
time.sleep(1)
os.system("adb shell input tap 99 1250") #звонилка
time.sleep(1)
os.system('adb shell input text "*#*#3646633#*#*"')
root.mainloop()
