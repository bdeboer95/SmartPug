import unittest
from Sensors import touch
from Sensors import sound
import settings

class touchTest(unittest.TestCase):
    def isTouchable(self):
        if(settings.touch_sensor):
            self.assertEqual(touch.init(),1)
        else:
            self.assertEqual(touch.init(),0)
        
class soundTest(unittest.TestCase):
    def canHear(self):
        if(settings.sound_sensor):
            self.assertEqual(sound.init(), 1)
        else:
            self.assertEqual(sound.init(), 0)
            

def create_suite():
    test_suite=unittest.TestSuite()
    test_suite.addTest(touchTest('isTouchable'))
    test_suite.addTest(soundTest('canHear'))
    return test_suite

if  __name__ == '__main__':
    suite=create_suite()
    
    runner=unittest.TextTestRunner()
    runner.run(suite)
    