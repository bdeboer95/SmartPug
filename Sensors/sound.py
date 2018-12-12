#!/usr/bin/python
import grovepi

# ====== VARIABLES ====== #
# Left / Right sound sensor
# = A1 / A2
pin_left = 1

# Sensor values
direction = "cant see you"

# ====== FUNCTIONS ====== #
def init():
	grovepi.pinMode(pin_left, "INPUT")
	#grovepi.pinMode(pin_right, "INPUT")
	print("Initialized sound sensors on A1")

def getDirection():
	return str(direction)

def getSoundLevel():
	# Read sensors
	return grovepi.analogRead(pin_left)
