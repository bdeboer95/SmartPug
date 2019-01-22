import time, settings, os, datetime, grovepi
from Sensors import motion, sound, touch, accel
from SensorData.sensornames import SensorNames
import subprocess

from Messaging import gmail
from Logger.logger import Logger

class TeddyBear:
    def __init__(self):
        #100 ticks = (100*0.1) = 10 secs
        self.cooldownMotionMin = 0
        self.cooldownMotionMax = 500
        
        self.cooldownAccelMin = 0
        self.cooldownAccelMax = 500
        
        self.cooldownSoundMin = 0
        self.cooldownSoundMax = 500
        
        self.cooldownBarkMin = 0
        self.cooldownBarkMax = 50
        
        self.tapDetected    = False
        self.motionDetected = False
        self.soundHighVal = 0
        
        self.barking = False
        self.processSound = None
        
        
        sound.init()
        accel.init()
        motion.init()
        
        self.soundLogger  = Logger(SensorNames.SOUND)
        self.motionLogger = Logger(SensorNames.MOTION)
        self.accelLogger  = Logger(SensorNames.ACCELEROMETER)
        
        time.sleep(2)
        
    
    def bark(self):
        self.processSound = subprocess.Popen(["aplay /home/pi/Desktop/smartteddy/bark3.wav"], shell=True)
        
        
    def monitor(self):
        while True:
            try:
                if not self.motionDetected and self.cooldownMotionMin == 0:
                   if motion.inRange():
                       self.motionLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), 1))
                       self.motionDetected = True
                       self.cooldownMotionMin = self.cooldownMotionMax
                       
                isTapped = True if accel.isTapped() else False
                if not self.tapDetected and self.cooldownAccelMin == 0:
                   if isTapped:
                       self.accelLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), 2))
                       self.tapDetected = True
                       self.cooldownAccelMin = self.cooldownAccelMax
                       
                       
                if isTapped:
                    self.cooldownBarkMin = self.cooldownBarkMax
                    
                if self.soundHighVal == 0:
                     self.cooldownSoundMin = self.cooldownSoundMax
                
                tmpSoundLevel = sound.getSoundLevel()
                tmpSoundLevel = 2000 if tmpSoundLevel > 1200 else tmpSoundLevel
                if self.soundHighVal < tmpSoundLevel:
                    self.soundHighVal = tmpSoundLevel
                
                if self.motionDetected and self.cooldownMotionMin >= 0 and self.cooldownMotionMin <= self.cooldownMotionMax:
                    self.cooldownMotionMin = self.cooldownMotionMin - 1
                    if self.cooldownMotionMin == 0:
                        self.motionDetected = False
                        
                if self.tapDetected and self.cooldownAccelMin >= 0 and self.cooldownAccelMin <= self.cooldownAccelMax:
                    
                    if self.processSound != None and self.barking == True:
                        self.processSound.terminate()
                        self.barking = False
                        
                    self.cooldownAccelMin = self.cooldownAccelMin - 1
                    if self.cooldownAccelMin == 0:
                        self.tapDetected = False
                
                if self.cooldownBarkMin >= 0 and self.cooldownBarkMin <= self.cooldownBarkMax:
                    self.cooldownBarkMin = self.cooldownBarkMin - 1
                    print self.cooldownBarkMin
                    if self.cooldownBarkMin > 0:
                        if tmpSoundLevel > 700:
                            self.barking = True
                            self.bark()
                            time.sleep(1)
                        
                        
                if self.cooldownSoundMin >= 0 and self.cooldownSoundMin <= self.cooldownSoundMax:
                    self.cooldownSoundMin = self.cooldownSoundMin - 1
                    if self.cooldownSoundMin == 0:
                        self.soundLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), self.soundHighVal))
                        self.soundHighVal = 0

            except IOError:
                print("Error")
                
            
            time.sleep(0.1)
        

if __name__ == '__main__':
    objTeddyBear = TeddyBear()
    objTeddyBear.monitor()
