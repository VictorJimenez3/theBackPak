from readgyro import readData

import board
import busio
import adafruit_bno055
import RPi.GPIO as GPIO

import json, time
from pprint import pprint

label = input("input label for logging training data:\n>>> ").lower()

with open("loggedData.txt", "w") as f:
	f.write("")

with open("loggedData.txt", "a") as f:
	# Initialize I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, GPIO.HIGH)

    #TODO set GPIO for addr switch on sensor2 to HIGH

    # Initialize the first BNO055 sensor at address 0x28
	sensor1 = adafruit_bno055.BNO055_I2C(i2c, address=0x28)
	sensor2 = adafruit_bno055.BNO055_I2C(i2c, address=0x29) #with pinHIGH on addr
	
	payload = []
	while True:
		postureValues = readData(sensor1, sensor2)
		if not postureValues or not all(postureValues.values()):
			continue
		"""
		s1x, s1y, s1z, s2x, s2y, s2z, label
		"""
		payload.extend([str(x) for x in postureValues["s1"]])
		payload.extend([str(x) for x in postureValues["s2"]])
		pprint(postureValues)
		
		f.write(",".join(payload) + f", {label}" + "\n")
		payload = []
		if not postureValues:
		    continue #don't wait with nullish values, execute immediately 
		    
		time.sleep(.1)
