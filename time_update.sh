#!/bin/bash

date_start=`date|awk -F"[ :]" '{print $4*3600 + $5*60 +$6}'`
/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/bin/python3.6 UpdateNodesInfoTests.py
date_end=`date|awk -F"[ :]" '{print $4*3600 + $5*60 +$6}'`
time=`expr "$date_end" - "$date_start"`
echo "your command will take $time seconds" > result_time.txt