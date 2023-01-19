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
#
# number_list = []
# list_size = int(input("Enter the size of list: "))
# for i in range(list_size):
#     number = int(input(f"Enter the number {i + 1} to check: "))
#     number_list.append(number)
# number_check = 4
# global count
#
#
# def check_number_times(check_number):
#     count = 0
#     for element in number_list:
#         if element == check_number:
#             count = count + 1
#     # print(f"There is {count} in the list of {number_list}")
#     # else:
#     #         print(f"There is no number 4 in the list of {number_list}")
#     return count
#
#
# print(f"There are {check_number_times(number_check)} in the list {number_list}")

# my_string = input("Enter your string: ")
# power = int(input("Enter the power of your string: "))
#
#
# def string_classify(string, my_power):
#     string_length = 2
#     if string_length > len(string):
#         string_length = len(string)
#     sub_string = string[:string_length]
#
#     result = ""
#     for i in range(my_power):
#         result = result + sub_string
#     return result
#
#
# print(f"The string copy of your string is: {string_classify(my_string, power)}")

# your_letter = input("Enter the number to check whether it is a vowel or not: ")
#
#
# def check_vowel(letter):
#     vowel_list = ['a', 'e', 'i', 'o', 'u']
#     if letter in vowel_list:
#         print(f"The letter {your_letter} is a vowel")
#     else:
#         print(f"The letter {your_letter} is not a vowel")
#
#
# check_vowel(your_letter)
#
# my_list = []
# list_length = int(input("Enter the length of the list: "))
# for i in range(list_length):
#     number = int(input("Enter the number to add in the list: "))
#     my_list.append(number)
#
# check_number = int(input("Enter the number to check in the list: "))
#
#
# def check_list(number_check):
#     if number_check in my_list:
#         print(f"The number {number_check} is in the list of {my_list}")
#     else:
#         print(f"The number {number_check} is not in the list of {my_list}")
#
#
# check_list(check_number)

# number_list = []
# list_length = int(input("Enter the size of your list: "))
# for i in range(list_length):
#     number = int(input("Enter the number to add in your list: "))
#     number_list.append(number)
#
#
# def histogram(list):
#     for i in list:
#         output = ""
#         times = i
#
#         while times > 0:
#             output += "#"
#             times = times - 1
#         print(output)
#
#
# histogram(number_list)
#
# string_list = []
# string_length = int(input("Enter the size of the string: "))
# for i in range(string_length):
#     letters = input("Enter the word to add in your list: ")
#     string_list.append(letters)
#
#
# def concatenated_list():
#     result = ""
#     for element in string_list:
#         result = result + element
#     return result
#
#
# print(f"The concatenated string is: {concatenated_list()}")

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
#
#
# def even_numbers():
#     even_numbers_list = []
#     for i in range(len(numbers)):
#         for element in numbers:
#             if element != 237:
#                 if element % 2 == 0:
#                     even_numbers_list.append(element)
#             else:
#                 break
#     return even_numbers_list
#
#
# print(f"Even numbers before 247 is reached are : {even_numbers()}")

# color_list_1 = []
# color_list_2 = []
# not_in_list2 = []
# not_in_list1 = []
#
# list1_length = int(input("Enter the size of list 1: "))
# for i in range(list1_length):
#     list1_colors = input(f"Enter color {i + 1} in list 1: ")
#     color_list_1.append(list1_colors)
# list2_length = int(input("Enter the size of list 2: "))
# for i in range(list2_length):
#     list2_colors = input(f"Enter color {i + 1} in list 2: ")
#     color_list_2.append(list2_colors)
#
#
# def check_colors():
#     for i in color_list_1:
#         if not i in color_list_2:
#             not_in_list2.append(i)
#     for i in color_list_2:
#         if not i in color_list_1:
#             not_in_list1.append(i)
#
#     return not_in_list2
#
#
# print(f"The color in list 1 {color_list_1} which are not in list 2 {color_list_2} are : {check_colors()}")
# # print(f"The color in list 2 {color_list_2} which are not in list 1 {color_list_1} are : {check_colors()}")

