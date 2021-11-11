def display_menu():
    print("==========================================================")
    print("MENU OPTIONS")
    print("==========================================================")
    print("1-Display lineup")
    print("2-Add player")
    print("3-Remove Player")
    print("4-Move player")
    print("5-Edit player position")
    print("6-Edit player stats")
    print("7-Exit program")
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("============================================================")


def display_lineup():
    if choice == 1:
        # lineup = 1
        print("Player POS AB H AVG")
        print("---------------------------------------------------------")
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player[0]} {player[1]} {player[2]}")


def add_player(numOfPlayers=3):
    if choice == 2:
        name = input("Name: ")
        pos = input("Position: ")

        while pos not in position:
            print("Incorrect position")
            pos = input("Position:")
        AB = int(input("At bats: "))
        hit = int(input("Hits: "))
        if AB != 0:
            avg = float(hit) / float(AB)
        else:
            avg = 0
        NewPlayer = [name, pos, AB, hit, avg]
        players.append(NewPlayer)
        numOfPlayers = numOfPlayers + 1
        print(name + ' was added')


def remove_player(numOfPlayers=3):
    if choice == 3:
        lineup = int(input("Lineup number:"))
        while lineup > numOfPlayers:
            print("Please enter the correct lineup number:")
            lineup = int(input("Lineup number:"))
        print("You selected " + str(players[lineup - 1][0]) + " " + str(players[lineup - 1][1]) + " " + str(
            players[lineup - 1][2]) + " " + str(players[lineup - 1][3]) + " " + str(players[lineup - 1][4]))
        del players[lineup - 1]
        numOfPlayers = numOfPlayers - 1
        print("The player with lineup number " + str(lineup) + " has been removed")


def move_player(numOfPlayers=3):
    if choice == 4:
        current_lineup = int(
            input("Current lineup number:"))

        while current_lineup < 1 or current_lineup > numOfPlayers:
            print("Please enter the correct lineup number:")
            current_lineup = int(input("Current lineup number:"))
        print("You selected " + str(players[current_lineup - 1][0]))

        new_lineup = int(input("New lineup number:"))
        while new_lineup < 1 or new_lineup > numOfPlayers:
            print("Please enter the correct lineup number:")
            new_lineup = int(input("New lineup number:"))

        (players[current_lineup - 1], players[new_lineup - 1]) = (
            players[new_lineup - 1], players[current_lineup - 1])
        print(str(players[new_lineup - 1][0]) + " was moved")


def edit_player_position():
    if choice == 5:
        lineup = int(input("Lineup number:"))
        while lineup < 1 or lineup > numOfPlayers:
            print("Please enter the correct lineup number:")
            lineup = int(input("Lineup number:"))
        print("You selected " + str(players[lineup - 1][0]) + " Pos=" + str(
            players[lineup - 1][1]))

        pos = input("Position:")

        while pos not in position:
            print("Incorrect position")
            pos = input("Position:")
        players[lineup - 1][1] = pos
        print(str(players[lineup - 1][0]) + " updated")


def edit_player_stats():
    if choice == 6:  # if choice is 6
        lineup = int(input("Lineup number:"))
        while lineup > numOfPlayers:
            print("Please enter the correct lineup number:")
            lineup = int(input("Lineup number:"))

        print("You selected " + str(players[lineup - 1][0]) + " AB=" + str(players[lineup - 1][2]) + " hits=" + str(
            players[lineup - 1][3]))
        AB = int(input("At bats:"))
        hit = int(input("Hits:"))
        players[lineup - 1][2] = AB
        players[lineup - 1][3] = hit
        if AB == 0:
            players[lineup - 1][4] = 0
        else:
            players[lineup - 1][4] = float(hit) / float(AB)
        print(str(players[lineup - 1][0]) + " updated")


def main():
    display_menu()
    global position
    position = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
    # creating a tuple for storing valid positions
    global choice
    # choice = int(input("Enter your choice: "))
    global lineup
    lineup = 1  # lineup to take the lineup number from user
    global numOfPlayers
    numOfPlayers = 3
    global players
    players = [["Joe", "P", 10, 2, 0.2],
               ["Tom", "SS", 11, 4, 0.364],
               ["Ben", "3B", 0, 0, 0.0]]

    while True:

        choice = int(input("Enter menu option:"))
        if choice == 1:
            display_lineup()
        elif choice == 2:
            add_player()
        elif choice == 3:
            remove_player()
        elif choice == 4:
            move_player()
        elif choice == 5:
            edit_player_position()
        elif choice == 6:
            edit_player_stats()
        else:
            print("Good Bye\n")

            break


if __name__ == "__main__":
    main()
