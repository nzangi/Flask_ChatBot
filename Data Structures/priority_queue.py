# priority queue implementation

# heapify function

def heapify(heapArray, n, i):
    # Find the largest among the root,left child and right node
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heapArray[i] < heapArray[left]:
        largest = left

    if right < n and heapArray[largest] < heapArray[right]:
        largest = right

    # swap and continue heapifying if the root it is not the largest

    if largest != i:
        heapArray[i], heapArray[largest] = heapArray[largest], heapArray[i]
        heapify(heapArray, n, largest)


# function insert a new n
def insert(array, newNumber):
    size = len(array)
    if size == 0:
        array.append(newNumber)
    else:
        array.append(newNumber)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# function to delte elements in the tree

def deleteNode(array, number):
    size = len(array)
    i = 0
    for i in range(0, size):
        if number == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]
    # array.remove(size - 1)
    array.remove(size - 1)
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


heapArray = []
insert(heapArray, 2)
insert(heapArray, 4)
insert(heapArray, 1)
insert(heapArray, 5)
insert(heapArray, 7)
# insert(heapArray, 9)
# insert(heapArray, 8)

print(f"Max-Heap Array : {str(heapArray)}")

deleteNode(heapArray, 7)
print(f"After deleting the element, the new array is: {str(heapArray)}")
