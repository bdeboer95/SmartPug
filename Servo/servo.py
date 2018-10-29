#!/usr/bin/python
import wiringpi
import time

# ====== VARIABLES ====== #
delay_period = 0.01

# ====== FUNCTIONS ====== #
# Set pins to PWM mode and set frequency
# - https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software
def init():
	# use 'GPIO naming'
	wiringpi.wiringPiSetupGpio()
 
	# set #18 to be a PWM output
	wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 
	# set the PWM mode to milliseconds stype
	wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
	# divide down clock
	wiringpi.pwmSetClock(192)
	wiringpi.pwmSetRange(2000)
	print "Initialized servo at 18 in PWM mode"

def sweep():
	print "Bark bark!"

	# Rotate cw
	for pulse in range(50, 250, 1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)

    # Rotate ccw
	for pulse in range(250, 50, -1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)

