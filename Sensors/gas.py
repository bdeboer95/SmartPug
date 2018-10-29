#!/usr/bin/python
import grovepi

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
	print "Initialized gas sensor on A0"

# Calculates gas density. Large values = more dense gas 
# - defaults at 270
def inDanger():
	# Read sensor
	value = grovepi.analogRead(pin)

	# Calculate
	density = (float)(value / 1024)
	print('sensor_value = ', value, ' density = ', density)
	return 0
