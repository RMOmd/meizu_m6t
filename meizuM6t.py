# Скрипт для настройки VoLTE на Meizu M6t под IDC
import subprocess

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
