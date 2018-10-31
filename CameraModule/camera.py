from picamera import PiCamera
from time import sleep
import uuid

def init():
camera= new PiCamera()

def takePicture():
    try:
        camera.start_preview()
        unique_filename = '/home/pi/Desktop/Smart Pug/Pictures/'+ str(uuid.uuid4())+'.jpg'
        #camera.start_recording('"/Desktop/Smart Pug/Videos/video.h264"')
        camera.capture(unique_filename)
        #camera.stop_recording()
        camera.stop_preview()
        return unique_filename
    except IOError:
        return None
        

def takeVideo()
    try:
        camera.start_preview()
        sleep(10)
        unique_filename ='/home/pi/Desktop/Smart Pug/Videos/'+str(uuid.uuid4())+'.h264'
        camera.start_recording(unique_filename)
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()
        return unique_filename
    except IOError:
        return None

    
