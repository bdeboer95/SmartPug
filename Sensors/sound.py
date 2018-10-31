#!/usr/bin/python
import grovepi
import settings
# ====== VARIABLES ====== #
# Left / Right sound sensor
# = A1 / A2

#pin_right = 2

# Sensor values
direction = "cant see you"

# ====== FUNCTIONS ====== #
def init():
    if(settings.sound_sensor):
	grovepi.pinMode(settings.sound_sensor, "INPUT")
        return 1
    else:
        return 0
    print("Initialized sound sensors on A1")

def getDirection():
	return str(direction)

# Based on "abstract" value
# - right +/- 240 
# - left ranges from 60 to 300 
def detectSoundLevel():
	# Read sensors
	level  = grovepi.analogRead(settings.sound_sensor)
        print(level)
        return level
    

	
