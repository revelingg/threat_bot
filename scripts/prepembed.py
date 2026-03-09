import json
import chromadb
from chromadb.config import Settings
from src.embeddings import generate_embeddings
from dotenv import load_dotenv
import os


"""
    Description/Steps:
        1. Takes the APi key from the env file you should have created
        2. loads the json file from the filtered mitre data and stores it in a variable
        3. for each item in the mitre data, append the info in a easy/readable format
        4. append that to the text list along with the ids
        5. generate the embeddings using the api key along with that text that was then created
            5i. The ai  will now take it and form vectors to categorize all the information similarly
        6. the return variable from the embeddings function will be the related documents
        7. Those documents/embeddings will now then be stored in the ChromaDB using the upsert collction function
        

"""

load_dotenv()  # loads variables from .env 
API_KEY =  os.getenv("OPENAI_API_KEY")

with open("./data/filtered_mitre.json", encoding="utf-8") as f:
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
try:
    client = chromadb.PersistentClient(path="./data/chroma_db") #access the storage db
    collection = client.get_or_create_collection("mitre_techniques") #creates/gets the collection and access that
except Exception as e:
    print(f"The chroma client could not be created: {e}\n")


collection.upsert( #use this instead of add so it overwrites duplicates instead of breaking the loop
    documents=texts,
    embeddings= embeddings,
    ids=ids
)
    
print(f"Stored {len(ids)} techniques in ChromaDB!")