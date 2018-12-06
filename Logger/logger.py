import time, datetime

class Logger:
    def __init__(self, sensor):
        self.logFile = None
        self.sensor = sensor
        self.creationDate = self.timeToDateTime(self.getCurrentTimeStamp())
        self.createFile()

    def getCurrentTimeStamp(self):
        return time.time()

    def createFile(self):
        self.logFile = open("./SensorData/{0}/{1}.txt".format(self.sensor, self.creationDate), 'a')

    def timeToDateTime(self, timeStamp):
        return datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    def log(self, sensorData):
        self.logFile.write('{}\n'.format(str(sensorData)))
        self.logFile.flush()
        
