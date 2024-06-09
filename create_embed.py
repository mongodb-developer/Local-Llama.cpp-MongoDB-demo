import subprocess
import json

def generate_embedding(text):
    result = subprocess.run(['./llama.cpp', '--text', text], capture_output=True, text=True)
    return json.loads(result.stdout)["embedding"]

# Example usage
embedding = generate_embedding("Clicked on product A")
print(embedding)
