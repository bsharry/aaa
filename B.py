#""""""""""""""""""""""""""""""""""""""""""""""""""
#	copyright @blader 2016 all right reserverd	   
#""""""""""""""""""""""""""""""""""""""""""""""""""

import bluetooth
import sys
import json
import RPi.GPIO as GPIO
import os.path
led_pin=25
version=None
def find_Devices():
	"""find the bluetooth device"""
	devices=bluetooth.discover_devices(lookup_names=True)		#need to be correct
	return devices  							# to list the name

def check_Devices():
	"""check whether this program has been correctly runned"""
	if not os.path.isfile("device.json"):
		return False
	file=open("device.json")
	data=json.load(file)
	if 'address' in data:
		file.close()
		return data['address']
	else:
		file.close()
		return False

def python_Version_Check():
	"""check for python version"""
	global version
	version=sys.version
	print(version)

def address_Save(address):
	"""save the bluetooth address"""
	file=open("device.json","w")
	data=dict()
	data['address']=address
	json.dump(data,file)
	file.close()

def choose_address(devices):
	print("please choose the devices[enter the number please]")
	i=0
	for address,name in devices:
		L="[%d] %s %s"%(i,address,name)
		print(L)
		i+=1
	if version[0] is 2:
		number=input()
	else:
		number=int(input())
	return devices[number][0]

def connect(address):
	port=1
	socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	socket.connect((address,port))
	socket.recv(1)

if __name__=="__main__":
	device=check_Devices()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin,GPIO.OUT)
	if not device:
		python_Version_Check()
		devices=find_Devices()
		print(devices)
		device=choose_address(devices)
	address_Save(device)
	while True:
		try:
			connect(device)
		except Exception as e:
			signal=e[0]
			if not signal is 112:
				print(signal)
				print("detected bluetooth")
				GPIO.output(led_pin,GPIO.LOW)
			else:	
				print(signal)
				print("error:not detect")
				GPIO.output(led_pin,GPIO.HIGH)
