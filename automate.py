import os
import time

os.system("adb devices")
time.sleep(3)
device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
# connect to the selected device 127.0.0.1:62001
print("Waiting for connection ...")
connect = os.popen("adb connect " + device ).read()
print(connect)
#os.system("adb shell input tap 442 980")
#time.sleep(3)
#os.system("adb shell input tap 130 1232 130 190 100")
#time.sleep(3)
#os.system("adb shell input tap 143 1086")
#time.sleep(3)
#os.system("adb shell input tap 162 205")
#time.sleep(3)
#os.system("adb shell input tap 131 593")
#time.sleep(3)
# swipe the page
#time.sleep(5)
#os.system("adb shell input tap 340 1030 340 650 100")
# press back key
#os.system("adb shell input keyevent 4")