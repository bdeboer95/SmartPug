import time, datetime

logFile = None;

class Logger:
    
    def __init__(self, sensor):
        global logFile
        logFile = open("../SensorData/{0}/{1}.txt".format(sensor, self.timeToDateTime(self.getCurrentTimeStamp())), 'a')

    def getCurrentTimeStamp(self):
        return time.time()

    def timeToDateTime(self, timeStamp):
        return datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    def log(self, sensorData):
        logFile.write('{}\n'.format(str(sensorData)))

objLogMotion = Logger('Motion')
objLogMotion.log(1)
objLogMotion.log(2)
objLogMotion.log(3)
objLogMotion.log('String Test')
