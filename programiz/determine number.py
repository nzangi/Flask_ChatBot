'''# Leap year
year = int(input("Enter the year which you need to check if its is leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"This year {year} it is a leap year")
        else:
            print(f"The year {year} it is not a leap year")
    else:
        print(f"This year {year} it is a leap year")
else:
    print(f"The year {year} it is not a leap year")

# Loop in Python
list_number = int(input("Enter the numbers you want for your list: "))
your_lists = []

for i in range(list_number):
    your_list = input(f"Enter number {i+1} item for your list: ")
    your_lists.append(your_list)
print(your_lists)

for your_list in your_lists:
    print(f"Your list contains the following {your_list}")
    for letter in your_list:
        print(f"Your list contains the following letters: {letter}")
    '''

# print("Twikle, twikle, twikle little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\nTwikle ,twikle,twikle little star,\n\tHow I wonder who you are")


# from platform import python_version
#
# print("The current version of python is: ", python_version())
#
# import datetime
# now = datetime.datetime.now()
# print(f'Current Datetime: {now.strftime("%Y-%m-%d %H:%M:%S")}')
# from math import pi
# radius = float(input("Enter the radius of the circle: "))
# area = pi * (radius **2)
# print(f"The area of the circle is: {area}")
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# fullname = first_name+" "+last_name
# print(f"The revered order of name {fullname} is: {fullname[::-1]}")
# values = input("Enter number of comma separated numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print(f"List: {list}")
# print(f"Tuple: {tuple}")
# filename = input("Enter the Input file: ")
# file_extension = filename.split(".")
# print(f"The Output file is: {file_extension[-1]}")
# color_list = ["Red","Green","White","Black"]
# print(f"The first color is: {color_list[0]} and last color is: {color_list[-1]}")

# exam_date = (11, 12, 2015)
# print("The examination will start on: %i / %i / %i " %exam_date)
#
# exam_st_date = (11,12,2014)
# print("The examination will start from : %i / %i / %i" %exam_st_date)

# import calendar
# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# print(calendar.month(year,month))

# from datetime import date
# date_one = date(2014, 7, 2)
# date_two = date(2014, 7, 11)
# difference_in_days = date_two-date_one
# print(f"The difference between {date_two} and {date_one} is {difference_in_days.days} days")

# from math import pi
# radius = int(input("Enter the radius of the sphere: "))
# volume = 4/3 * pi * (radius**3)
# print(f"The volume of the sphere with radius of {radius} is : {volume}")

# number = int(input("Enter the number to check the difference: "))
#
#
# def minus(number):
#     difference = number - 17
#     if number > 17:
#         new_difference = 2 * difference
#         print(f"The difference is: {new_difference}")
#     else:
#         print(f"The difference is : {difference}")
#
#
# minus(number)
#
# number_1 = int(input("Enter the first value: "))
# number_2 = int(input("Enter the second number: "))
# number_3 = int(input("Enter the third number: "))
#
# def addition(number_one, number_two,number_three):
#     if number_one == number_two == number_three:
#         sum = number_two + number_three + number_one
#         sum_total = sum * 2
#
#     else:
#         sum_total = number_two + number_three + number_one
#
#     return sum_total
# print(f"The sum of the three numbers {number_1},{number_2},{number_3} is : {addition(number_1,number_2,number_3)}")

# my_string = input("Enter the string: ")
#
#
# def strings(string):
#     if len(string) >= 2 and string[:2] == "Is":
#         return string
#     return "Is" + string
#
#
# print(f"The new string is: {strings(my_string)}")

# words = input("Enter the word: ")
# copies = int(input("Enter the number of copes which one needs: "))
#
#
# def larger_string(string, numbers):
#     result = ""
#     for i in range(numbers):
#         result = result + string
#     return result
#
#
# print(f"Your word {words} times {copies} is: {larger_string(words, copies)}")

# number = int(input("Enter the number to check if its old or even: "))
#
#
# def classify(my_number):
#     if number % 2 == 0:
#         print(f"The number {number} is even ")
#     else:
#         print(f"The number {number} is old")
#
#
# classify(number)

number_list = []
list_size = int(input("Enter the size of list: "))
for i in range(list_size):
    number = int(input(f"Enter the number {i + 1} to check: "))
    number_list.append(number)
number_check = 4
global count


def check_number_times(check_number):
    count = 0
    for element in number_list:
        if element == check_number:
            count = count + 1
    # print(f"There is {count} in the list of {number_list}")
    # else:
    #         print(f"There is no number 4 in the list of {number_list}")
    return count


print(f"There are {check_number_times(number_check)} in the list {number_list}")
