#!/bin/bash
set -e
 
echo "Installing python and pip"
 
sudo dnf install python3 -y
 
python3 -m ensurepip --upgrade || true
 
python3 -m pip install --upgrade pip
 
echo "Installing project dependencies"
 
cd /home/ec2-user/app
 
pip3 install -r requirements.txt || true
