import requests, json, time

#import the current section from github
url = 'https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'
response = requests.get(url)

if response.status_code == 200:
    print("Request successful!......Proceeding with filtering")
    
    #begin filtering the results
    data = response.json()
    relevant_techniques = []  #output list of dict
    keywords = [
        "network", "service", "credential", "execution", 
        "credential access", "lateral movement", "collection",
        "exfiltration", "impact", "defense evasion"
        ]
    
    #checks the objects for matching names & appends it
    for obj in data['objects']:
        if obj['type'] == "attack-pattern":
            name = obj.get('name','').lower()
            description = obj.get('description','').lower()
            text = name + " " + description
            
            #extract the info based on keyword
            if any(k in text for k in keywords):
                tech_id = None
                for ref in obj.get("external_references", []):
                    if ref.get("source_name") == "mitre-attack":
                        tech_id = ref.get("external_id")     
                tactics = [t.get("phase_name") 
                          for t in obj.get("kill_chain_phases",[]) 
                          if t.get("phase_name")
                        ]  
                
                #after all the filtering stores the relevant info in a dict   
                technique = {
                    "id": tech_id,
                    "name": obj.get("name"),
                    "description": obj.get("description"),
                    "tactics": tactics,
                }

                relevant_techniques.append(technique)
                
    #cute writing to file screen
    print("="*50)
    print("      🛠️  MITRE ATT&CK Processing Started  🛠️")
    print("="*50)
 
    #writes to file
    with open("data/filtered_mitre.json", "w", encoding="utf-8") as f:
        for i,tech in enumerate(relevant_techniques, 1):
            print(f"[{i}/{len(relevant_techniques)}] Processing technique: {tech['name']}")
            time.sleep(0.2)
           
        print(f"\nSaved {len(relevant_techniques)} techniques to filtered_mitre.json")
        print("="*50)
        print("\n"*2)
        
        json.dump(relevant_techniques, f, indent=2, ensure_ascii=False)
        
else:
    print(f"Request failed with status code: {response.status_code}")