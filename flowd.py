#!/usr/bin/env python

import os, time
from datetime import datetime
from daemon import runner
from flowtimer import *

class FlowD():


    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/var/log/flowd_stdout.log'
        self.stderr_path = '/var/log/flowd_stderr.log'
        self.pidfile_path = '/var/run/flowd.pid'
        self.pidfile_timeout = 5

    def run(self):

        print '%s flowd started' % datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        
        while True:
            print '%s flowd is running' % datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            time.sleep(5)


app = FlowD()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
