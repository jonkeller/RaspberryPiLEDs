#!/usr/bin/env python
 
import RPi.GPIO as GPIO, time
import sys
 
GPIO.setmode(GPIO.BCM)
pin = int(sys.argv[1])
print "Pin:", pin
GPIO.setup(pin, GPIO.OUT)
SLEEP_TIME = 3 
while True:
    print "On"
    GPIO.output(pin, True)
    time.sleep(SLEEP_TIME)
    print "Off"
    GPIO.output(pin, False)
    time.sleep(SLEEP_TIME)
