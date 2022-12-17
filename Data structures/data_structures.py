# myList = [10,20,30,40,50]
# total = 0
# print(myList[-2])
# for element in range(0,len(myList)):
#     total = total + myList[element]
# print(total)

names = ["Sam", "Judy", "Michael", "James", "Sarah","Jane", "John"]
marks = ['67','77', '89', '90', '80', '71', '98']
for element in range(0,len(names),len(marks)):
    print(f" {element + 1 }. You Name is {names[element]} and your marks is {marks[element]}")
