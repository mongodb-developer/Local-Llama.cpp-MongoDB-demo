from pymongo import MongoClient
import subprocess
import json

# Connect to MongoDB Atlas
uri = "your_mongodb_atlas_connection_string"
client = MongoClient(uri)
db = client.myDatabase
collection = db.userInteractions

def generate_embedding(text):
    result = subprocess.run(['./llama.cpp', '--text', text], capture_output=True, text=True)
    return json.loads(result.stdout)["embedding"]
# Retrieve data

interactions = collection.find()
for interaction in interactions:
    # Generate embedding
    embedding = generate_embedding(interaction["interaction"])
    # Update document with embedding
    collection.update_one({"_id": interaction["_id"]}, {"$set": {"embedding": embedding}})

print("Processed and updated all documents with embeddings.")
