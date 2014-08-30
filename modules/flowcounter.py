import sys, thread, time, datetime, os

class FlowCounter:

    def __init__(self, countFactor, flushMs): 

        #self.flushMs = 500
        if flushMs != None:
            self.flushMs = flushMs
        else:
            self.flushMs = 500

        self.countFactor = countFactor

        self.startTs = 0
        self.lastTs = 0
        self.count = 0
        print 'self.flushMs', self.flushMs

        def flusher():
            self.logToFile('this is flusher method' + str(self.flushMs))
            while True:
                self.logToFile('flusher will sleep for asdasd %d' % (self.flushMs/100))
                #time.sleep(self.flushMs / 100)
                self.logToFile('flusher')
                self.doFlush()
            self.logToFile('this is flusher method end')
            

        thread.start_new_thread(flusher, ())

    def countPulse(self):
        now = self.nowMs()
        if self.startTs == 0:
            self.startTs = now
        self.lastTs = now 
        self.count += 1
        print 'count pulse ' + str(self.count)


    def doFlush(self):

        deltaMs = self.nowMs() - self.lastTs

        self.logToFile('this is doFlush self.count: %d self.nowMs(): %d self.lastTs %d self.flushMs: %d' %(self.count, self.nowMs(), self.lastTs, -9) )
	self.logToFile('delta ts' )

        if self.count > 0 and ((nowMs - self.lastTs) > self.flushMs):
            self.logToFile('hello inside the if!')
            flowTime = self.lastTs - self.startTs
            flowStart = datetime.datetime.fromtimestamp(self.startTs/1000.0)

            msg = '%s count: %d, timeMs: %d' % (flowStart, self.count, flowTime)
            print msg
            self.logToFile(msg)
            self.count = 0
            self.startTs = 0
            self.lastTs = 0
        self.logToFile('end of doFlush')

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
