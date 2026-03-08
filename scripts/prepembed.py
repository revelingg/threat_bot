import json
import chromadb
from chromadb.config import Settings
from src.embeddings import generate_embeddings
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env 

API_KEY =  os.getenv("OPENAI_API_KEY")

with open("data/filtered_mitre.json", encoding="utf-8") as f:
    mitre_data = json.load(f)

texts = []
ids = []

#convert the json file for each technique to a text that can be embedded
for tech in mitre_data:
    text = f"""
        Technique: {tech['id']}
        Name: {tech['name']}
        Tactics: {', '.join(tech['tactics'])}
        Description: {tech['description']}
    """

    texts.append(text)
    ids.append(tech['id'])

#generate the embeddings 
embeddings = generate_embeddings(texts, api_key=API_KEY)

#Store in DB
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet"))
collection = client.get_or_create_collection("mitre_techniques")

for i in range(len(ids)):
    collection.add(
        documents=[texts[i]],
        embeddings=[embeddings[i]],
        ids=[ids[i]] )
    
print(f"Stored {len(ids)} techniques in ChromaDB!")