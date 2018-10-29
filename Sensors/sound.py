#!/usr/bin/python
import grovepi

# ====== VARIABLES ====== #
# Left / Right sound sensor
# = A1 / A2
pin_left = 1
#pin_right = 2

# Sensor values
direction = "cant see you"

# ====== FUNCTIONS ====== #
def init():
	grovepi.pinMode(pin_left, "INPUT")
	#grovepi.pinMode(pin_right, "INPUT")
	print("Initialized sound sensors on A1")

def getDirection():
	return str(direction)

# Based on "abstract" value
# - right +/- 240 
# - left ranges from 60 to 300 
def detectSoundLevel(sound_level):
	# Read sensors
	left = grovepi.analogRead(pin_left)
	#right = grovepi.analogRead(pin_right)

        

	# Determine direction
	#margin = 5

	#if left > right:
		#direction = "left"
	#elif right > left:
		#direction = "right"
	#elif (left - right + margin) > 0:
		#direction = "front"

	if left > sound_level:
		return True

	return False 
