string_input = input("Enter the string to check if it is a palindrome: ")
# list = []
# for l in string_input:
#     list.append(l)
# print(list)
my_string_input = ""
for i in string_input:
    my_string_input = i + my_string_input
print(my_string_input)
if string_input == my_string_input:
    print(f"The string {string_input} is a palindrome.")
else:
    print(f"The string {string_input} is not a palindrome.")
