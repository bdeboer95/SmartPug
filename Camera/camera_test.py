from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.start_preview()
sleep(10)
#camera.start_recording('"/Desktop/Smart Pug/Videos/video.h264"')
camera.capture('/home/pi/Desktop/Smart Pug/Pictures/test.jpg')
#camera.stop_recording()
camera.stop_preview()
