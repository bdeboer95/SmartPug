#!/usr/bin/python
import grovepi
import settings
# ====== VARIABLES ====== #
# PIR sensor
# = D3
pin = settings.motion_sensor

# Sensor values
value = 0

# ====== FUNCTIONS ====== #
def init():
    if(pin):
	grovepi.pinMode(pin, "INPUT")
	print("Initialized motion sensor on D3")
        return 1
    else:
        return 0

# Detects the user. Can be adjusted via pot I think :)
# - no detection every few ticks or so
def inRange():
	return True if grovepi.digitalRead(pin) is 1 else False
