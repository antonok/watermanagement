import sys, thread, time, datetime

class FlowCounter:

    def __init__(self, countFactor, flushMs): 

        if flushMs != None:
            self.flushMs = flushMs
        else:
            self.flushMs = 500

        self.countFactor = countFactor

        self.startTs = 0
        self.lastTs = 0
        self.count = 0

        def flusher():
            while True:
                time.sleep(self.flushMs / 100)
                self.doFlush()


        thread.start_new_thread(flusher, ())

    def countPulse(self):
        now = self.nowMs()
        if self.startTs == 0:
            self.startTs = now
        self.lastTs = now 
        self.count += 1


    def doFlush(self):

        if self.count > 0 and (self.nowMs() - self.lastTs > self.flushMs):
            flowTime = self.lastTs - self.startTs
            flowStart = datetime.datetime.fromtimestamp(self.startTs/1000.0)
            print '%s count: %d, timeMs: %d' % (flowStart, self.count, flowTime)
            self.count = 0
            self.startTs = 0
            self.lastTs = 0

    def nowMs(self):
        return int(round(time.time() * 1000))



if __name__ == "__main__":
    sys.exit(1)
