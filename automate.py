import os
import time

os.system("adb devices")
time.sleep(3)
device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")
os.system("adb shell input tap 261 1434") #mobile networks
time.sleep(1)
os.system("adb shell input tap 216 1030") #apn
time.sleep(1)
os.system("adb shell input tap 785 155") #add
time.sleep(1)
os.system("adb shell input tap 155 340") #name apn
time.sleep(1)
os.system('adb shell input text "idc"')
os.system("adb shell input tap 895 732") #ok
time.sleep(1)
os.system("adb shell input tap 125 526") #apn
time.sleep(1)
os.system('adb shell input text "idc"')
os.system("adb shell input tap 895 732") #ok
time.sleep(3)
#adb shell input text "Text_%s_tut"
# swipe the page
#time.sleep(5)
#os.system("adb shell input tap 340 1030 340 650 100")
# press back key
#os.system("adb shell input keyevent 4")