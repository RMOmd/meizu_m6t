import os
import time

os.system("adb devices")
#time.sleep(3)
device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
#print("Waiting for connection ...")
os.system("adb shell input tap 438 845") #Заходим в настройки
#time.sleep(1)
os.system("adb shell input tap 315 778") #сим-карты и сети
#time.sleep(1)
os.system("adb shell input tap 273 272") #SIM idc
time.sleep(1)
os.system("adb shell input tap 214 535") #apn
os.system("adb shell input tap 271 1360") #новый апн
time.sleep(1)
os.system("adb shell input tap 145 236") #apn
os.system("adb shell input tap 145 1198") #apn
#time.sleep(1)
#os.system('adb shell input text "idc lte"')
os.system("adb shell input tap 500 1355") #ok
os.system("adb shell input tap 145 236") #имя apn
os.system("adb shell input tap 145 1198") #имя apn
#time.sleep(1)
#os.system('adb shell input text "4g.idknet.com"')
os.system("adb shell input tap 500 1355") #ok
os.system("adb shell input tap 162 729") #логин
os.system("adb shell input tap 145 1198") #логин
#time.sleep(1)
#os.system('adb shell input text "idc"')
os.system("adb shell input tap 500 1355") #ok
os.system("adb shell input tap 132 881") #пароль
os.system("adb shell input tap 145 1198") #пароль
#time.sleep(1)
#os.system('adb shell input text "idc"')
os.system("adb shell input tap 500 1355") #ok

os.system("adb shell input tap 343 1360") #еще
os.system("adb shell input tap 130 1167") #сохранить


os.system("adb shell input tap 342 1485") #выход на рабочий стол
time.sleep(1)
os.system("adb shell input tap 101 1367") #звонилка
time.sleep(1)
os.system('adb shell input text "*#*#86583#*#*"')
time.sleep(5)
#os.system("adb shell input tap 895 732") #ok
#time.sleep(1)
#os.system("adb shell input tap 125 526") #apn
#time.sleep(1)
#os.system('adb shell input text "idc"')
#os.system("adb shell input tap 895 732") #ok
#time.sleep(3)
#adb shell input text "Text_%s_tut"
# swipe the page
#time.sleep(5)
#os.system("adb shell input tap 340 1030 340 650 100")
# press back key
#os.system("adb shell input keyevent 4")
