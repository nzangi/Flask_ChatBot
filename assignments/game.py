# solution includes the following

# Python Code Snippet
# Python Code Screen Shot
# Output Screen Shot
# Python Code Snippet:

# game type declaration
def game():
    # game Variable called gameFileName
    gameFileName = "tic_tac.txt"

    # game constructor with optional Parameters
    def __init__(self, title="", playerLastName="", gameDate="", playingDate="", wins='', price=0.0):
        # Set the game details
        self._title = title
        self._playerLastName = playerLastName
        self._playingDate = playingDate
        self._wins = wins

    # Get the title
    def getTitle(self):
        return self._title

    # Get the player last name
    def getplayerLastName(self):
        return self._playerLastName

    # Get the game date
    def getgameDate(self):
        return self._gamingDate

    # Get the n of wins
    def getwins(self):
        return str(self._wins)

    # Print the string
    def __str__(self):
        printLine = self.getTitle() + ", " + self.getplayerLastName() + ", " + self.getgamingDate() + ", " + self.getwins()
        return printLine

    # Function to write from the file.txt
    def writeToFile(self, fileName):
        playersFile = open(fileName, 'a')
        # Write the header line
        playersFile.write(self.__str__() + "\n")
        playersFile.close()

    # Function to read from the file.txt
    def readFromFile(self, fileName):
        gameList = []
        try:
            file = open(fileName, "r")
            # Read the contents of the file.txt using the read() and split based on new lines using splitlines()
            lines = file.read().splitlines()
            for line in lines:
                self._title, self._playerLastName, self._gamingDate, self._wins, gameType = line.split(",")
                gameList.append([self._title, self._playerLastName, self._gamingDate, self._wins, gameType])
            return gameList
        # Exception handling if file.txt is not found
        except FileNotFoundError:
            print("{} NOT FOUND!".format(fileName))
            print(
                "Kindly ensure the input file.txt is in the same location where the Python program is running and try again")
            return []
        except Exception as ex:
            print("File open error")
            print(ex)
            print(
                "Kindly ensure the input file.txt is in the same location where the Python program is running and try again")
            print("Exiting the program - Execution Terminated !!!")
            return []


# random matches
def random(players):
    def __init__(self, title="", playerLastName="", gameDate="", gamingDate='', price='', wins=0.0):
        # Set the styleofplay(tic-tac)
        self.gameType = "random"

        # max natches
        super().__init__(title, playerLastName, gamingDate, price)

    # String representation for gaming object
    def __str__(self):
        printLine = super().__str__() + ", " + self.gameType
        return printLine


def cmax_max(players):
    def __init__(self, title="", playerLastName="", gamingDate="", wins='', price=0.0):
        # Set the gameType
        self.gameType = "tic-tac"

        # Call the game constructor
        super().__init__(title, playerLastName, gamingDate, wins)

    # String representation for Hardcover class object
    def __str__(self):
        printLine = super().__str__() + ", " + self.gameType
        return printLine


# Function to check if n entered is a valid n
def isValidNumber(number):
    try:
        number = float(number)
        if number < 0:
            print("Only positive numbers are allowed")
            return False
        else:
            return True
    except ValueError:
        print("Entered value is not a valid n")
        return False


# Add a game
def addgame():
    title = input("Enter the game title: ")
    lastName = input("Enter the player last name: ")
    gamingDate = input("Enter the gaming date: ")
    validPrice = False
    while (validPrice == False):
        price = input("Enter the price of the game: ")
        if isValidNumber(price):
            validPrice = True
        else:
            validPrice = False
    gameType = input("1 - For max games \n2 - random games\nEnter your choice: ")
    if gameType not in ["1", "2"]:
        print("Invalid game type entered.Defaulting the game type to random game")
        gameType = "1"
    if gameType == "1":
        hcgame1 = (title, lastName, gamingDate, price)
        hcgame1.writeToFile(game.gameFileName)
        print("game added successfully")
    elif gameType == "2":
        scgame1 = (title, lastName, gamingDate, price)
        scgame1.writeToFile(game.bookFileName)
        print("game added successfully")


# View a book
def viewgame():
    # Declare the game object
    game()
    # Call the readFromFile() function to get the myList of games
    gameList = game.readFromFile(game.gameFileName)
    gameFound = False
    # Get the author name from the user
    searchLastName = input("Enter the player last name: ")
    # Check if the author name is present in the game details, if yes print the details
    for gameDetail in gameList:
        title = gameDetail[0]
        authorLastName = gameDetail[1]
        gamingDate = gameDetail[2]
        price = gameDetail[3]
        gameType = gameDetail[4]
        if searchLastName.lower() in playerLastName.lower():
            bookFound = True
            print("Title: {}, Author Name: {}, gaming Date: {}, Price: {}, game Type: {}".format(title, playerLastName,
                                                                                                 gamingDate, price,
                                                                                                 gameType))
    if gameFound == False:
        print("game with author name {} not found?.".format(searchLastName))


def main():
    exitProcessing = False
    # Add, View, Exit based on the user choice
    while (exitProcessing == False):
        User_Choice = input("\n1 - Add a game\n2 - View a game\n3 - Exit\enter your choice: ")
        if (User_Choice == "1"):
            # Call the add game () function
            addgame()
            exitProcessing = False
        elif (User_Choice == "2"):
            # Call the view game () function
            viewgame()
            exitProcessing = False
        elif (User_Choice == "3"):
            print("You choose to exit. Good Bye have a nice day!!!")
            exitProcessing = True
        else:
            print("Invalid choice entered. Enter a valid choice")
            exitProcessing = False


# Standard way to call the Python main
if __name__ == '__main__':
    main()
