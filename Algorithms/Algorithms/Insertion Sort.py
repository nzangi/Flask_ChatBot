# insertion sort
number_list = []
list_length = int(input("Enter the size of your list : "))
for i in range(list_length):
    number = int(input("Enter the number to add in your list: "))
    number_list.append(number)


def insertion_sort(list):
    if (n := len(list)) <= 1:
        return
    for i in range(1, n):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key


insertion_sort(number_list)
print(f"Your was sorted to {number_list} ")
