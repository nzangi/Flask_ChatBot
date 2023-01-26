string_text = input("Enter the input of the string: ")
string1 = ''
string2 = ''
string3 = ''
for i in range(0, len(string_text)):
    if i <= len(string_text) // 2 - 1:
        string1 = string1 + string_text[i]
    else:
        string2 = string2 + string_text[i]
print(string1, string2)

for i in string_text:
    string3 = i + string3
print(string3)

if string1 == string2:
    print("The string it is and symmetrical")
else:
    print("The string it is not a symmetrical")
if string_text == string3:
    print("The string it is palindrome")
else:
    print("The string it is not palindrome")
