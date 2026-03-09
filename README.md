Threat Intelligence Bot
Overview

The Threat Intelligence Bot is a Python-based cybersecurity tool that uses Retrieval-Augmented Generation (RAG) to analyze network scan information and identify potential attacker behavior based on the MITRE ATT&CK framework.

The system converts MITRE techniques into vector embeddings and stores them in ChromaDB, allowing the bot to perform semantic searches when a user submits a network scan or security-related question. The bot retrieves the most relevant techniques and uses an LLM to generate attack path analysis and mitigation recommendations that resemble what a SOC analyst might produce.

This project demonstrates how modern AI-assisted threat intelligence workflows can be built by combining vector databases, language models, and structured security frameworks.