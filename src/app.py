#packages
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_cors import CORS
import board
import busio
import adafruit_bno055
import RPi.GPIO as GPIO

#built-ins
import json, os, threading, socket
from pprint import pprint
from time import sleep
from datetime import datetime
import hashlib

#files
from readgyro import readData
from linreg import getPosture

postureValues = {}

#read posture values
def readPostureValuesInBackground():
    global postureValues
    
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    GPIO.setmode(GPIO.BCM);
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)

    #TODO set GPIO for addr switch on sensor2 to HIGH

    # Initialize the first BNO055 sensor at address 0x28
    sensor1 = adafruit_bno055.BNO055_I2C(i2c, address=0x28)
    sensor2 = adafruit_bno055.BNO055_I2C(i2c, address=0x29) #with pinHIGH on addr

    while True:
        postureValues = readData(sensor1, sensor2)
        if not postureValues:
            continue #don't wait with nullish values, execute immediately 
        sleep(.1)

#APP
app = Flask(__name__)

CORS(app)
#TODO hash secret key
#m = hashlib.sha256()
#hashed = m.update(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).digest()
#hashed = hashed.hexdigest()

hashed="testing for now"
app.config.update( #sets encryption key for session-cookies
    TESTING=True,
    SECRET_KEY=hashed
)

#ROUTES
@app.route("/")
def homepage():
    return render_template("index.html")
    
@app.route("/api/getPosture", methods=["GET"])
def getPostureRequest():
    return jsonify({
        "isGoodPosture" : "ERROR" if not postureValues or not all(postureValues) else ("TRUE" if getPosture(postureValues) else "FALSE"),
        "status" : 400 if not postureValues or not all(postureValues) else 200
    })
    
@app.route("/api/startMeasure", methods=["GET"])
def startGryoMeasure():
    if __name__ == "__main__":
        try:
            measureGyroThread = threading.Thread(target=readPostureValuesInBackground, daemon=True)
            measureGyroThread.start()
        except Exception as e:
            print(f"error in largest thread scope, {e}")
        return jsonify({"message" : "success"})
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 10998)

