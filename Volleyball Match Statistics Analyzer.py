max_difference = 0
five_sets = 0
without_lost = 0

#Number of matches won and lost
number_of_won_matches = 0
number_of_lost_matches = 0

#total points for all matches
total_points_won = 0
total_points_lost = 0

#I defined to determine the team to consist of a max point difference.
team = "a"

total_matches = int(input("Enter number of total matches? "))
match_order = 0
for match in range(1, total_matches + 1):
    match_order += 1
    print()
    print(f"{match_order}. Match")
    name_of_opposing_team = input("Enter the name of the opposing team: ")
    #Number of sets won and lost at per matches.
    set_points_won = 0
    set_points_lost = 0
    #Total points per match.
    ttl_points_lost = 0
    ttl_points_won = 0
    #Number of sets per match.
    number_of_set = 0
    set_order = 0
    while set_points_won < 3 and set_points_lost < 3:
        set_order += 1
        print(f"{set_order}. Set")
        points_won = int(input("Enter the points won: "))
        points_lost = int(input("Enter the points lost: "))
        if points_won > points_lost:
            set_points_won += 1
        else:
            set_points_lost += 1
        number_of_set = set_points_won + set_points_lost
        ttl_points_won += points_won
        ttl_points_lost += points_lost
    if set_points_won > set_points_lost:
        number_of_won_matches += 1
    else:
        number_of_lost_matches += 1

    if number_of_set == 3:
        without_lost += 1
    if number_of_set == 5:
        five_sets += 1
    average_of_points_won = ttl_points_won / number_of_set
    average_of_points_lost = ttl_points_lost / number_of_set
    print()
    print(f"Average of points won: {average_of_points_won:.2f} \nAverage of points lost: {average_of_points_lost:.2f}")
    print(f"Total points won: {ttl_points_won} \nTotal points lost: {ttl_points_lost}")
    print(f"Number of won sets: {set_points_won} \nNumber of lost sets: {set_points_lost}")
    difference1 = ttl_points_won - ttl_points_lost
    difference2 = ttl_points_lost - ttl_points_won
    total_points_won += ttl_points_won
    total_points_lost += ttl_points_lost
    if difference1 > 0: #If the biggest difference is in a losing match, the result will be negative, for this, I defined two different variables and used if - else.
        while difference1 > max_difference:
            max_difference = difference1
            team = name_of_opposing_team
    else:
        while difference2 > max_difference:
            max_difference = difference2
            team = name_of_opposing_team


average = total_points_won / total_matches
percentage1 = without_lost / number_of_won_matches * 100 #Gives a division by zero error if all matches are lost
percentage2 = five_sets / total_matches * 100
print()
print()
print(f"Total number of points won: {total_points_won} \nAverage of points won per game: {average:.2f}")
print(f"number of matches won: {number_of_won_matches} \nnumber of matches lost: {number_of_lost_matches}")
print(f"Percentage of matches won without losing a set in all matches won: {percentage1:.2f}%")
print(f"Percentage of matches played in five sets in all matches: {percentage2:.2f}%")
print(f"The match with the highest difference in points: {team}  Difference in points: {max_difference}") #If there are two teams (The match with the highest difference in points), it will be a problem.
