import os
import sys
import time

from datetime import datetime
from daemon import runner
import logging

sys.path.append("modules")
from flowcounter import FlowCounter

#import flowtimer


class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/var/log/flowd_stdout.log'
        self.stderr_path = '/var/log/flowd_stderr.log'
        self.pidfile_path = '/var/run/flowd.pid'
        self.pidfile_timeout = 5

    def run(self):
        logger.info("start run()")

        self.fc = FlowCounter(float (1) / 450, 200)

        while True:
            #do a heartbeat or something to indicate that we are still alive
            #logger.info('via logger '+ datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
            time.sleep(1)

        logger.info("end run()")


app = App()


#logger = logging.getLogger("DaemonLog")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
