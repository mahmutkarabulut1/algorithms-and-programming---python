TOTAL_GAMES = 26
age = int(input("Enter Your Age = "))
annual_fee = int(input("Enter Your Last Annual Fee ($) = "))
teams_rank = int(input("Enter Your Teams Rank at The End of the Regular Sezon = "))
if teams_rank <= 8:
    number_games_playoff = int(input("Enter The Number of Games Your Team Played in the Playoff Season = "))
    cost1 = annual_fee / (TOTAL_GAMES + number_games_playoff)
    cost1 = round(cost1, 2)
    print("Your cost to your team per game you play: ", cost1)
else:
    cost2 = annual_fee / TOTAL_GAMES
    cost2 = round(cost2, 2)
    print("Your cost to your team per game you play: ", cost2)
if age < 22:
    print("You do not have the right to be released (leave your team).")
else:
    if age == 22:
        rls_fee = annual_fee * 2
    elif age == 23:
        rls_fee = annual_fee
    elif age == 24:
        rls_fee = annual_fee / 2
    else:
        rls_fee = 0
    print(f"You have the right to be released (leave your team), your release fee: ${rls_fee}")

