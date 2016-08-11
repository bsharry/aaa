import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
print("high")
gpio.output(15,True)
time.sleep(10)
print("low")
gpio.output(15,False)
time.sleep(10)
gpio.cleanup()
