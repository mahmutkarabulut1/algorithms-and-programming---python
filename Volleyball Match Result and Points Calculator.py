name_of_team1 = input("Enter the name of the first team: ")
sets_won_by_the_team1 = input("Enter the number of sets won by the first team: ")
name_of_team2 = input("Enter the name of the second team: ")
sets_won_by_the_team2 = input("Enter the number of sets won by the second team: ")
if sets_won_by_the_team1 == '3' and sets_won_by_the_team2 == '0' or sets_won_by_the_team1 == '3' and sets_won_by_the_team2 == '1':
    print("The name of the team that won the match: ", name_of_team1, ", the points it earned:", "3")
    print("The name of the team that lost the match", name_of_team2, ", the points it earned: ", '0')
if sets_won_by_the_team1 == '3' and sets_won_by_the_team2 == '2':
    print("The name of the team that won the match: ", name_of_team1, ", the points it earned", "2")
    print("The name of the team that lost the match: ", name_of_team2, ", the points it earned: ", "1")
if sets_won_by_the_team2 == '3' and sets_won_by_the_team1 == '0' or sets_won_by_the_team2 == '3' and sets_won_by_the_team1 == '1':
    print("The name of the team that won the match: ", name_of_team2, ", the points it earned: ", "3")
    print("The name of the team that lost the match: ", name_of_team1, ", the points it earned: ", "0")
if sets_won_by_the_team1 == '2' and sets_won_by_the_team2 == '3':
    print("The name of the team that won the match: ", name_of_team2, ", the points it earned: ", "2")
    print("The name of the team that lost the match: ", name_of_team1, ", the points it earned: ", "1")




