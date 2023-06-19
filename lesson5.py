#!usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

blue=GPIO.PWM(17,75)
green=GPIO.PWM(27,75)
red=GPIO.PWM(22,75)
i=45
o=33

try:

 while (True):
    
     red.start(i)
     blue.start(i)
     sleep(0.5)
     red.stop()
     blue.stop()
     sleep(0.5)

     red.start(i)
     green.start(o)
     sleep(0.5)
     red.stop()
     green.stop()
     sleep(0.5)

     green.start(i)
     blue.start(o)
     sleep(0.5)
     green.stop()
     blue.stop()
     sleep(0.5)
except KeyboardInterrupt:
      blue.stop()
      red.stop()
      green.stop()   
      GPIO.cleanup()
      print("應用程式結束")


