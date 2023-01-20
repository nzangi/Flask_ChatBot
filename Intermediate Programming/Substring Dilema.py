yourString = input("Enter the word to check the repeated characters: ")


def testString(string=""):
    # initializing a substring
    subString = ""
    testList = []
    initial = 0

    for char in string:
        for i in range(initial, len(string)):
            subString += string[i]

            # checking conditions
            if subString.count(string[i]) > 1:
                testList.append(subString[:-1])
                initial += 1
                subString = ""
                break
    maxi = ""

    for word in testList:
        if len(word) > len(maxi):
            maxi = word

    if len(maxi) < 3:
        return "-1"
    else:
        return maxi


print(f"The repeated letters are: {testString(yourString)}")
