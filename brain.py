from Sensors import motion  
from Sensors import sound
from Messaging import gmail
from Sensors import touch
from Logger.logger import Logger
from SensorData.sensornames import SensorNames
#from Sensors import gas
from Servo import servo_pig
import time
import settings
import os


# ====== VARIABLES ====== #


# Cooldown for animations
cooldown = 25
tired = False

# Cooldown for motion detecting
cooldownInit = 500
detected = False

# ====== FUNCTIONS ====== #
def init():
    motion.init()
    sound.init()
	#gas.init()
	#touch.init()

    #Write to Log
    #logger.log(SensorNames.TOUCH, 1)
    servo_pig.init()
    servo_pig.sweep(0.4, 4)
    #servo_pig.sweep()
    print("===============")
    time.sleep(2)

#define loggers    
def initLoggers():
    motionLogger=Logger(SensorNames.MOTION)
    soundLogger= Logger(SensorNames.SOUND)
    gasLogger = Logger(SensorNames.GAS)
    accelLogger = Logger(SensorNames.ACCELEROMETER)


#======== MAIN ========= #
init()

while True:
        try:
            
                # Once detected it goes on a 500 ticks cooldown
                if touch.isTouched():
                    #logger.log("Touch", 
                    print("Touched")
                    #servo_pig.sweepfast()
                if not detected:
                       if motion.inRange():
                           print("Motion detected")
                           detected = True
                           cooldownDetected = 500
                           servo_pig.sweep(0.4, 4)
                else:
                    if touch.isTouched():
                        print("touched")

                time.sleep(0.1)
                     #   servo_pig.sweepfast(0,1, 5)
#                      if cooldownDetected > 0:
  #                              cooldownDetected -= 1
   #                     else:
     #                           detected = False
    #                            #if it detects sound from his human
                #if sound.detectSoundLevel(settings.human_sound_level):
                      #      servo_pig.sweepfast()
                # Once it has barked it will wait 100 ticks before it can bark again
                #if not tired:
                   #     if sound.detectSoundLevel(settings.danger_sound_level):
                    #        print("Danger sound level: Email has been sent")
                       #     servo_pig.sweepfast()
                     #       message='Dangerous Sound Level'
                      #      subject='Smart pug Sound detection'
                            #gmail.sendemail(sender=settings.login,recipients=settings.recipients,cc_recipients=settings.cc_recipients,subject=subject,msg=message,login=settings.login,password=settings.password)
                       #     tired=True
                        
       
 
		        # TODO
			#if canFeel():
			        #print "Am I good boy?"

               # else:
                ##        if cooldown > 0:
                #                cooldown -= 1
                 #       else:
                  #              cooldown = 25
                   #             tired = False

        except IOError:
            print("Error")
                # Always check for gas :)
		#if gas.inDanger():
			# todo: make more userfriendly
			#print "Run mothafucka run" 

		# Delay to prevent sensor information overload
                    
                    
servo_pig.shutdown()
