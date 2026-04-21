#!/bin/bash
cd /home/ec2-user/app
sudo pkill -f "python3 app.py" || true
sudo nohup python3 app.py > /tmp/app.log 2>&1 &
 
