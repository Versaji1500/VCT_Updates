import requests
import json

# Arrays with events and teams to check for in JSON file
urls = {"events": 'https://vlr.orlandomm.net/api/v1/events',
        "matches": 'https://vlr.orlandomm.net/api/v1/matches',
        "results": 'https://vlr.orlandomm.net/api/v1/results?page=1'
    }

events = ['Champions Tour 2025: Masters Bangkok', 
          'Champions Tour 2025: Americas Stage 1', 
          'Champions Tour 2025: Masters Toronto'
]

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

importantTeams = [
    "Sentinels",
    "G2 Esports",
    "Edward Gaming",
    "Team Vitality",
    "NRG"
]

def importVLRJSON(request):
    # API URL where the information is hosted
    url = urls.get(request)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Get the API response as JSON
        with open(request+".json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)  # Save to a JSON file with indentation
        print("Data saved to matches.json")
    else:
        print("Error:", response.status_code)

def getEvents():
    importVLRJSON("events")
    
    with open('events.json', 'r') as events:
        tournaments = json.load(events)
        
    events = [
    tournament["name"] for tournament in tournaments["data"] if "Champions Tour 2025" in tournament["name"]
    ]

def getMatchDetails():
    importVLRJSON("matches")
    
    with open('matches.json', 'r') as matches:
        liveMatches = json.load(matches)
        
    

getMatchDetails()