#packages
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, CORS
import board
import busio
import adafruit_bno055
import RPi.GPIO as GPIO

#built-ins
import json, os, threading, socket
from pprint import pprint
from time import sleep

#files
from readgyro import readData
from linreg import getPosture

postureValues = {}

#read posture values
def readPostureValuesInBackground():
    global postureValues
    
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    GPIO.setmode(GPIO.BCM); GPIO.setup(21, GPIO.OUT)
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

app.config.update( #sets encryption key for session-cookies
    TESTING=True,
    SECRET_KEY=os.environ["FLASK_KEY"]
)

#ROUTES
@app.route("/")
def homepage(): #TODO check redirect usage
    return redirect("/goodPosture")

@app.route("/posture", methods=["GET"])
def posture():
    return render_template("posture.html")

# @app.route("/goodPosture")
# def goodPosture():
#     return render_template("goodPosture.html")

# @app.route("/badPosture")
# def badPosture():
#     return render_template("badPosture.html")

@app.route("/api/getPosture/", methods=["GET"])
def manipulateGyroscope():
    pprint(f"Received request: {json.loads(request.json)}") #TODO delete for deployment

    return jsonify({
        "isGoodPosture" : "ERROR" if not any(postureValues.values()) else getPosture(postureValues)
    }), 200

if __name__ == "__main__":
    measureGyroThread = threading.Thread(target=readPostureValuesInBackground, daemon=True)
    measureGyroThread.start()
    app.run()