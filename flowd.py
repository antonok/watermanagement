import os
import time

from datetime import datetime
from daemon import runner


import logging


class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/var/log/flowd_stdout.log'
        self.stderr_path = '/var/log/flowd_stderr.log'
        self.pidfile_path = '/var/run/flowd.pid'
        self.pidfile_timeout = 5

    def run(self):
        logger.info("start run()")
        filepath = '/tmp/mydaemon/currenttime.txt'
        dirpath = os.path.dirname(filepath)
        while True:
            if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
                os.makedirs(dirpath)
            f = open(filepath, 'a')
            f.write(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S') + "\n")
            print datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

            logger.info(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
            f.close()
            time.sleep(1)

        logger.info("end run()")


app = App()


logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
