def list(player_list):
    if len(player_list) == 0:
        print("There are no movies in the myList.\n")
        return
    else:
        for i, player in enumerate(player_list, start=1):
            print(f"{i}. {player[0]} ({player[1]}) @ {player[2]}")
        print()


def add(player_list, calculate_batting_average):
    name = input("Name: ")
    position = input("Position: ")
    at_bats = input("At bats: ")
    hits = input("Hits: ")
    


def delete(player_list):
    number = int(input("Number: "))
    if number < 1 or number > len(player_list):
        print("Invalid movie n.\n")
    else:
        player = player_list.pop(number - 1)
        print(player[0] + " was deleted.\n")


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

def calculate_batting_average():
    print("Welcome to the batting average calculator \n")
    at_bats = int(input("Enter n of at bats: "))  # initialize at_bats and store user entry
    while at_bats <= 0:
        print("invalid n of bats")
        at_bats = int(input("Enter n of at bats: "))

    hits = int(input("Enter n of hits: "))  # initialize  n of hits store user entry
    # calculate the average and round to three decimal places
    while hits > at_bats or hits < 0:
        print('Invalid Number of hits. It should be positive and can not be more than n of bats.')
        hits = int(input("Number of hits: "))
    avg = hits / at_bats
    avg = round(avg, 3)
    print("The average is: ", avg)
    print()


def main():

    player_list = [["Joe", "P", 10, 2, 0.2],
                   ["Tom", "SS", 11, 4, 0.364],
                   ["Ben", "3B", 0, 0, 0.0],
                   ["Mike" "C", 0, 0, 0.0]]
    position = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
    display_menu()

    while True:  # loop for entire program
        x = int(input("Enter menu option:"))
        if x == 1:
            list(player_list)
        elif x == 2:
            add(player_list, calculate_batting_average)
        elif x == 3:
            delete(player_list)
        elif x == 4:

            break
        else:
            print("Invalid Entry... Please try again \n")


if __name__ == "__main__":
    main()

