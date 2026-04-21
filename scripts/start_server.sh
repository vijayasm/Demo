#!/bin/bash
 
cd /home/ec2-user
 
# stop existing app if running
pkill -f app.py || true
 
# start new app in background
nohup python3 app.py > app.log 2>&1 &
