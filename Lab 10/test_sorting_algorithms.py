import time
import random
from mergesort import merge_sort
from quicksort import quick_sort
from sort_algorithms import selection_sort
from sort_algorithms import insertion_sort
from sort_algorithms import bubble_sort


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
    print_list(list_to_sort)
    print(f"starting {description}...")
    start = time.perf_counter_ns()
    sorted_list = sort_function(list_to_sort)
    end = time.perf_counter_ns()
    processing_time = end - start
    print(f"{description} finished in {processing_time:,d} nanoseconds.")
    print_list(sorted_list)
    print("*" * 20)


def main():
    size = int(input("How large of a list should we sort? "))
    random_list = create_unsorted_list(size)

    test_algorithm(selection_sort, "selection sort", random_list)
    test_algorithm(insertion_sort, "insertion sort", random_list)
    test_algorithm(bubble_sort, "bubble sort", random_list)
    test_algorithm(merge_sort, "mergesort", random_list)
    test_algorithm(quick_sort, "quicksort", random_list)


if __name__ == "__main__":
    main()
