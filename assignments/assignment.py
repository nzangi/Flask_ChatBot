from past.builtins import raw_input

players = [['Joe', 'P', 10, 2, 0.2], ['Tom', 'SS', 11, 4, 0.364],
           ['Ben', '3B', 0, 0, 0.0]]  # creating an list of lists with few playes information
position = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')  # creating a tuple for storing valid positions
choice = 0  # choice variable for taking user's menu choice
lineup = 1  # lineup to take the lineup n from user
numOfPlayers = 3  # to keep hold on the n of players

print("=" * 64)
print("\t\tBaseball Team Manager")
print("MENU OPTIONS")  # display the menu
print("1-Display lineup")
print("2-Add player")
print("3-Remove Player")
print("4-Move player")
print("5-Edit player position")
print("6-Edit player stats")
print("7-Exit program")
# display the positions
print("\nPOSITIONS:")

for i in range(len(position)):
    if i < len(position) - 1:
        print(position[i] + ","),
    else:
        print(position[i])

# print("="*64)
while choice != 7:  # loop till the choice of user is not equal to 7
    try:
        choice = int(raw_input("\nMenu Option:"))
        # take user's menu option in variable choice
        if choice == 1:  # if choice is 1
            lineup = 1
            print("Player POS AB H AVG")
            print("-" * 30)
            for player in players:  # loop through the list and display each players' information
                print(str(lineup)),
                for item in player:
                    print(str(item) + " "),
                lineup = lineup + 1
                print("")

        elif choice == 2:  # if the user's choice is 2
            name = raw_input("Name: ")  # take name and position from user
            pos = raw_input("Position: ")

            while pos not in position:  # if user is provided valid position
                print("Incorrect position")
                pos = raw_input("Position:")
            AB = int(raw_input("At bats: "))  # take at bats and hits value from user
            hit = int(raw_input("Hits: "))
            if AB != 0:  # if at bats is not 0, set avg as hits / at bats
                avg = float(hit) / float(AB)  # else set avg as 0
            else:
                avg = 0
            NewPlayer = [name, pos, AB, hit, avg]  # create a list as newPlayer, and update the list with new info
            players.append(NewPlayer)  # append the list newplayer to players list
            numOfPlayers = numOfPlayers + 1  # increment n of players by 1
            print(name + ' was added')

        elif choice == 3:  # if choice is 3
            lineup = int(raw_input("Lineup n:"))  # take lineup n from user
            while lineup > numOfPlayers:  # if lineup n is greater than n of player
                print(
                    "Please enter the correct lineup n:")  # then show appropriate info and again ask for lineup n
                lineup = int(raw_input("Lineup n:"))  # display the player's information with specified lineup
            print("You selected " + str(players[lineup - 1][0]) + " " + str(players[lineup - 1][1]) + " " + str(
                players[lineup - 1][2]) + " " + str(players[lineup - 1][3]) + " " + str(players[lineup - 1][4]))
            del players[lineup - 1]  # delete the player with specified lineup
            numOfPlayers = numOfPlayers - 1  # decrement num of players by 1
            print("The player with lineup n " + str(lineup) + " has been removed")

        elif choice == 4:  # if choice is 4
            current_lineup = int(
                raw_input("Current lineup n:"))  # take current lineup from user and print the player's info

            while current_lineup < 1 or current_lineup > numOfPlayers:  # show appropriate message and again ask for lineup if incorrect
                print("Please enter the correct lineup n:")  # lineup is provided
                current_lineup = int(raw_input("Current lineup n:"))
            print("You selected " + str(players[current_lineup - 1][0]))

            new_lineup = int(raw_input("New lineup n:"))  # take new lineup from user
            while new_lineup < 1 or new_lineup > numOfPlayers:  # show appropriate message and again ask for lineup if incorrect
                print("Please enter the correct lineup n:")  # lineup is provided
                new_lineup = int(raw_input("New lineup n:"))

            (players[current_lineup - 1], players[new_lineup - 1]) = (
            players[new_lineup - 1], players[current_lineup - 1])
            print(str(players[new_lineup - 1][0]) + " was moved")


        elif choice == 5:  # if choice is 5
            lineup = int(raw_input("Lineup n:"))  # take line up from user
            while lineup < 1 or lineup > numOfPlayers:  # show appropriate message and again ask for lineup if incorrect
                print("Please enter the correct lineup n:")  # lineup is provided
                lineup = int(raw_input("Lineup n:"))
            print("You selected " + str(players[lineup - 1][0]) + " Pos=" + str(
                players[lineup - 1][1]))  # show player's information

            pos = raw_input("Position:")  # Ask the position to change

            while pos not in position:  # get appropriate position, if incorrect position is specified
                print("Incorrect position")
                pos = raw_input("Position:")
            players[lineup - 1][1] = pos  # update the player's information with new position
            print(str(players[lineup - 1][0]) + " updated")

        elif choice == 6:  # if choice is 6
            lineup = int(raw_input("Lineup n:"))  # take correct lineup n from user
            while lineup > numOfPlayers:
                print("Please enter the correct lineup n:")
                lineup = int(raw_input("Lineup n:"))

            print("You selected " + str(players[lineup - 1][0]) + " AB=" + str(players[lineup - 1][2]) + " hits=" + str(
                players[lineup - 1][3]))
            AB = int(raw_input("At bats:"))  # take the value of at bats and hits from user
            hit = int(raw_input("Hits:"))
            players[lineup - 1][2] = AB  # update the player's information with new at bats and hots
            players[lineup - 1][3] = hit
            if AB == 0:  # also calculate average and update
                players[lineup - 1][4] = 0
            else:
                players[lineup - 1][4] = float(hit) / float(AB)
            print(str(players[lineup - 1][0]) + " updated")

        elif choice == 7:  # if choice is 7, print break and come out of the loop
            print("Bye!")

    except ValueError:
        print('Not a valid option. Please try again')
        print("\nMENU OPTIONS")  # display the menu
        print("1-Display lineup")
        print("2-Add player")
        print("3-Remove Player")
        print("4-Move player")
        print("5-Edit player position")
        print("6-Edit player stats")
        print("7-Exit program")