import board
import busio
import adafruit_bno055

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the first BNO055 sensor at address 0x28
sensor_1 = adafruit_bno055.BNO055_I2C(i2c, address=0x28)

# Initialize the second BNO055 sensor at address 0x29
#sensor_2 = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

# Example of reading data from both sensors
print("Reading data from Sensor 1")

print("Gyroscope:", sensor_1.gyro)

print("\nReading data from Sensor 2")

#print("Gyroscope:", sensor_2.gyro)
