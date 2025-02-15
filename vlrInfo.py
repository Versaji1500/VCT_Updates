import requests
import json

# Arrays with events and teams to check for in JSON file
urls = {"events": 'https://vlr.orlandomm.net/api/v1/events',
        "matches": 'https://vlr.orlandomm.net/api/v1/matches',
        "results": 'https://vlr.orlandomm.net/api/v1/results?page=1'
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


# *Function to get the requested information from the URL that is passed in
# *The function creates a JSON under the name of information acquired
def importVLRJSON(request):
    # API URL where the information is hosted
    url = urls.get(request)
    response = requests.get(url)

    # If request is successful, save the information to a JSON file
    # under the name of the nature of the request
    if response.status_code == 200:
        data = response.json()  # Get the API response as JSON
        with open(request+".json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)  # Save to a JSON file with indentation
        print("Data saved to matches.json")
    else:
        print("Error:", response.status_code)

# *Function to get a list of Valorant events
# *Returns the prefix of the JSON file created
def getEvents():
    importVLRJSON("events")
    return "events"

# *Function to get list of live and upcoming valorant matches
# *Returns the prefix of the JSON file created
def getMatchDetails():
    importVLRJSON("matches")
    return "matches"

# *Function to get a list of past results from matches
# *Returns the prefix of the JSON file created
def getMatchResults():
    importVLRJSON("results")
    return "results"
    
    
