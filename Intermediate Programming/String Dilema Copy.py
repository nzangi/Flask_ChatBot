# user input string

yourLetter = input("Enter your letter to check your repeated words: ")


def stringDilema(string=""):
    subString = ""
    listTest = []
    initialLetter = 0

    # illitearing the string
    for character in string:
        for i in range(initialLetter, len(string)):
            subString += string[i]

            if subString.count(string[i]) > 1:
                listTest.append(subString[:-1])

                initialLetter += 1
                subString = ""
                break

    maxi = ""
    # check the longest word in the list
    for word in listTest:
        if len(word) > len(maxi):
            maxi = word
    # checking if the longest word is less than 3
    if len(maxi) < 3:
        return "-1"
    else:
        return maxi


print(f"The non repeated character in the string of {yourLetter} is : {stringDilema(yourLetter)}")
