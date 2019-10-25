import os
import time

os.system("adb devices")
#time.sleep(3)
device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")
#os.system("adb shell input tap 435 990") #Заходим в настройки
#time.sleep(1)
#os.system("adb shell input tap 186 262") #сим-карты и сети
#time.sleep(1)
#os.system("adb shell input tap 631 949") #включаю вольте
#time.sleep(1)
#os.system("adb shell input tap 290 1228") #apn
#os.system("adb shell input tap 615 110") #сброс апн
#time.sleep(7)
#os.system("adb shell input tap 343 1390") #выход на рабочий стол
#time.sleep(1)
#os.system("adb shell input tap 99 1250") #звонилка
#time.sleep(1)
#os.system('adb shell input text "*#*#3646633#*#*"')
#time.sleep(5)
os.system("adb shell input touchscreen tap 162 1254 138 1045 100") #ищем ims "adb shell input tap 340 1030 340 650 100"
os.system("adb shell input tap 112 1213") #ims
os.system("adb shell input touchscreen tap 162 1254 138 184 100") #свайпаем
os.system("adb shell input touchscreen tap 162 1254 120 765 100") #свайпаем еще
os.system("adb shell input tap 63 1147") #ставим cmw500
os.system("adb shell input tap 110 1234") #жмем set
os.system("adb shell input touchscreen tap 138 184 162 1254 100") #свайпаем назал
os.system("adb shell input touchscreen tap 120 765 162 1254 100") #свайпаем еще


#os.system('adb shell input text "idc"')
#os.system("adb shell input tap 895 732") #ok
#time.sleep(3)
#adb shell input text "Text_%s_tut"
# swipe the page
#time.sleep(5)
#os.system("adb shell input tap 340 1030 340 650 100")
# press back key
#os.system("adb shell input keyevent 4")
