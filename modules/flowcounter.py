import sys, thread, time, datetime, os, atexit
import RPi.GPIO as GPIO

import logging


FLOW_SENSOR = 23


class FlowCounter:


    def __init__(self, countFactor, flushMs): 

        self.logger = logging.getLogger()
        self.logger.info('countFactor: %f' % countFactor)
        self.logger.info('flush miliseconds: %d' % flushMs)
        self.flushMs = 500
        if flushMs != None:
            self.flushMs = flushMs

        self.countFactor = countFactor

        self.startTs = 0
        self.lastTs = 0
        self.count = 0

        self.initGPIO()

        def flusher():
            while True:
                time.sleep(self.flushMs / 100)
                self.doFlush()
            
        thread.start_new_thread(flusher, ())

    def initGPIO(self):
        self.logger.info('initializing gpio')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=self.countPulse)
        atexit.register(self.cleanup)

    def cleanup(self):
        GPIO.cleanup()

    def countPulse(self, arg):
        now = self.nowMs()
        if self.startTs == 0:
            self.startTs = now
        self.lastTs = now 
        self.count += 1


    def doFlush(self):

        deltaMs = self.nowMs() - self.lastTs


        if self.count > 0 and (deltaMs > self.flushMs):
            flowTime = self.lastTs - self.startTs
            flowStart = datetime.datetime.fromtimestamp(self.startTs/1000.0)

            volume = self.count * self.countFactor

            msg = '%s count: %d, vol: %f, timeMs: %d' % (flowStart, self.count, volume, flowTime)
            print msg
            self.logToFile(msg)
            self.count = 0
            self.startTs = 0
            self.lastTs = 0

    def logToFile(self, msg):
        filepath = '/tmp/flowd/log.txt'
        dirpath = os.path.dirname(filepath)

        if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
            os.makedirs(dirpath)
        f = open(filepath, 'a')
        f.write(msg + "\n")
        f.close()

    def nowMs(self):
        return int(round(time.time() * 1000))



if __name__ == "__main__":
    sys.exit(1)
