# Automatic
import subprocess
import os
import time


subprocess.call("adb push F:\\note8_volte\\build.prop //sdcard/", shell=True)
subprocess.call("adb push F:\\note8_volte\\apns-conf.xml //sdcard/", shell=True)
subprocess.call("adb push F:\\note8_volte\\spn-conf.xml //sdcard/", shell=True)
procId = subprocess.Popen('adb shell', stdin=subprocess.PIPE)
procId.communicate('su\n'
                   'su\n'
                   'mount -o rw,remount /system\n'
                   'cp -r /sdcard/build.prop /system/\n'
                   'cp -r /sdcard/apns-conf.xml /system/etc/\n'
                   'cp -r /sdcard/spn-conf.xml /system/etc/\n'
                   'reboot\n'
                   'exit\n'.encode())
print('Перезаписали системные файлы, перегружаемся')
subprocess.call("adb wait-for-device", shell=True)
time.sleep(25)
os.system("adb devices")
os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")
os.system("adb shell input tap 655 1548") # Заходим в настройки
print("Заходим в настройки")
time.sleep(1)
os.system("adb shell input tap 273 571") # сим-карты и сети
print("Заходим в сим-карты и сети.")
time.sleep(1)
os.system("adb shell input tap 271 480") # заходим в сим-карты
print("Заходим в сим-карту ИДК.")
time.sleep(1)
os.system("adb shell input tap 936 1026") # включаю вольте
print("Включаю VoLTE")
time.sleep(1)
os.system("adb shell input tap 266 1446") # apn
print("Заходим в точки доступа")
os.system("adb shell input tap 908 177") # сброс апн
print("Сбрасываем точки доступа")
time.sleep(7)
os.system("adb shell input tap 540 2090") # выход на рабочий стол
print("Выходим на рабочий стол")
time.sleep(1)
os.system("adb shell input tap 153 1892") # звонилка
print("Заходим в звонилку")
