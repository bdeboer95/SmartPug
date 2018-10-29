#!/usr/bin/python
import time
import pigpio 

pi = pigpio.pi()

def shutdown():
    pigpio.stop()

def init():
        	#pi = pigpio.pi() # Connect to local Pi.
    
        for g in range(0,32):
            print("gpio {} is {}".format(g, pi.read(g)))
            
        pi.set_mode(17, pigpio.OUTPUT)
        print("mode:", pi.get_mode(17));
        print("Initialized servo on GPIO17")
      

def sweep():
	pi.set_servo_pulsewidth(17, 500)
	time.sleep(.05)
	pi.set_servo_pulsewidth(17, 1500)
	time.sleep(.5)
	pi.set_servo_pulsewidth(17, 500)
	time.sleep(.05)
	pi.set_servo_pulsewidth(17, 1500)
	time.sleep(.5)

	# switch servo off
	pi.set_servo_pulsewidth(17, 0);

def sweepfast():
    for x in range(6):
        pi.set_servo_pulsewidth(17, 500)
        time.sleep(.05)
        

    pi.set_servo_pulsewidth(17, 0)
