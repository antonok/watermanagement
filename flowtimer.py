#!/usr/bin/env python


import sys
import atexit

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

def cleanup():
    print 'ok, I will clean up gpio now'
    GPIO.cleanup()

atexit.register(cleanup)


def main():
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    main()
