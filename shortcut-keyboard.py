#!/bin/python
import os
import time
import evdev
from evdev import InputDevice, categorize, ecodes
import xml.etree.ElementTree as XML

#Loading conf XML
tree = XML.parse('shortcut.conf.xml')
root = tree.getroot()
conf = root[0]
keyboardname = root[1].text
keybindings = {}
for a in conf:
     tmp = {a[1].text : a[0].text}
     keybindings.update(tmp)

#get keyboard
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devlist = []
for device in devices:
	devlist.append(device.fn + " " + device.name + " " + device.phys)
event = 0
devid = []
for dev in devlist:
	if keyboardname in dev:
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
		keys = device.active_keys(verbose=True)
		if(len(keys) > 0):
			keypress = keys[0]
			print(keypress)
			key = keypress[0]
			print(key)
			if(keybindings[key] == "set Command"):
				continue
			os.system(keybindings[key])
		time.sleep(0.25)
