string_one = input("Enter the first string to compare: ")
string_two = input("Enter the second string to compare: ")
count = 0
for element in string_one:
    if element in string_two:
        count = count + 1
print(count)