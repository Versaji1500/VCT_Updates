import json
from notificationOptions import *
from vlrInfo import *

'''
Function to parse JSON files from the VLR API and acquire
relevant information from it. Information will be processed
and used to construct a message which can then be sent with
one of the notification methods from notificationOptions.py
'''


'''
Function to get updated JSON data, load the data, and return
the data when called
'''
def loadJSON(jsonType):
    if jsonType == "matches": getMatchDetails()
    if jsonType == "results": getMatchResults()
    if jsonType == "events": getEvents()
    
    with open((jsonType + ".json"), 'r') as file:
        data = json.load(file)
    
    return data
    

# TODO: Parse matches.json to get live scores
'''
- Get updated json. Check if there are live matches.
- Check if it is list of teams I care about
- Grab scores and send as update to Pushover
'''
def liveMatchScores():
    matches = loadJSON("matches")

    for match in matches["data"]:
        if (match["status"] == "Live"):
            for team in match["teams"]:
                if team["name"] in bangkokTeams:
                    print(f"Live Match Found: {match['event']} - {team['name']} is playing!")
        
                

        

# TODO: Parse matches.json to get results from past matches to send update on

    
liveMatchScores()