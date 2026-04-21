#!/bin/bash
set -e
 
echo "Updating system"
sudo dnf update -y
 
echo "Installing python"
sudo dnf install python3 python3-pip -y
 
echo "Installing pip properly"
python3 -m ensurepip --upgrade || true
 
echo "Upgrade pip"
sudo python3 -m pip install --upgrade pip
 
echo "Go to app directory"
cd /home/ec2-user/app
 
echo "Installing requirements"
sudo python3 -m pip install -r requirements.txt
 
echo "Dependencies installed successfully"
 
