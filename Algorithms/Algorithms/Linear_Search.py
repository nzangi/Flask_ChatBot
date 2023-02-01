def search(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1


my_list = [10, 20, 80, 30, 60, 50,
           110, 100, 130, 170]
y = 1000
result = search(my_list, y)
if result == -1:
    print(f"Element not in the list")
else:
    print(f"Element on the list : {my_list} at index {str(result)}")
