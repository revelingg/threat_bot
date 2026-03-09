from openai import OpenAI
import chromadb
from chromadb.config import Settings



class MitreRetriever:
    
    #initializes the retriever system
    def __init__(self,api_key,collection_name="mitre_techniques"):
        """
            Description: Initializes an instnace of the retriever object
            Parameters: Takes in self, the api key(specifcied from the user env file),  
                and then the collection name which is hardcoded currently as mitre_techniques (the collection that gets passed)  
        """
        
        self.client = OpenAI(api_key=api_key)
        self.chroma_client = chromadb.PersistentClient(path="./data/chroma_db") #persistnet storage for our info

        self.collection = self.chroma_client.get_or_create_collection(collection_name)
        #print("Techniques in DB:", self.collection.count()) run this to ensure your stuff got saved
    
    def query(self,query_text, top_n=5):
        """
            Description: Generates and returns the query embeddings for the user
            Param:
                self = takes in the self obj
                query_text: text obj that the user typed in or is parsed from a file(parsing coming soon)
                top_n: this declares the top 5 results so the bot isnt combing forever
            
            Returns: 
                results(dict/nested list): Results from the query is inherently a dict, but we access it as a nested list
                hence thats what we get back a list of lists which we always get the first item in the documents section

        """
        
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