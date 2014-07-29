#!/usr/bin/env python


import sys
sys.path.append("modules")

import RPi.GPIO as GPIO
import time 

from flowcounter import FlowCounter 


FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

fc = FlowCounter(0.45, 200)

def countPulse(channel):
    fc.countPulse()

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
