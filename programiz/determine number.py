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

exam_date = (11, 12, 2015)
print("The examination will start on: %i / %i / %i " %exam_date)

exam_st_date = (11,12,2014)
print("The examination will start from : %i / %i / %i" %exam_st_date)

