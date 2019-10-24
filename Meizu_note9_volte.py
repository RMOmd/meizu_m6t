# Automatic
import subprocess
import os
import time


subprocess.call("adb push F:\\note9_VOLTE\\build.prop //sdcard/", shell=True)
subprocess.call("adb push F:\\note9_VOLTE\\apns-conf.xml //sdcard/", shell=True)
subprocess.call("adb push F:\\note9_VOLTE\\spn-conf.xml //sdcard/", shell=True)
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
time.sleep(20)
os.system("adb devices")
os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")

os.system("adb shell input swipe 550 1700 550 500 100") # разблокируем экран
print("Разблокируем экран")
time.sleep(2)
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
os.system("adb shell input tap 600 1670") # apn
print("Заходим в точки доступа")
os.system("adb shell input tap 920 190") # сброс апн
print("Сбрасываем точки доступа")
time.sleep(7)
os.system("adb shell input tap 70 170") # назад из apn
print("Выход из точки доступа")
time.sleep(1)
os.system("adb shell input tap 70 170") # выход из карты
print("Выход из сим-карт")
time.sleep(1)
os.system("adb shell input tap 70 170") # выход из сим-карты
print("Выход из карт")
time.sleep(1)
os.system("adb shell input tap 260 1260") # ищем режим самолета
print("Ищем режим самолета")
os.system("adb shell input tap 935 365") # включаем самолет
print("Включаем режим в самолете")
time.sleep(3)
os.system("adb shell input tap 935 365") # выключаем самолет
print("Выключаем режим в самолете")

os.system("adb shell input tap 540 2190") # выход на рабочий стол
print("Выходим на рабочий стол")
time.sleep(1)
os.system("adb shell input tap 145 1950") # звонилка
print("Заходим в звонилку")
