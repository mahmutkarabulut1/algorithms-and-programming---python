MIN_PLAYING_FIELD = 4
MAX_PLAYING_FIELD = 8
FOR_PLAYING_FIELD_FORMULA = 4
MIN_STONE=2

def display_letters(playing_field,letters_list):#printing letters on top and bottom of the playing fields
    print(end="    ")
    for i in range(playing_field):
        print(f"{letters_list[i]:3}", end=" ")
def display_playing_field(playing_field,letters_list,numbers_list,stone_location,player1,player2): #printing playing field
    display_letters(playing_field,letters_list)
    print()
    print(end="  ")
    print((playing_field*FOR_PLAYING_FIELD_FORMULA+1)*"-")
    for column in range(0,playing_field):
        print(numbers_list[column],end=" ")
        for row in range(playing_field):
            print("|",end="")
            if stone_location[column][row]==1:#printing player1 stones
                print(end=" ")
                print(player1,end=" ")
            elif stone_location[column][row]==-1:#printing player2 stones
                print(end=" ")
                print(player2,end=" ")
            else:#printing empty stones
                print("   ",end="")
        print("|",end=" ")
        print(column+1)
        print(end="  ")
        print((playing_field * FOR_PLAYING_FIELD_FORMULA + 1) * "-")
    display_letters(playing_field,letters_list)
    print()
def controlls(player_name,numbers_list,letters_list,stone_location,new_location):#controlling invalid movements
    remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()

    while 1:
        while 1:

            if (remove[0] == add[0] and remove[1] == add[1]):  # Preventing player's movement on to same block it has already on
                print("You are already at the position you want to move! Please try to move another position.")
                remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()


            elif stone_location[numbers_list.index(remove[0])][letters_list.index(remove[1])] == 0 or stone_location[numbers_list.index(remove[0])][letters_list.index(remove[1])] == -new_location:  # Preventing empty block movement and rival block movement
                print("You can only play your own stones! There isn't any stone of yours in that block. ")
                remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()

            elif (remove[0] != add[0] and remove[1] != add[1]):  # Preventing movements other than vertical and horizontal
                print("You can only move vertically and horizontally!")
                remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()
            else:
                break
        # Controlling from up to down
        if (remove[1] == add[1] and numbers_list.index(remove[0]) < numbers_list.index(add[0])):
            for i in range(numbers_list.index(remove[0])+1, numbers_list.index(add[0])+1):
                if stone_location[i][letters_list.index(add[1])] != 0:
                    print("You can only move to empty blocks and you can't jump over the stones.")
                    remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()
                    break
            else:
                break
        # Controlling from down to up
        elif (remove[1] == add[1] and numbers_list.index(add[0]) < numbers_list.index(remove[0])):
            for i in range(numbers_list.index(add[0]), numbers_list.index(remove[0])):
                if stone_location[i][letters_list.index(add[1])] != 0:
                    print("You can only move to empty blocks and you can't jump over the stones.")
                    remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()
                    break
            else:
                break
        # Controlling from right to left
        elif (remove[0]==add[0] and letters_list.index(add[1])<letters_list.index(remove[1])):
            for i in range(letters_list.index(add[1]), letters_list.index(remove[1]) ):
                if stone_location[numbers_list.index(add[0])][i] != 0:
                    print("You can only move to empty blocks and you can't jump over the stones.")
                    remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()
                    break
            else:
                break
        # Controlling from left to right
        elif (remove[0]==add[0] and letters_list.index(remove[1])<letters_list.index(add[1])):
            for i in range(letters_list.index(remove[1])+1,letters_list.index(add[1])+1 ):
                if stone_location[numbers_list.index(add[0])][i] != 0:
                    print("You can only move to empty blocks and you can't jump over the stones.")
                    remove, add = input(f"Player {player_name}, please enter the position of your own stone you want to move and the target position:").split()
                    break
            else:
                break
    return remove, add
def stone_moves(new_location,player_name,numbers_list,letters_list,stone_location):#moving the stones
    while 1:
        try:#Controlling invalid input
            remove, add = controlls(player_name, numbers_list, letters_list, stone_location,new_location)
            remove=" ".join(remove)
            remove=remove.split()
            stone_location[numbers_list.index(remove[0])][letters_list.index(remove[1])]=0#Using the index of the given string to remove stone
            add=" ".join(add)
            add=add.split()
            stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]=new_location#Using the index of the given string to add stone,new_location is 1 for player1 and -1 for player2
            break
        except:
            print("It is not a valid movement! Please enter the position of your own stone you want to move and the target position again. ")

    return stone_location,add
