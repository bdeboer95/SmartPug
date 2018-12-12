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
        
        self.cooldownSoundMin = 0
        #20 ticks = (20*0.1) = 2 secs
        self.cooldownSoundMax = 20
        
        self.tired = False
        self.soundDetected = False
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
                       self.motionLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), 1))
                       self.motionDetected = True
                       self.cooldownMotionMin = self.cooldownMotionMax
                       
                if not self.soundDetected and self.cooldownSoundMin == 0:
                    self.soundLogger.log('{};{}'.format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')), sound.getSoundLevel()))
                    self.soundDetected = True
                    self.cooldownSoundMin = self.cooldownSoundMax
                    
                #if touch.isTouched():
                #    print("Touch detected")
                #    self.touchLogger.log(3)
                    
            except IOError:
                print("Error")
                
            if self.motionDetected and self.cooldownMotionMin >= 0 and self.cooldownMotionMin <= self.cooldownMotionMax:
                self.cooldownMotionMin = self.cooldownMotionMin - 1
                if self.cooldownMotionMin == 0:
                    self.motionDetected = False
        
            if self.soundDetected and self.cooldownSoundMin >= 0 and self.cooldownSoundMin <= self.cooldownSoundMax:
                self.cooldownSoundMin = self.cooldownSoundMin - 1
                if self.cooldownSoundMin == 0:
                    self.soundDetected = False
            
            time.sleep(0.1)
        servo_pig.shutdown()
        

if __name__ == '__main__':
    objTeddyBear = TeddyBear()
    objTeddyBear.monitor()
