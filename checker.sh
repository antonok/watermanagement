#!/bin/bash


start() {
   echo "starting flowd.py"
   python /home/pi/watermanagement/flowd.py start

   echo "started flowd.py"
}

if [ ! -e /var/run/flowd.pid ]
then
   echo "pid file doesn't exist!"
   start;
else
   pid=`cat /var/run/flowd.pid`
   stillup=`ps --no-headers -p $pid`
   if [[ ! $stillup ]]
   then
      echo "process has died, starting"
      start
   else
      echo "process $pid is up"
   fi
fi