def lock_stones(stones, location_no, add,stone_location,numbers_list,letters_list,playing_field):#locking stones
    for i in [-1,1]: #Removing locked stones except the corner blocks
        try:
            if stone_location[numbers_list.index(add[0])][letters_list.index(add[1])+i] == location_no:
                if stone_location[numbers_list.index(add[0])][letters_list.index(add[1])+2*i] == -location_no and letters_list.index(add[1])+2*i>=0:
                    stone_location[numbers_list.index(add[0])][letters_list.index(add[1]) + i] = 0
                    print(f"The stone at position {numbers_list[numbers_list.index(add[0])]}{letters_list[letters_list.index(add[1]) + i]} was locked and removed.")
                    stones -= 1

        except IndexError:
            pass
        try:
            if stone_location[numbers_list.index(add[0])+i][letters_list.index(add[1])] == location_no:
                if stone_location[numbers_list.index(add[0])+2*i][letters_list.index(add[1])] == -location_no and numbers_list.index(add[0])+2*i>=0:
                    stone_location[numbers_list.index(add[0])+i][letters_list.index(add[1])] = 0
                    print(f"The stone at position {numbers_list[numbers_list.index(add[0])+i]}{letters_list[letters_list.index(add[1])]} was locked and removed.")
                    stones -= 1
        except IndexError:
            pass
    #Removing locked stones on corner blocks
    try:
        if stone_location[0][1] ==stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[0][0] == location_no and stone_location[1][0] == -location_no:
                stone_location[0][0] = 0
                print(f"The stone at position 1A was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[1][0] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[0][0] == location_no and stone_location[0][1] == -location_no:
                stone_location[0][0] = 0
                print(f"The stone at position 1A was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[0][playing_field-2] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[0][playing_field-1] == location_no and stone_location[1][playing_field-1] == -location_no:
                stone_location[0][playing_field - 1] = 0
                print(f"The stone at position 1{letters_list[playing_field-1]} was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[1][playing_field-1] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[0][playing_field-1] == location_no and stone_location[0][playing_field-2] == -location_no:
                stone_location[0][playing_field - 1] = 0
                print(f"The stone at position 1{letters_list[playing_field-1]} was locked and removed.")
                stones -= 1
    except IndexError:
        pass

    try:
        if stone_location[playing_field - 1][1] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[playing_field -1][0] == location_no and stone_location[playing_field - 2][0] == -location_no:
                stone_location[playing_field - 1][0] = 0
                print(f"The stone at position {numbers_list[playing_field-1]}A was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[playing_field-2][0] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[playing_field -1][0] == location_no and stone_location[playing_field - 1][1] == -location_no:
                stone_location[playing_field - 1][0] = 0
                print(f"The stone at position 1{letters_list[playing_field-1]} was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[playing_field - 1][playing_field -2] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[playing_field - 1][playing_field -1] == location_no and stone_location[playing_field - 2][playing_field -1] == location_no:
                stone_location[playing_field - 1][playing_field - 1] = 0
                print(f"The stone at position {numbers_list[playing_field-1]}{letters_list[playing_field-1]} was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    try:
        if stone_location[playing_field - 2][playing_field -1] == stone_location[numbers_list.index(add[0])][letters_list.index(add[1])]:
            if stone_location[playing_field - 1][playing_field -1] == location_no and stone_location[playing_field - 1][playing_field -2] == -location_no:
                stone_location[playing_field - 1][playing_field - 1] = 0
                print(f"The stone at position {numbers_list[playing_field-1]}{letters_list[playing_field-1]} was locked and removed.")
                stones -= 1
    except IndexError:
        pass
    return stone_location,stones
def play(stone1,stone2,player1,player2,numbers_list,letters_list,stone_location,playing_field,add):

    display_playing_field(playing_field, letters_list, numbers_list, stone_location, player1, player2)
    while(stone1>=MIN_STONE or stone2>=MIN_STONE):
        stone_location,add = stone_moves(1,player1,numbers_list,letters_list,stone_location)
        stone_location,stone2 = lock_stones(stone2,-1,add,stone_location,numbers_list,letters_list,playing_field)
        display_playing_field(playing_field,letters_list,numbers_list,stone_location,player1,player2)
        if stone2 == 1:
            break
        stone_location,add = stone_moves(-1,player2,numbers_list,letters_list,stone_location)
        stone_location,stone1 = lock_stones(stone1, 1,add,stone_location,numbers_list,letters_list,playing_field)
        display_playing_field(playing_field,letters_list,numbers_list,stone_location,player1,player2)
        if stone1 == 1:
            break
    if stone1 == 1:
        player = player2
    else:
        player = player1
    print(f"Player {player} won the game.")
def new_game(player1,player2):
    numbers_list = ["1","2","3","4","5","6","7","8"]
    letters_list = ["A","B","C","D","E","F","G","H"]
    add = []

    while 1:
        try:
            playing_field = int(input("Enter the row/column number of the playing field(4-8): "))
            while playing_field < MIN_PLAYING_FIELD or playing_field>MAX_PLAYING_FIELD:
                playing_field = int(input("Playing field must be between 4 and 8. Please enter the row/column number of the playing field(4-8) again:"))
            break
        except:
            print("You must enter an integer.")


    stone1 = playing_field
    stone2 = playing_field

    stone_location = []
    for i in range(playing_field):
        stone_location.append([0] * playing_field)

    for j in range(playing_field):
        stone_location[0][j] = -1
        stone_location[playing_field - 1][j] = 1

    play(stone1,stone2,player1,player2,numbers_list,letters_list,stone_location,playing_field,add)

    play_again = input("Would you like to play again(Y/N)?")
    while(play_again not in ["y","Y","n","N"] ):
        print("Your answer should be one of these:Y, y, n, N.")
        play_again = input("Would you like to play again(Y/N)?")
    if play_again == "Y" or play_again=="y":
        new_game(player1,player2)
    else:
        print("Game Over")
def main():

    player1=input("Enter a character to represent player 1: ")
    while len(player1) != 1 or "Z"<player1 or  player1<"A":
        player1 = input("Character must be one capital letter from English alphabet. Please enter a character to represent player 1 again: ")

    player2=input("Enter a character to represent player 2: ")
    while len(player2) != 1 or "Z"<player2 or player2<"A":
        player2 = input("Character must be one capital letter from English alphabet. Please enter a character to represent player 2 again: ")

    while(player1==player2):
        print("Player 1 and player 2 must be represented by different characters. ")
        player2 = input("Enter a character to represent player 2: ")
        while len(player2) != 1 or "Z" < player2 or player2 < "A":
            player2 = input("Character must be one capital letter from English alphabet. Please enter a character to represent player 2 again: ")

    new_game(player1,player2)

main()
