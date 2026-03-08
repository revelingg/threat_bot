Workflow

1. Take network scan data
    what do network scan data consist of?
2. Compare it against the MITRe framrwork to find attack paths
3. Store internal security policies as vector embeddings
    what are vector imbeddings?
    how will it improve search?
4. Let SOC query system via nattrual language using the AI

Tech Stakc
1. Python for backend code and calling API
2. ChromaDB to store the policies
3. OpenAI to generate the natrual language responses 
4. MITRE ATT&CK as the knowledge base to cross reference
5. Git for version country 

RAG SYStem
1. Retrieve: Pull  info from the vector DB or the stored knowledge base
2. Generate: Use openAI to genrate natrual language explanations & querying

Flow: 
- User query/network data imported 
    - Retrieve: ChromaDB + Mitre
        - OpenAI LLM
            - response back to user