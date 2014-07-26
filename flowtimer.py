#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys


FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global count
count = 0

global lastTs, previousTs, timeDelta
lastTs = 0
previousTs = 0
timeDelta = 0


currentMs = lambda: int(round(time.time() * 1000))


def countPulse(channel):
    global count, lastTs, previousTs, timeDelta
    now = currentMs()

    # last recorded timestamp is part of the current water flow
    if now - lastTs < 1000:
        #update delta with difference between previous and last
        if previousTs > 0:
            timeDelta = timeDelta + (lastTs - previousTs)
        previousTs = lastTs
        lastTs = now   
    else:
        #this looks like a new run
        print 'last run lasted %d ms.' % timeDelta
        timeDelta = 0
        previousTs = 0
        lastTs = now

    count = count+1
    #print count

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
