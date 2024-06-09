from pymongo import MongoClient

# Replace with your MongoDB Atlas connection string
uri = "your_mongodb_atlas_connection_string"
client = MongoClient(uri)
db = client.myDatabase
collection = db.userInteractions
Insert Data
Inserting Data: Insert user interaction data into your MongoDB Atlas collection.

interactions = [
    {"user_id": 1, "interaction": "Clicked on product A", "timestamp": "2023-06-01T12:00:00Z"},
    {"user_id": 2, "interaction": "Viewed category B", "timestamp": "2023-06-01T12:05:00Z"},
    # Add more interactions as needed
]
