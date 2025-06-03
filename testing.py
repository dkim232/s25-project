import json

with open("mlb.json") as file:
    data = json.load(file)


for game in data:
    if game['away_team'] != "Los Angeles Angels":
        continue
    # print(f"\nGame: {game['away_team']} at {game['home_team']}")
    # print(f"Start time: {game['commence_time']}")

    best_odds = {}

    for bookmaker in game["bookmakers"]:
        # print(f"\n  Bookmaker: {bookmaker['title']}")

        for market in bookmaker["markets"]:
            if market['key'] != "h2h":
                continue

            # print(f"        Market: {market['key']}")
            
            for outcome in market["outcomes"]:
                team = outcome["name"]
                price = outcome["price"]
                #point = outcome.get("point", "N/A")
                #print(f"            {team} | Price: {price}")
                if team not in best_odds or (price > best_odds[team]['price']):
                    best_odds[team] = {
                        "price" : price,
                        "bookmaker" : bookmaker["title"],
                        "date" : game["commence_time"]
                    }

    if len(best_odds) == 2:
        team1, team2 = list(best_odds.keys())
        odds1 = best_odds[team1]["price"]
        odds2 = best_odds[team2]["price"]

        imp_sum = (odds1 + odds2) / (odds1 * odds2)

        if imp_sum < 1:
            profit = (1 - imp_sum) * 100
            print("Arbitrage Opportunity Found!\n")
            # print(f"Best Odds: {team1} @ {odds1}, {team2} @ {odds2}")
            # print(f"Sum of implied probability: {imp_sum:.4f}")
            # print(f"Profit Margin: {profit:.2f}%")
            print(f"""Place bet on {game['away_team']} at {game['home_team']} on {best_odds[team1]["date"]}
            Bet on {team1} at {best_odds[team1]['bookmaker']}
            Bet on {team2} at {best_odds[team2]['bookmaker']} 
            Guaranteed profit of {profit:.2f}%!""")

        else:
            print("\nNo more arbitrage opportunities found.")