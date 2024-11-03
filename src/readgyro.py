#native
from pprint import pprint
import math

def quaternion2Euler(w, x, y, z):
    """
    Converts quaternion (w, x, y, z) to Euler angles (roll, pitch, yaw).

    Parameters:
    w, x, y, z -- the quaternion components

    Returns:
    A tuple (roll, pitch, yaw) in degrees
    """
    
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

def readData(sensor1, sensor2):
    payload = []
    
    try:
        payload.extend(quaternion2Euler(*sensor1.quaternion))
        payload.extend(quaternion2Euler(*sensor2.quaternion))
    except Exception as e:
        print(f"Err: {e}")
    
    #keep reading till amended on addressing
    return None if not any(payload) else payload
