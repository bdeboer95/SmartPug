#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
export DISPLAY=:0.0
killall python
sleep 5
sudo python /home/pi/Desktop/smartteddy/send_email.py
