#!/usr/bin/python
import servo_pig
import time

servo_pig.init()

while True:
    try:
        servo_pig.sweepfast()
        time.sleep(.05)
    except IOError:
        print "something is wrong"
