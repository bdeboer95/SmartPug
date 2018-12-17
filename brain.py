import time, settings, os, datetime, grovepi
from Sensors import motion, sound, touch, accel
from SensorData.sensornames import SensorNames

from Messaging import gmail
from Logger.logger import Logger

class TeddyBear:
    def __init__(self):
        #100 ticks = (100*0.1) = 10 secs
        self.cooldownMotionMin = 0
        self.cooldownMotionMax = 590
        
        self.cooldownAccelMin = 0
        self.cooldownAccelMax = 590
        
        self.cooldownSoundMin = 0
        self.cooldownSoundMax = 590
        
        self.tapDetected    = False
        self.motionDetected = False
        self.soundHighVal = 0
        
        sound.init()
        accel.init()
        motion.init()
        
        self.soundLogger  = Logger(SensorNames.SOUND)
        self.motionLogger = Logger(SensorNames.MOTION)
        self.accelLogger  = Logger(SensorNames.ACCELEROMETER)
        
        time.sleep(2) 
        
    def monitor(self):
        while True:
            try:
                if not self.motionDetected and self.cooldownMotionMin == 0:
                   if motion.inRange():
                       self.motionLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), 1))
                       self.motionDetected = True
                       self.cooldownMotionMin = self.cooldownMotionMax
                       
                if not self.tapDetected and self.cooldownAccelMin == 0:
                   if accel.isTapped():
                       self.accelLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), 2))
                       self.tapDetected = True
                       self.cooldownAccelMin = self.cooldownAccelMax
                       
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
                    self.cooldownAccelMin = self.cooldownAccelMin - 1
                    if self.cooldownAccelMin == 0:
                        self.tapDetected = False
                        
            
                if self.cooldownSoundMin >= 0 and self.cooldownSoundMin <= self.cooldownSoundMax:
                    print "CD {}".format(self.cooldownSoundMin)
                    self.cooldownSoundMin = self.cooldownSoundMin - 1
                    if self.cooldownSoundMin == 0:
                        print "logging"
                        self.soundLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), self.soundHighVal))
                        self.soundHighVal = 0

            except IOError:
                print("Error")
                
            
            time.sleep(0.1)
        

if __name__ == '__main__':
    objTeddyBear = TeddyBear()
    objTeddyBear.monitor()
