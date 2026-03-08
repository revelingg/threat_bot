from openai import OpenAI
import chromadb
from chromadb.config import Settings


class MitreRetriever:
    
    #initializes the retriever system
    def __init__(self,api_key,collection_name="mitre_techniques"):
        self.client = OpenAI(api_key=api_key)
        self.chroma_client = chromadb.PersistentClient(path="./data/chroma_db")

        self.collection = self.chroma_client.get_or_create_collection(collection_name)
    
    def query(self,query_text, top_n=5):
        #makes an embeding for the query
        response = self.client.embeddings.create(
            input=query_text,
            model="text-embedding-3-small"
        )
        query_embedding = response.data[0].embedding
        #search the db for similar results with the vectors
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_n
        )
        
        #return the document text from similar embeddings
        return results["documents"][0]