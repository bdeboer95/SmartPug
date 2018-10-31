#!/usr/bin/python
import time
import pigpio 
import os
sudoPassword='root'
command='pigpiod'
os.popen("sudo -S %s"%( command), 'w').write(sudoPassword)
pi = pigpio.pi()

pin=18
def shutdown():
    pi.set_servo_pulsewidth(pin,0)
    

def init():
        #Initialize pigpiod in commandline to setup pigpiod.
        
        print("initialized pigpiod")
    
        pi.set_mode(pin, pigpio.OUTPUT)
        #Read out the status of the GPIO pins
        print("mode:", pi.get_mode(pin));
        print("Initialized servo on GPIO18")
        print(pi)
   #pulse width between 0 or 500-2500

def sweep(delay, repeat):
    print("Sweeping")
    for x in range(repeat):
        pi.set_servo_pulsewidth(pin, 500)
        time.sleep(delay)
        pi.set_servo_pulsewidth(pin, 2500)
        time.sleep(delay)
        
    shutdown()
	
	
	#pi.set_servo_pulsewidth(pin, 0);

def sweepfast():
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 2500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 500)
    time.sleep(.1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(.1)
        
init()
time.sleep(0.5)
sweep(0.1, 8)

#sweepfast()
