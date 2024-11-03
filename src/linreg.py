import joblib
import numpy as np

def getPosture(postureValues):
    """
    Uses regression to determine whether posture is good or bad
    Returns 1 for good posture, 0 for bad posture
    """
    model = joblib.load('../model/model.pkl')
    
    print(postureValues)
    data = np.array(postureValues).reshape(1, -1)
    
    prediction = model.predict(data)
    
    return int(prediction[0])
