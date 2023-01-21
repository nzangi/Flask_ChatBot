# solving a mastermind game
import random


# function on user input code

def user_input():
    my_guess = input("Enter your 4 digit code guess: ")
    return my_guess


# function on generating code

def generate_code():
    code_list = []

    for i in range(4):
        code = random.randrange(0, 9)
        code_list.append(code)

    return code_list


# code on playing the game

def game_play():
    generated_code = generate_code()
    i = 0

    while i < 10:
        input_code = [int(i) for i in user_input()]
        result = ""
        list = []
        if len(input_code) != 4:
            print("Enter 4 digit number")
            continue
        if input_code == generated_code:
            print(f"You guessed it right : {input_code}")

        for element in input_code:
            if element in generated_code:
                if input_code.index(element) == generated_code.index(element):
                    result = "R"
                else:
                    result = "Y"
            else:
                result = "B"

            list.append(result)
        my_list = list
        my_list = "".join(my_list)
        print(my_list)

        i += 1

    else:
        print(f"Your 10 trials are over. The guess code was {generated_code}")


# driver function
game_play()
