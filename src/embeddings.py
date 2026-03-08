#embeddings built to be reusable 

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env 


#calls the openai api
def generate_embeddings(text_list, model="text-embedding-3-small", api_key=None):
    """
    Generates embeddings for a list of texts using OpenAI.
    Returns a list of embeddings in the same order.
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
        embeddings.append(response['data'][0]['embedding'])
    
    return embeddings