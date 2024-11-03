#My Hero: https://www.youtube.com/watch?v=daMxiBS0odk
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from pprint import pprint

# Load environment variables from the .env file
load_dotenv()

# Retrieve the URI from the environment
uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Choose a database and collection
db = client['TheBackPak']  # Cannot be changed, name of CLUSTER
collection = db['collection1']  # Can name it whatever, new name means new collection of data

def addRecordToDatabase(isGoodPosture: int):
    import random
    isGoodPosture = random.randint(0,1)#remove later
    """
    Modifies the single entry in the Users collection to update the good_posture_count
    and update_count. If isGoodPosture is 1, increment good_posture_count; otherwise, only increment posture_update_count.
    """
    try:
        # Update the record or insert a new one if none exists
        update_fields = {"$inc": {"posture_update_count": 1}}
        if isGoodPosture == 1:
            update_fields["$inc"]["good_posture_count"] = 1
        
        collection.update_one(
            {},  # Modify this filter to target the appropriate document(s) in the collection
            update_fields,
            upsert=True  # Create a new document if none exists
        )
        print("Record updated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def deriveDailyScore():
    gpc = 0
    puc = 0
    for x in collection.distinct("good_posture_count"):
        gpc = x
    for y in collection.distinct("posture_update_count"):
        puc = y

    return (gpc / puc) *100

# Example call

pprint(deriveDailyScore())
addRecordToDatabase(1)  # Update posture status with good posture

# Confirm data insertion by printing the inserted data
for doc in collection.find():
    print(doc)
    pprint(deriveDailyScore())
