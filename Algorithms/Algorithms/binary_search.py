# number_list = []
# # collect numbers from user(make your list)
# list_length = int(input('Enter the length of the list: '))
# for i in range(list_length):
#     number = int(input("Enter the number which you need to add in the list: "))
#     number_list.append(number)
#
# print(number_list)
#
# for i in range(len(number_list)):
#     for j in range(0, len(number_list) - i - 1):
#         if number_list[j] > number_list[j + 1]:
#             number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
# print(number_list)
#
#
# def binary_search(list, x):
#     low = 0
#     high = len(list) - 1
#     mid = 0
#
#     while low <= high:
#         mid = (high + low) // 2
#
#         # if x is greater, ignore left
#
#         if list[mid] < x:
#             low = mid + 1
#         # if x is smaller , ignore right
#         elif list[mid] > x:
#             low = mid - 1
#         else:
#             return mid
#     return -1
#
#
# number_search = int(input("Enter the number to search: "))
# result = binary_search(number_list,number_search)
#
# if result != -1:
#     print(f"Element is present at index {str(result)}")
# else:
#     print(f"The number {number_search} is not at list {number_list}")


# implemnting binary search

# adding numbers to your list
number_list = []
list_length = int(input("Enter the size of your list: "))
for i in range(list_length):
    number = int(input("Enter the number to add at your list: "))
    number_list.append(number)

# sort the list in ascending order
for i in range(list_length):
    for j in range(0, len(number_list) - i - 1):
        if number_list[j] > number_list[j + 1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
print(f"Sorted List {number_list}")


def binary_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if list[mid] > x:
            low = list[mid] + 1
        elif list[i] < x:
            low = list[mid] - 1
        else:
            return mid
    return -1


number_search = int(input("Enter number to search: "))
result = binary_search(number_list, number_search)

if result == -1:
    print(f"Number not in the list ")
else:
    print(f"Number {number_search} in the list of {number_list} at index {str(result)}")