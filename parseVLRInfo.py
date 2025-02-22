import json
from notificationOptions import *
from vlrInfo import *
import unicodedata 

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
    # Load the appropriate data based on what data we need
    # Determined by the passed in variable
    if jsonType == "matches": getMatchDetails()
    if jsonType == "results": getMatchResults()
    if jsonType == "events": getEvents()
    if jsonType == "live_match": getLiveMatch()
    
    # Load the JSON data file into the data variable and return for processing
    with open((jsonType + ".json"), 'r') as file:
        data = json.load(file)
    
    return data

'''
Function to normalize and compare strings

This removes any accents and makes the word lowercase
'''
def normalize(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8').lower()
    

'''
Get the score information for a map for each team, construct the string
and return it
'''
def mapScoreString(match):
    # Get score info from whichever variable is not "N/A"
    
    team1score = None
    team2score = None
    
    if match['team1_round_ct'] != "N/A":
        team1score = match['team1_round_ct']
    elif match['team2_round_t'] != "N/A":
        team1score = match['team2_round_t']

    if match['team2_round_ct'] != "N/A":
        team2score = match['team2_round_ct']
    elif match['team2_round_t'] != "N/A":
        team2score = match['team2_round_t']
    
    return (f"{team1score} to {team2score}")


# TODO: Parse matches.json to get live scores
'''
- Get updated json. Check if there are live matches.
- Check if it is list of teams I care about
- Grab scores and send as update to Pushover
'''
def liveMatchScores():
    liveMatch = loadJSON("live_match")

    # Loop through all the live matches
    for match in liveMatch["data"]["segments"]:
        team1 = match["team1"]
        team2 = match["team2"]
        
        # Check if the name matches teams in my stored list
        if (normalize(team1) in map(normalize, bangkokTeams) 
            or (normalize(team2) in map(normalize, bangkokTeams))):
            # Message title with the team names
            msgTitle = f"{team1} vs {team2}"
            
            # Construct message with map info, map score, match score info
            mapInfo = f"Map {match['map_number']}: {match['current_map']}" 
            mapScore = mapScoreString(match)
            msgString = f"{mapInfo} \nMap Score: {mapScore} \nMatch: {match['score1']} to {match['score2']}"

            # Call notification function with acquired information to send notification
            pushoverNotification(msgString, msgTitle)
                
            
# Call function to send notification  
liveMatchScores()
