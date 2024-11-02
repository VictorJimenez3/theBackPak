#native
from pprint import pprint
from time import sleep
import math

#packages
import board
import busio
import adafruit_bno055


def quaternion2Euler(w, x, y, z):
    """
    Converts quaternion (w, x, y, z) to Euler angles (roll, pitch, yaw).

    Parameters:
    w, x, y, z -- the quaternion components

    Returns:
    A tuple (roll, pitch, yaw) in degrees
    """
    
    if not any((w, x, y, z)):
        return None
    
    # Roll (x-axis rotation)
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(t0, t1)

    # Pitch (y-axis rotation)
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = math.asin(t2)

    # Yaw (z-axis rotation)
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(t3, t4)

    return [x*(180/math.pi) for x in (roll, pitch, yaw)]

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the first BNO055 sensor at address 0x28
sensor1 = adafruit_bno055.BNO055_I2C(i2c, address=0x28)

# Initialize the second BNO055 sensor at address 0x29
#sensor2 = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

# Example of reading data from both sensors
print("Reading data from Sensor 1")

while True:
    pprint(quaternion2Euler(*sensor1.quaternion))
    sleep(.25)

print("\nReading data from Sensor 2")

#print("Gyroscope:", sensor2.quanternion)
