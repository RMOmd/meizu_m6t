import os
import time

os.system("adb shell input tap 340 1030")
# swipe the page
time.sleep(5)
os.system("adb shell input tap 340 1030 340 650 100")
# press back key
os.system("adb shell input keyevent 4")