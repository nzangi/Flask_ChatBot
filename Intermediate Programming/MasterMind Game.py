import random


# get input
def user_code():
    input_code = input("Enter the 4 digit code to play the game: ")
    return input_code


# generate code
def generate_code():
    generate_code = []

    for i in range(4):
        value = random.randrange(0, 9)
        generate_code.append(value)
    return generate_code


# play the mind game
def play_game():
    generate_mycode = generate_code()
    i = 0
    while i < 10:
        result = ""
        myGuesscode = []
        # change the string into int form
        user_input_code = [int(c) for c in user_code()]

        if len(user_input_code) != 4:
            print("Enter a 4 digit value")
            continue

        if user_input_code == generate_mycode:
            print(f"You guessed it right: {generate_mycode}")
            break

        for element in user_input_code:
            if element in generate_mycode:
                if user_input_code.index(element) == generate_mycode.index(element):
                    result = "R"
                else:
                    result = "Y"
            else:
                result = "B"

            myGuesscode.append(result)

            my_result = "".join(myGuesscode)

        print(my_result)
        i += 1

    else:
        print(f"You have ran out of your 10 trays ! {generate_mycode}")


# driver function
play_game()
