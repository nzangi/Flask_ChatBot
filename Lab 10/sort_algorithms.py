import random, time


def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


def bubble_sort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def selection_sort(array):
    # Traverse through all array elements
    for i in range(len(array)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]


def binary_search(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def SequentialSearch(array, n, x):
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


def create_unsorted_list(size):
    # Creates a random list of integers to sort
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(1, size))
    return random_list


def print_list(mylist):
    # Checks the size of list and prints if not too long
    if len(mylist) <= 100:
        print(mylist)


def test_algorithm(sort_function, description, random_list):
    list_to_sort = []
    list_to_sort += random_list
    print(f"starting {description}...")
    start = time.perf_counter_ns()
    # sorted_list = sort_function(list_to_sort)
    end = time.perf_counter_ns()
    processing_time = end - start
    print(f"{description} finished in {processing_time:,d} nanoseconds.")


def main():
    size = int(input("How large of a list should we sort? "))
    random_list = create_unsorted_list(size)
    print_list(random_list)
    # Function call of sequential search

    array = random_list
    x = 3
    n = len(array)
    result = SequentialSearch(array, n, x)
    # Function call of binary search
    array = random_list
    x = 4
    result = binary_search(array, x, 0, len(array) - 1)
    # test_algorithm(selection_sort(random_list, size), "selection sort", random_list)
    test_algorithm(selection_sort, "selection sort", random_list)
    test_algorithm(insertion_sort, "insertion sort", random_list)
    test_algorithm(bubble_sort, "bubble sort", random_list)
    test_algorithm(binary_search, "binary search", random_list)
    if result != -1:
        print("Target found in the list")
    else:
        print("Target found in the list")
    test_algorithm(SequentialSearch, "SequentialSearch sort", random_list)
    # selection_sort(random_list)
    # print(f'selection sort :{random_list}')
    # insertion_sort(random_list)
    # print(f'insertion_sort : {random_list}')
    # bubble_sort(random_list)
    # print(f'bubble_sort : {random_list}')


if __name__ == '__main__':
    main()
