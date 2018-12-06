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
        self.detected = False
        
        sound.init()
        motion.init()
        servo_pig.init()
        
        #self.touchLogger  = Logger(SensorNames.TOUCH)
        self.soundLogger  = Logger(SensorNames.SOUND)
        self.motionLogger = Logger(SensorNames.MOTION)
        
        date_kickoff_midnight = datetime.datetime.strptime('2018-12-04 00:00:00', "%Y-%m-%d %H:%M:%S")
        print date_kickoff_midnight
        
        d = datetime(2018, 12, 4, 0, 0, 0)
        unixtime = time.mktime(d.timetuple())
        print unixtime
        
        date_kickoff = datetime.datetime.strptime(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
        print date_kickoff
        
        date_monitor_one   = date_kickoff + datetime.timedelta(days=1)
        date_monitor_two   = date_kickoff + datetime.timedelta(days=2)
        date_monitor_three = date_kickoff + datetime.timedelta(days=3)
        date_monitor_four  = date_kickoff + datetime.timedelta(days=4)
        date_monitor_five  = date_kickoff + datetime.timedelta(days=5)
        date_monitor_six   = date_kickoff + datetime.timedelta(days=6)
        
        print date_monitor_one
        print date_monitor_two
        print date_monitor_three
        print date_monitor_four
        print date_monitor_five
        print date_monitor_six
        
        time.sleep(2) 
        
    def monitor(self):
        while True:
            try:
                if not self.detected and self.cooldownMotionMin == 0:
                   if motion.inRange():
                       self.motionLogger.log(1)
                       self.detected = True
                       self.cooldownMotionMin = self.cooldownMotionMax
                       
                if sound.detectSoundLevel(settings.human_sound_level):
                    self.soundLogger.log(2)
                    
                #if touch.isTouched():
                #    print("Touch detected")
                #    self.touchLogger.log(3)
                    
            except IOError:
                print("Error")
                
            if self.detected and self.cooldownMotionMin >= 0 and self.cooldownMotionMin <= self.cooldownMotionMax:
                self.cooldownMotionMin = self.cooldownMotionMin - 1
                if self.cooldownMotionMin == 0:
                    self.detected = False
            
            time.sleep(0.1)
        servo_pig.shutdown()
        

if __name__ == '__main__':
    objTeddyBear = TeddyBear()
    objTeddyBear.monitor()
