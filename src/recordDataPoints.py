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
	
	while True:
		data = readData(sensor1, sensor2)
		if not data:
			continue
		postureValues = [str(x) for x in data]
		if not postureValues or not all(postureValues):
			continue
		"""
		s1x, s1y, s1z, s2x, s2y, s2z, label
		"""
		pprint(postureValues)
		
		f.write(",".join(postureValues) + f", {label}" + "\n")
		if not postureValues:
		    continue #don't wait with nullish values, execute immediately 
		    
		time.sleep(.1)