#
# base = int(input("Enter the base of the triangle: "))
# height = int(input("Enter the height of the triangle: "))
#
# def calculate_area(triangle_base,triangle_height):
#     area = 0.5 * triangle_base * triangle_height
#     return area
#
# print(f"The are of triangle with height of {height} and base of {base} is : {calculate_area(base,height)}")

# number_1 = int(input("Enter the number 1 to check GCD: "))
# number_2 = int(input("Enter the number 2  to check GCD: "))
#
#
# def calculate_GCD(a, b):
#     if a > b:
#         small = b
#     else:
#         small = a
#     for i in range(1, small + 1):
#         if (a % i == 0) and (b % i == 0):
#             gcd = i
#     return gcd
#
#
# def calculate_lcm(c, d):
#     if c > d:
#         large = c
#     else:
#         large = d
#
#     while (True):
#         if (large % c == 0) and (large % d == 0):
#             lcm = large
#             break
#         large += 1
#
#     return lcm
#
#
# print(f"The GCD of {number_1} and {number_2} is : {calculate_GCD(number_1, number_2)}")
# print(f"The LCM of {number_1} and {number_2} is : {calculate_lcm(number_1, number_2)}")

# number_1 = int(input("Enter the 1 number find sum : "))
# number_2 = int(input("Enter the 2 number to find sum: "))
# number_3 = int(input("Enter the 3 number to find sum: "))
#
#
# def total(a, b, c):
#     if a == b or a == c or b == c:
#         sum = 0
#     else:
#         sum = a + b + c
#     return sum
#
#
# print(f"The sum of the numbers {number_1},{number_2},{number_3} is : {total(number_1, number_2, number_3)}")

# number_one = int(input("Enter your first number: "))
# number_two = int(input("Enter your second number: "))
#
#
# def sum_of_numbers(number1, number_2):
#     sum = number_2 + number1
#     if sum == 15 or sum == 20:
#         sum = 20
#     else:
#         sum = number_2 + number1
#
#     return sum
#
#
# print(f"The sum of numbers {number_one} and {number_two} is : {sum_of_numbers(number_one, number_two)}")

# number_One = input("Enter your first number: ")
# number_Two = input("Enter the second number: ")
#
#
# def check_int(number1, number2):
#     if not isinstance(number1, int) and isinstance(number2, int):
#         return "inputs must be integers"
#     return number1 + number2
#
#
# print(f"The sum of the two integers is {check_int(number_One, number_Two)}")

# name = input("Enter your name: ")
# age = int(input("Enter your current age: "))
# address = input("Enter your address:  ")
#
#
# def display_details(your_name, your_age, your_address):
#     print(f" Name : {your_name}\n Age : {your_age}\n Address : {your_address}")
#
#
# display_details(name, age, address)

# x = int(input("Enter input of value of X: "))
# y = int(input("Enter input of value of Y: "))
#
#
# def power(a, b):
#     # (x+y) * (x+y)
#     sum = a + b
#     result = sum ** 2
#     return result
#
#
# print(f"The output of (({x} + {y}) ** 2) = {power(x, y)}")
#
# principal = int(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of the principal: "))
# time = int(input("Enter time for the amount to mature: "))
#
#
# def principal_interest(p, r, t):
#     my_principal = p * ((1 + (1/100 * r)) ** t)
#     # interest = (p * r * t) // 100
#     # total_principal = p + interest
#     return round(my_principal,3)
#
#
# print(f"principal and Interest of principal of {principal},rate of {rate} and time of {time} is: {principal_interest(principal,rate,time)}")

