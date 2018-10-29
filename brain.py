from Sensors import motion  
from Sensors import sound
from Sensors import touch
from Messaging import gmail
#from Sensors import gas
from Servo import servo_pig
import time
import settings

# ====== VARIABLES ====== #
# Cooldown for animations
cooldown = 25
tired = False

# Cooldown for motion detecting
cooldownInit = 500
detected = False

# ====== FUNCTIONS ====== #
def init():
    print("===============")
    motion.init()
    sound.init()
	#gas.init()
	#touch.init()
    servo_pig.init()
    servo_pig.sweep()
    #servo_pig.sweep()
    print("===============")
    time.sleep(2)

# ======== MAIN ========= #
init()

while True:
        try:
            
                # Once detected it goes on a 500 ticks cooldown
                if touch.isTouched:
                    servo_pig.sweepfast()
                if not detected:
                        if motion.inRange():
                                detected = True
                                cooldownDetected = 500
                else:
                        print("Motion detected")
                        servo_pig.sweepfast()

                        if cooldownDetected > 0:
                                cooldownDetected -= 1
                        else:
                                detected = False
                                #if it detects sound from his human
                if sound.detectSoundLevel(settings.human_sound_level):
                            servo_pig.sweepfast()
                # Once it has barked it will wait 100 ticks before it can bark again
                if not tired:
                        if sound.detectSoundLevel(settings.danger_sound_level):
                            print("Danger sound level: Email has been sent")
                            servo_pig.sweepfast()
                            message='Dangerous Sound Level'
                            subject='Smart pug Sound detection'
                            gmail.sendemail(sender=settings.login,recipients=settings.recipients,cc_recipients=settings.cc_recipients,subject=subject,msg=message,login=settings.login,password=settings.password)
                            tired=True
                        
       
 
		        # TODO
			#if canFeel():
			        #print "Am I good boy?"

                else:
                        if cooldown > 0:
                                cooldown -= 1
                        else:
                                cooldown = 25
                                tired = False

                print(detected)
                time.sleep(.1)
        except IOError:
            print("Error")
                # Always check for gas :)
		#if gas.inDanger():
			# todo: make more userfriendly
			#print "Run mothafucka run" 

		# Delay to prevent sensor information overload
                    
                    
            servo_pig.shutdown()
