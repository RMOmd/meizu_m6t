# Скрипт для настройки VoLTE на Meizu M6t под IDC
import subprocess
import os
import time

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
print('Готово')
subprocess.call("adb wait-for-device", shell=True)
os.system("adb devices")
time.sleep(60)
os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")
os.system("adb shell input tap 435 990") #Заходим в настройки
print("Заходим в настройки")
time.sleep(1)
os.system("adb shell input tap 186 262") #сим-карты и сети
print("Заходим в сим-карты и сети.")
time.sleep(1)
os.system("adb shell input tap 631 949") #включаю вольте
print("Включаю VoLTE")
time.sleep(1)
os.system("adb shell input tap 290 1228") #apn
print("Заходим в точки доступа")
os.system("adb shell input tap 615 110") #сброс апн
print("Сбрасываем точки доступа")
time.sleep(7)
os.system("adb shell input tap 343 1390") #выход на рабочий стол
print("Выходим на рабочий стол")
time.sleep(1)
os.system("adb shell input tap 99 1250") #звонилка
print("Заходим в звонилку")
time.sleep(1)
os.system('adb shell input text "*#*#3646633#*#*"')
print("Заходим в HiddenMenu")
