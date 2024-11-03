#My Hero: https://www.youtube.com/watch?v=daMxiBS0odk
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

#put this in .env before you commit
uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Choose a database and collection
db = client['TheBackPak']  # Cannot be changed, name of CLUSTER
collection = db['collection1']  # Can name it whatever, new name means new collection of data

# Sample data: replace these with actual collected data
good_posture_count = 160  # Number of times good posture was detected
posture_update_count = 200  # Total number of times posture was updated

# Data to be inserted
data_entry = {
    "good_posture_count": good_posture_count,
    "posture_update_count": posture_update_count,
}

# Insert the data into the collection
try:
    collection.insert_one(data_entry)
    print("Posture data inserted successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

# Confirm data insertion by printing the inserted data
for doc in collection.find():
    print(doc)
