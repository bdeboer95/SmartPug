#!/bin/sh
# launcher.sh
# navigate to home, then this directory, then execeute scripts then back home

cd / 
cd home/pi/Desktop/Smart\ Pug/Servo/PIGPIO/
sudo pigpiod
cd ..
cd ..
sudo python brain.py
cd /
