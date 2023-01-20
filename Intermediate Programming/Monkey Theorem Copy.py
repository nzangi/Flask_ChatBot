import random
#function to generate a string
def generateNewString(lengString):
    letters = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(lengString):
        result += letters[random.randrange(27)]
    return result

#function to calculate the score

def calculateScore(stringGoal,stringTest):
    sameLetters = 0
    for i in range(len(stringTest)):
        if stringGoal[i] == stringTest[i]:
            sameLetters += 1
    sameLetters = round(sameLetters,2)

    return sameLetters

#main function to call the 2 functions

def main():
    goalString = "a computer science portal for geeks"
    stringNew = generateNewString(35)
    score = 0
    newScore = calculateScore(goalString,stringNew)
    while newScore < 100:
        if newScore > score:
            score = newScore
            print(stringNew)
            print(score)
        stringNew = generateNewString(35)
        newScore = calculateScore(goalString,stringNew)

main()