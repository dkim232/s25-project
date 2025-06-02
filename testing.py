import json

with open("mlb.json") as file:
    data = json.load(file)


for game in data:
    if game['away_team'] != "Los Angeles Angels":
        continue
    print(f"\nGame: {game['away_team']} at {game['home_team']}")
    print(f"Start time: {game['commence_time']}")

    for bookmaker in game["bookmakers"]:
        print(f"\n  Bookmaker: {bookmaker['title']}")

        for market in bookmaker["markets"]:
            if market['key'] != "h2h":
                continue

            print(f"        Market: {market['key']}")
            
            for outcome in market["outcomes"]:
                team = outcome["name"]
                price = outcome["price"]
                #point = outcome.get("point", "N/A")
                print(f"            {team} | Price: {price}")