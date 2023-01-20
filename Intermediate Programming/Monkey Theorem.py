import random


#Generate a random string

def generateString(stringLength):

    #decleare string with all aphabets and strings
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(stringLength):
        result += alphabets[random.randrange(27)]

    return  result

#function to determine the score of the generated string
def score(goalString, testString):
    letterSame = 0
    for i in range(len(goalString)):
        if goalString[i] == testString[i]:
            letterSame = letterSame + 1
    accuracy = (letterSame / len(goalString)*100)
    accuracy = round(accuracy)
    return accuracy

#main fuctions to call the 2 functions
def main():
    goalString = "a computer science portal for gigs"
    newString = generateString(35)
    best = 0
    newScore = score(goalString,newString)
    while newScore < 100:
        if newScore > best:
            best = newScore
            print(newString)
            print(best)
        newString = generateString(35)
        newScore = score(goalString, newString)
    print(goalString)
    print(best)

#briver code
main()



