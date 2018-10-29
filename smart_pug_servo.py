import time
from Servo import servo

while True:
	try:
		servo.init()
		servo.sweep()
		time.sleep(2)
	except IOError:
		print("Error")

