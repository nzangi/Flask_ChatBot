# Class question to store question and answers
import random


class Question:
    ques = ""
    answer = ""

    def __init__(self, q, a):  # constructor
        self.ques = q
        self.answer = a


if __name__ == "__main__":
    # Formatting quiz menu
    # ques = ""
    print("Welcome to QUIZ MENU, please enter the quiz questions")
    numq = input("How many questions do you want to enter?")
    questions = []  # List to score questions
    leaderboard = {}  # Dictionary to store user scores
    # looping to take question inputs, we can take any number of questions
    for i in range(1, int(numq) + 1):
        while True:
            print("Enter question {0}:".format(i))
            q = str(input())
            if q == "":
                print("Please enter a valid question")
                continue
            ans = str(input("Enter the answer for above question: "))
            if ans == "":
                print("Please enter a valid answer")
                continue

            questions.append(Question(q, ans))

            break
    print("Questions entered successfully, Starting Quiz")
    # loop for user answers
    while True:
        # shuffling our questions
        random.shuffle(questions)
        name = str(input("Enter your name: "))
        if name == "":
            print("Name cannot be empty")
            continue
        else:
            leaderboard[name] = 0
            i = 1
            # nested loop to keep asking the same user questions
            while True:

                if i > len(questions):
                    break
                print("Question {0}: {1}".format(i, questions[i - 1].ques))
                z = str(input("Ans: "))
                if z == "":
                    print("Enter a valid answer")
                    continue
                elif z == questions[i - 1].answer:
                    print("Your answer was correct +1 point")
                    leaderboard[name] += 1
                    i += 1
                    continue
                else:
                    print("wrong answer")
                    i += 1
                    continue
        print("=========Quiz Over========")
        # print("Your Score is {0}/{1}({2}%)").format(leaderboard[name], Question(len(ques)))
        print(f"Correct answers {i}")
        print(len(questions))

        print(leaderboard[name])

        x = (leaderboard[name] / len(questions))  * 100
        # print(f"Your Score is ")
        print(f"Your Score is {leaderboard[name],len(questions)} ({x})%")

        again = str(input("Do you want to play again Y/N: "))
        if again == "Y":
            continue
        elif again == "N":
            break
        else:
            print("Invalid input Quitting game")
            break
    # using lambda expression to find the highest score
    dicmax = max(leaderboard, key=lambda x: leaderboard[x])
    print("Top Score => {0} : {1}/10".format(dicmax, leaderboard[dicmax]))
    total_score = 0
    for i in leaderboard.values():
        total_score += i
    avg = total_score / len(leaderboard)
    print("Average score of all users is {0}/10".format(avg))
