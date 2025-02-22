import requests
import json
import os

'''
This is code to grab information from the VLR API and save
it to the appropriate JSON file

There are multiple types of information so the functions
are designed separately to account for each one
'''


# Arrays with events and teams to check for in JSON file
urls = {"events": 'https://vlr.orlandomm.net/api/v1/events',
        "matches": 'https://vlr.orlandomm.net/api/v1/matches',
        "results": 'https://vlr.orlandomm.net/api/v1/results?page=1',
        "live_match":  'https://vlrggapi.vercel.app/match?q=live_score'
    }

# List of important events to monitor
events = ['Champions Tour 2025: Masters Bangkok', 
          'Champions Tour 2025: Americas Stage 1', 
          'Champions Tour 2025: Masters Toronto',
          'Champions Tour 2025: Americas Stage 2'
]

# List of teams to monitor
teamsOverall = [
    "100 Thieves",
    "Cloud9",
    "Evil Geniuses",
    "Leviatán",
    "LOUD",
    "MIBR",
    "NRG",
    "Sentinels",
    "G2 Esports",
    "Edward Gaming",
    "Team Vitality"
]

# List of teams especially important to me
importantTeams = [
    "Sentinels",
    "G2 Esports",
    "Edward Gaming",
    "Team Vitality",
    "NRG"
    "Cubert Academy"
]

# List of teams attending Masters Bangkok 2025
bangkokTeams = [
    "Trace Esports",
    "G2 Esports",
    "EDward Gaming",
    "Team Liquid",
    "DRX",
    "Sentinels",
    "Team Vitality",
    "T1",
    "Cubert Academy"
]


# *Function to get the requested information from the URL that is passed in
# *The function creates a JSON under the name of information acquired
def importVLRJSON(request):
    # Specify save location
    fileDirectory = "/home/joels/Documents/Projects/VCT_Updates"
    
    # API URL where the information is hosted
    url = urls.get(request)
    response = requests.get(url)

    # If request is successful, save the information to a JSON file
    # under the name of the nature of the request
    if response.status_code == 200:
        data = response.json()  # Get the API response as JSON
        
        file_path = os.path.join(fileDirectory, f"{request}.json")
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)  # Save to a JSON file with indentation
        print(f"Data saved to {request}.json")
    else:
        print("Error:", response.status_code)

# *Function to get a list of Valorant events
# *Returns the prefix of the JSON file created
def getEvents():
    importVLRJSON("events")
    return "events"

# *Function to get upcoming valorant matches
# *Returns the prefix of the JSON file created
def getMatchDetails():
    importVLRJSON("matches")
    return "matches"

# *Function to get a list of past results from matches
# *Returns the prefix of the JSON file created
def getMatchResults():
    importVLRJSON("results")
    return "results"

# *Function to get live match results
# *Returns the prefix of the JSON file created
def getLiveMatch():
    importVLRJSON("live_match")
    return "live_match"
