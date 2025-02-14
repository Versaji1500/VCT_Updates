import requests
import json


def importVLRJSON() :
    # API URL where the information is hosted
    url = "https://vlr.orlandomm.net/api/v1/matches"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Get the API response as JSON
        with open("matches.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)  # Save to a JSON file with indentation
        print("Data saved to matches.json")
    else:
        print("Error:", response.status_code)
