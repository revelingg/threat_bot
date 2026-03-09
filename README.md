# Threat Intelligence Bot 

## Overview
  The Threat Intelligence Bot is a Python-based cybersecurity tool that uses RAG systems o analyze network scan information and identify potential attacker behavior based on the MITRE ATT&CK framework. 

  The system converts MITRE techniques into vector embeddings and stores them in ChromaDB, allowing the bot to search through when a user submits a network scan or security-related question. The bot retrieves the most relevant techniques and uses an LLM [OpenAI](https://openai.com) to generate attack path analysis and mitigation recommendations that resemble what a SOC analyst might produce.


## How The System Works
1. MITRE ATT&CK techniques are filtered and cleaned to remove unnecessary metadata.
2. Each technique is converted into structured text and transformed into vector embeddings using the OpenAI API.
3. The embeddings are then stored in ChromaDB
4. When a user submits a query (for ex: results of a network scan), the system:
  - [x] Generates an embedding for the query
  - [X] Searches the vector DB for the most relevant techniques(top 5)
  - [X] Sends those techniques to the LLM
  - [X] Produces an analysis and mitgation recommendation


# Installation
1. Clone the repo: git clone https://github.com/revelingg/threat_bot.git
2. cd into it: cd threat_bot
3. **Install** the required libraries using pip
   - **pip install openai chromadb python-dotenv python requests**
4. Create a .env file in the root directory
   - within the file input: **OPENAI_API_KEY=your_key**
   - your key should be gotten from chatgpt open ai website other tutorials       on the web for that

# Project Structure 
threat_bot
- data
  - filtered_mitre.json
  - chroma_db
- scripts: prepembed.py, filterdata.py
- src: threatbot.py, retriever.py, embeddings.py
- readme.md

# File Roles:
**prepembed.py**
Processes the filtered MITRE dataset and generates embeddings.

**filterdata.py**
Filters the large mitre sheet into smaller network related information ~ 655 entries

**embeddings.py**
Handles communication with the OpenAI API to generate vector embeddings.

**retriever.py**
Queries the ChromaDB vector database for techniques relevant to user input.

**threatbot.py**
Main application that ties everything together and produces the threat analysis.

# How to Run the Project
1. Generate the mitre embeddings & load the dataset by running **python -m scripts.prepembed.py**
2. Run the bot with: **python -m src.threatbot**
3. The menu will have various options you can put in
  - An example with option 1 is "Open SSH on 192.168.1.10 and HTTP on 192.168.1.12 detected."
  - Option 2 will take in a file path to be parsed

# Example Output:
- Likely MITRE ATT&CK techniques
- Possible attack paths
- Recommended mitigation steps
- SOC-style analysis of the network exposure

# LICENSE
This project is intended for educational and research purposes.
