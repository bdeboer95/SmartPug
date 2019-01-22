#!/usr/bin/python
import grovepi, time

# ====== VARIABLES ====== #
# PIR sensor
# = D3
pin = 3

# Sensor values
value = 0

# ====== FUNCTIONS ====== #
def init():
	grovepi.pinMode(pin, "INPUT")
	print("Initialized motion sensor on D3")

# Detects the user. Can be adjusted via pot I think :)
# - no detection every few ticks or so
def inRange():
	return True if grovepi.digitalRead(pin) is 1 else False
