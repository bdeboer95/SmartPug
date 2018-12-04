import time, datetime

logFile = None;

class Logger:
    
    def __init__(self, sensor):
        self.sensor = sensor
        self.creationDate = self.timeToDateTime(self.getCurrentTimeStamp())
        self.createFile()

    def getCurrentTimeStamp(self):
        return time.time()

    def createFile(self):
        global logFile
    
        logFile = open("../SensorData/{0}/{1}.txt".format(self.sensor, self.creationDate), 'a')
        print time.time()

    def timeToDateTime(self, timeStamp):
        return datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    def log(self, sensorData):
        logFile.write('{}\n'.format(str(sensorData)))

objLogMotion = Logger('Motion')
objLogSound  = Logger('Sound')
objLogMotion.log(1)
objLogMotion.log(2)
objLogMotion.log(3)
objLogMotion.log('String Test')
