#!/usr/bin/env python
 
import RPi.GPIO as GPIO, time
 
DEBUG = 1
SLEEP_TIME = 2
 
GPIO.setmode(GPIO.BCM)
RED_LED = 31
GPIO.setup(RED_LED, GPIO.OUT)
#GREEN_LED = 23
#GPIO.setup(GREEN_LED, GPIO.OUT)
 
while True:
    GPIO.output(RED_LED, True)
    time.sleep(SLEEP_TIME)
    GPIO.output(RED_LED, False)
    time.sleep(SLEEP_TIME)
