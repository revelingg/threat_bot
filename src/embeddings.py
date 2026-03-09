#embeddings built to be reusable 

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env 


#calls the openai api
def generate_embeddings(text_list, model="text-embedding-3-small", api_key=None):
    """
        Generates embeddings for a list of texts using OpenAI.
        Param:
            text_list: the list of texts from the prepembed file
            model: the model to be used, can be changed per user
            api_key: default none but the script takes the api_key from the env variable
        
        Returns:
            returns embeddings( list)
            
        Action: Creates the api connection and for each text in the text list create an embedding for it
            then append the response of that embedding to the embeddings list ( the numbers) which will them be returned and parsed by prepembed
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OpenAI API key not provided and isnt in env variables.")
    else:
        client = OpenAI(api_key=api_key)

    embeddings = []
    #creates the embedding
    for text in text_list:
        response = client.embeddings.create(
            input=text,
            model=model
        )
        embeddings.append(response.data[0].embedding) #updated how to access the openai results old method wasnt correct
    
    return embeddings