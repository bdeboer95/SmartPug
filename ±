from Sensors import motion  
from Sensors import sound
from Messaging import gmail
from Sensors import touch
from Sensors import gas
from Servo import servo_pig
from Camera import camera
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
hearing=False
touchable= False
sensesMotion=False
gasable=False
# ====== FUNCTIONS ====== #
def init():
    
    global sensesMotion
    global touchable
    global hearing
    global cooldown
    global gasable

    sensesMotion=motion.init()
    hearing=sound.init()
    hearing=False;
    camera.init()
    gasable=gas.init()
    if gasable:
        print("Gasable")
    touchable=touch.init()
    print(touchable)
    servo_pig.init()
    #servo_pig.sweep()
    print("===============")
    time.sleep(2)

# ======== MAIN ========= #
init()

while True:
        try:
            if touchable:
                if touch.isTouched():
                    print("Touched")
                    servo_pig.sweep(0.1, 5)
            elif sensesMotion:
                if not detected:
                    if motion.inRange():
                        print("Motion Sensed")
                        servo_pig.sweep(0.2, 5)
                        fileName=camera.takePicture()
                        subject="Danger: Smart Pug has detected a burglar"
                        message="The Smart Pug has detected an unusual presence inside this room. A weird person is present in here. Please call the police immediately or ask if your loved one is OK!"
                        gmail.sendemail(subject, message, [fileName])
                        detected=True
            if gasable:
                if not tired:
                    if gas.inDanger():
                        servo_pig.sweep(0.01,100)
                        print("in Danger:")
                        subject="Danger: Smart Pug has detected a burglar"
                        #subject='DANGER: Smart pug has detected smoke/gas nearby'
                        message="The Smart Pug has detected an unusual presence inside this room. A weird person is present in here. Please call the police immediately or ask if your loved one is OK!"
                        #message="   Danger : Abnormal levels of smoke /gas detected!!! Please contact your loved one as soon as possible and ask if they're okay! Feel free to take a visit!"
                        fileName=camera.takePicture()
                        gmail.sendemail(subject, message, [fileName])
                        tired=True

                    
    
                            #servo_pig.sweepfast()
                # Once it has barked it will wait 100 ticks before it can bark again
            if not tired:
                if hearing:
                    soundlevel=sound.detectSoundLevel()
                    if soundlevel>settings.human_sound_level and soundlevel < settings.danger_sound_level:
                        servo_pig.sweep(0.1, 6)
                    elif sound.detectSoundLevel()>settings.danger_sound_level:
                        print("Danger sound level: Email has been sent")
                        message='Dangerous Sound Level above '+soundlevel
                        subject='Smart pug Sound detection'
                        gmail.sendemail(sender=settings.login,recipients=settings.recipients,cc_recipients=settings.cc_recipients,subject=subject,msg=message,login=settings.login,password=settings.password)
                        tired=True
                    
            else:
                if cooldown > 0:
                    cooldown -= 1
                else:
                    cooldown = 45
                    tired = False

            time.sleep(0.1)
        except IOError:
            print("Error")
                # Always check for gas :)
		#if gas.inDanger():
			# todo: make more userfriendly
			#print "Run mothafucka run" 

		# Delay to prevent sensor information overload
                    
                    
print("Shutdown")
servo_pig.shutdown()
