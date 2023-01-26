string_input = input("Enter your sentence to reverse here: ")
# reverse_string = ''
reverse_string = string_input.split(' ')
# print(result)
# for word in reverse_string:
#     reverse_string = word + reverse_string[::-1]
# print(reverse_string)
result = [word for word in reverse_string[::-1]]
print(result)

for word in result:
    print(word,end="\t")