myList = [80, 89, 87, 56, 76, 67, 67, 77, 65, 45, 43, 32, 89, 67, 77, 88]
# myList = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

sum = 0
# get 1 item on the list
print(myList[-1])
# get last item in the list
print(myList[0])

# sorting items
sorted_list = []
# maximum_number = myList[0]

length = 0

# calculate mean of the list

for _ in myList:
    length += 1
print(length)

for i in range(length):
    for j in range(i + 1, length):
        if myList[i] > myList[j]:
            maximum_number = myList[i]
            myList[i] = myList[j]
            myList[j] = maximum_number

print(f"Sorted list of {myList} is : {myList}")

# calculate sum of the list
for number in myList:
    sum += number
print(sum)
mean = sum // length
# print(mean)
# checking the list
# print(myList)
# MEDIAN
if length % 2 == 0:
    median_1 = myList[length // 2]
    median_2 = myList[length // 2 - 1]
    median = (median_2 + median_1) / 2
else:
    median_ = myList[length // 2]

    # MODE

frequency = {}
for i in myList:
    frequency.setdefault(i, 0)
    frequency[i] += 1
frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i

print(f"The total number of {myList} is : {sum}")
print(f"The mean number of {myList} is : {mean}")
print(f"The median  number of {myList} is : {median}")
print(f"The mode  number of {myList} is : {mode}")