# X1 = int(input("Enter the coordinate of X1: "))
# Y1 = int(input("Enter the coordinate of Y1: "))
# X2 = int(input("Enter the coordinate of X2: "))
# Y2 = int(input("Enter the coordinate of Y2: "))
#
#
# def coordinate_distance(x1, y1, x2, y2):
#     answer = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
#
#     result = answer ** 0.5
#     return  result
#
# print(f"The distance between ({X1},{Y1}) and ({X2},{Y2}) is : {coordinate_distance(X1,Y1,X2,Y2)}")

# import os
#
# path = "home/nzangi/PycharmProjects/My Projects/dkdetermine number.py"
# if os.path.exists(path):
#     print("File found")
# else:
#     print("File not found")

# import platform
# import os
# print(f"The name of my OS is : {os.name}")
# print(f"The name of my plaform is :{platform.system()}")
# print(f"The version of the OS: {platform.release()}")
#
# import site
# print(site.getsitepackages()[0])
# print(site.getsitepackages()[1])
# print(site.getsitepackages()[2])
#
# from subprocess import call
# path ="/home/nzangi/PycharmProjects/My Projects/programiz"
# # call(path["ls"])
# call(["ls", "-l"])

# import os
# print(f"Current file is: {os.path.relpath(__file__)}")
#
# import multiprocessing
# print(multiprocessing.cpu_count())
#
# my_string = input("Enter a flaot here: ")
#
# my_float = float(my_string)
# int_mystring = int(my_float)
# print(my_float)
# print(int_mystring)
#
# from os import listdir
# from os.path import isfile,join
# files = [f for f in listdir("/home/nzangi") if isfile(join("/home/nzangi",f))]
# print(files)
#
# for i in range(1,11):
#     print("#",end="")

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')
#
# import os
# print(os.environ["PATH"])
#
# import getpass
# print(getpass.getuser())

# import socket,os
# host_name = socket.gethostname()
# IPAdress = socket.gethostbyname(host_name)
# print(f"Your Computer Name is : {host_name}")
# print(f"Your Computer IP Address is : {IPAdress}")
# print(os.system('ip a'))

#calculate teh excution time of a program
# import time
# loop = int(input("Enter the number of loop to terminate: "))
# global sum
# sum = 0
#
# def calculate_time(loop_number):
#     start_time = time.time()
#     sum = 0
#     for i in range(1,loop_number+1):
#         sum = sum  + i
#     end_time =  time.time()
#     return sum,end_time
# my_tupple = calculate_time(loop)
# print(my_tupple)
# print(f"The sum of from number 1 and to {loop}  is {my_tupple[0]} and excution time is {my_tupple[1]}")


# my_list = []
# numbers_loop = int(input("Enter the the size of your list to add numbers to: "))
# for i in range(numbers_loop):
#     number = int(input(f"Add the number {i+1} to be in your list:  "))
#     my_list.append(number)
#
# def add_numbers(list):
#     sum = 0
#     for i in list:
#         sum = sum + i
#     return sum
#
# print(f"Your sum of the list is : {add_numbers(my_list)}")

# base = int(input("Enter your base of triangle: "))
# height = int(input("Enter your height of traiangle: "))
#
# def hypotenuse(b,h):
#     h = b ** 2 + h ** 2
#     hypotenuse = h** 0.5
#     return hypotenuse
# print(f"The hypotenuse with base of {base} and height of {height} is : {hypotenuse(base,height)}")

# days = int(input("Enter the number of days: "))
# hrs = int(input("Enter the number of hrs: "))
# mins = int(input("Enter the minutes: "))
# sec = int(input("Enter the number od seconds: "))
#
# total_time = (3600* 24* days) + (60*60* hrs) + (60 * mins) + sec
#
# print(f"Total time is : {total_time} seconds")

seconds = int(input("Enter the number of seconds to covert into Days, hrs, minutes and seconds: "))

days = seconds // (3600*24)
rem_hrs = (seconds % (3600*24))
hrs = rem_hrs // 3600
rem_min = (rem_hrs % 3600)
mins = rem_min // 60
sec = (rem_min % 60)

print(f"In {seconds}, there are {days} days {hrs} hrs {mins} mins {sec} secs")



