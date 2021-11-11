import random

# declaring the empty list
my_list = []
for _ in range(100):
    # ilterating all the values from -15.00 - 150.00 for oonly 100 vqlues
    value = random.uniform(-15, 150)
    my_list.append(value)

# printing the list
print(f"my list contains the following numbers {my_list}")


def max_and_min():
    # calculating the maximum value
    maximum = max(my_list)
    print(f"The maximum value if {maximum}")

    # calculating the maximum value

    manimum = min(my_list)
    print(f"The maximum value if {manimum}")


max_and_min()


def split():
    negative_numbers = []
    positive_numbers = []
    for x in my_list:
        if x >= 0:
            # spliting all the positive numbers only
            positive_numbers.append(x)
        else:
            # spliting all the negative numbers only
            negative_numbers.append(x)

    #         printing all positive numbers in one list and negative numbers in another list
    print(f"The negative numbers are {negative_numbers}")
    print(f"The positive numbers are {positive_numbers}")


split()
