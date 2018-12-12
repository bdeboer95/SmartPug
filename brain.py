import time, settings, os, datetime

from Servo import servo_pig
from Sensors import motion, sound, touch, gas
from SensorData.sensornames import SensorNames

from Messaging import gmail
from Logger.logger import Logger

class TeddyBear:
    def __init__(self):
        self.cooldownMotionMin = 0
        #100 ticks = (100*0.1) = 10 secs
        self.cooldownMotionMax = 100
        
        self.tired = False
        self.motionDetected = False
        
        sound.init()
        motion.init()
        servo_pig.init()
        
        #self.touchLogger = Logger(SensorNames.TOUCH)
        self.soundLogger  = Logger(SensorNames.SOUND)
        self.motionLogger = Logger(SensorNames.MOTION)
        
        time.sleep(2) 
        
    def monitor(self):
        while True:
            try:
                if not self.motionDetected and self.cooldownMotionMin == 0:
                   if motion.inRange():
                       self.motionLogger.log(1)
                       self.motionDetected = True
                       self.cooldownMotionMin = self.cooldownMotionMax
                       
                if sound.detectSoundLevel(settings.human_sound_level):
                    self.soundLogger.log(2)
                    
                #if touch.isTouched():
                #    print("Touch detected")
                #    self.touchLogger.log(3)
                    
            except IOError:
                print("Error")
                
            if self.motionDetected and self.cooldownMotionMin >= 0 and self.cooldownMotionMin <= self.cooldownMotionMax:
                self.cooldownMotionMin = self.cooldownMotionMin - 1
                if self.cooldownMotionMin == 0:
                    self.motionDetected = False
            
            time.sleep(0.1)
        servo_pig.shutdown()
        

if __name__ == '__main__':
    objTeddyBear = TeddyBear()
    objTeddyBear.monitor()
