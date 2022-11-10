import os
import time

os.system("adb shell input swipe 550 1180 550 500 100") # разблокируем экран
print("Разблокируем экран ")
time.sleep(2)
os.system("adb shell input tap 150 1825") # Заходим в настройки
print("Заходим в настройки")
time.sleep(1)
os.system("adb shell input tap 240 271") # заходим в подключения
print("Заходим в подключения.")
time.sleep(1)
os.system("adb shell input tap 225 1670") # заходим в мобильные сети
print("Заходим в мобильные сети.")
time.sleep(1)
os.system("adb shell input tap 200 650") # apn
print("Заходим в точки доступа")
os.system("adb shell input tap 860 125") # добавить апн
print("Добавляем точки доступа")
time.sleep(1)
os.system("adb shell input tap 170 345") # имя апн
print("Ввод имени точки доступа")
time.sleep(1)
os.system("adb shell input text 'idc lte'")
time.sleep(1)
os.system("adb shell input tap 888 807") # ok
time.sleep(1)
os.system("adb shell input tap 170 510") # апн
print("Ввод имени точки доступа")
os.system('adb shell input text "4g.idknet.com"')
time.sleep(1)
os.system("adb shell input tap 888 807") # ok
time.sleep(1)
os.system("adb shell input tap 170 1150") # login
print("Ввод имени точки доступа")
os.system('adb shell input text "idc"')
time.sleep(1)
os.system("adb shell input tap 888 807") # ok
time.sleep(1)
os.system("adb shell input tap 170 1300") # pass
print("Ввод имени точки доступа")
os.system('adb shell input text "idc"')
time.sleep(1)
os.system("adb shell input tap 888 807") # ok
time.sleep(1)
os.system("adb shell input tap 1000 150") # save
time.sleep(1)
os.system("adb shell input tap 720 165") # save
time.sleep(1)
os.system("adb shell input tap 75 125") # выход из карты
print("Выход из сим-карт")

os.system("adb shell input tap 555 2175") # выход на рабочий стол
print("Выходим на рабочий стол ")
time.sleep(1)
os.system("adb shell input tap 100 1915") # звонилка
print("Заходим в звонилку")
