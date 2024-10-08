# Notice: Repository Deprecation
This repository is deprecated and no longer actively maintained. It contains outdated code examples or practices that do not align with current MongoDB best practices. While the repository remains accessible for reference purposes, we strongly discourage its use in production environments.
Users should be aware that this repository will not receive any further updates, bug fixes, or security patches. This code may expose you to security vulnerabilities, compatibility issues with current MongoDB versions, and potential performance problems. Any implementation based on this repository is at the user's own risk.
For up-to-date resources, please refer to the [MongoDB Developer Center](https://mongodb.com/developer).

# Local-Llama.cpp-MongoDB-demo 🦙
Run Llama.cpp locally (local LLM) persist embeddings and data to MongoDB Atlas

![Description of the image](https://drive.google.com/uc?export=view&id=1mxAWh35Psc6uxbTjRkViAhoW35v-U-zq)

# Install Llama.cpp
```
brew install llama.cpp
```
# Start llama server
```
llama-server --hf-repo microsoft/Phi-3-mini-4k-instruct-gguf --hf-file Phi-3-mini-4k-instruct-q4.gguf
```
# Connect to local host on port 8080
```
curl 8080/v1/chat/completions 
```

# Integrating MongoDB Atlas and llama.cpp

## Step 1: Data Ingestion

### Connect to MongoDB Atlas

1. **Install `pymongo`**:
```
pip3 install pymongo
```     
Connect to MongoDB Atlas: Use your connection string to connect to MongoDB Atlas.

```
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
```

Step 2: Model Processing with llama.cpp

Generate Embeddings

Script to Generate Embeddings:
```
import subprocess
import json

def generate_embedding(text):
    result = subprocess.run(['./llama.cpp', '--text', text], capture_output=True, text=True)
    return json.loads(result.stdout)["embedding"]

# Example usage
embedding = generate_embedding("Clicked on product A")
print(embedding)
```

Step 3: Store Processed Data in MongoDB Atlas
Extend the Ingestion Script:
```
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
```

Summary

Connect to MongoDB Atlas: Ensure your Python script connects to your MongoDB Atlas cluster using the connection string.

Generate Embeddings: Use llama.cpp to generate embeddings for your text data.

Store Processed Data: Update your MongoDB Atlas collection with the generated embeddings.

# Useful Resources

## llama.cpp Documentation
[llama.cpp Python Documentation](https://llama-cpp-python.readthedocs.io/en/latest/)

## LangChain Integration with llama.cpp 🦜 ⛓️
[LangChain llama.cpp Integration Documentation](https://python.langchain.com/v0.2/docs/integrations/llms/llamacpp/)

