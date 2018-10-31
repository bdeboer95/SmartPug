#!/usr/bin/python
import grovepi
from Servo import servo_pig 
# ====== VARIABLES ====== #
# Gas (MQ2) sensor 
# = A0
# - Combustable Gas
# - Smoke
pin = 0

# Sensor values
value = 0

# ====== FUNCTIONS ====== #
def init():
	grovepi.pinMode(pin, "INPUT")
	print ("Initialized gas sensor on A0")
        return 1
# Calculates gas density. Large values = more dense gas 
# - defaults at 270
def inDanger():
	# Read sensor
	value = grovepi.analogRead(pin)
        print value
	# Calculate
	density = (float)(value / 1024)
	if(value >400):
            print value
            return True
        else:
            return False
	
	
	
