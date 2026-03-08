from src.retriever import MitreRetriever
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys



load_dotenv() 
API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    #initialize retriever
    try:
        retriever = MitreRetriever(api_key=API_KEY)
    except Exception as e:
        print(f"Failed to initalize the retriever: {e}")
        return 
    
    print("\n"*2 )
    print("🛡️  Threat Intelligence Bot  🛡️")
    print("Welcome! Select an option from the menu below.\n")
    
    while True:
        print("="*50)
        print("Menu Options:")
        print("1️⃣  Write your own query")
        print("2️⃣  Parse network scan / file data")
        print("3️⃣  Exit")
        print("Always remeber! Ctrl+C to force quit @@@👋")
        print("="*50)
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        if choice == "3":
            print("Exiting bot! Stay Safe@@@👋")
            break
        elif choice == "1":
            query = input("\nEnter your network scan or question: ").strip()
            if not query:
                print("No input provided. Pls try again.\n")
                continue
            
            try:
                #retrieve data
                top_results = retriever.query(query,top_n=5)
                if not top_results:
                    print("Alert!! No relevant techniques found.@@@\n")
                    continue
                
                #combine the results to feed into AI and then create AI prompt
                techniques_text = "\n".join(top_results)
                prompt=f""" 
                    You are a cybersecurity analyst AI.

                        Network scan or user input: "{query}"

                        Relevant MITRE techniques:
                        {techniques_text}

                        Provide a prioritized attack path analysis and mitigation recommendations
                        as if you are advising a SOC team.
                """
                
                #query open ai 
                client = OpenAI(api_key=API_KEY)
                response = client.chat.completions.create(
                    model="gpt-4.1",
                    messages=[{"role": "user", "content": prompt}]
                )
                #output
                output = response.choices[0].message.content
                print("\n--- Threat Intelligence Analysis ---\n")
                print(output)
                print("\n----------------------------------\n")
                
            except Exception as e:
                print(f"Error during query/AI response: {e}\n")
                continue
            
        elif choice=="2":
            print("under developmnent")
        else:
            print("Invalid Choice @@@@ Pls enter 1,2,or 3. \n")
        
if __name__ == "__main__":
    main()