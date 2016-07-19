#!/bin/python
import os
import time
import evdev
from evdev import InputDevice, categorize, ecodes

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devlist = []
for device in devices:
	devlist.append(device.fn + " " + device.name + " " + device.phys)
event = 0
devid = []
for dev in devlist:
	if "Logitech USB Keyboard" in dev:
		devid.append("")
		for char in dev:
			event = len(devid) - 1
			if char.isdigit():
				devid[event] = devid[event] + "" + char
			elif char.isalpha():
				if devid[event].isdigit():
					print(devid[event])
					break

if len(devid) < 2:
	quit("Keyboard not fund")
if devid[0] < devid[1]:
	deviceid = devid[0]
else:
	deviceid = devid[1]
deviceid = '/dev/input/event' + deviceid
device = evdev.InputDevice(deviceid)
device.grab()
print(deviceid)
while 1:
	if 1 == 1:
		keys = device.active_keys(verbose=True)
		if "KEY_KP0" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 1.0" )
		if "KEY_KP1" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.10" )
		if "KEY_KP2" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.20" )
		if "KEY_KP3" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.30" )
		if "KEY_KP4" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.40" )
		if "KEY_KP5" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.50" )
		if "KEY_KP6" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.60" )
		if "KEY_KP7" in str(device.active_keys(verbose=True)):
			os.system("transset-df 0.70" )
		if "KEY_KP8" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.80" )
		if "KEY_KP9" in str(device.active_keys(verbose=True)):
			print(device.active_keys(verbose=True))
			os.system("transset-df 0.90" )
		time.sleep(0.25)
