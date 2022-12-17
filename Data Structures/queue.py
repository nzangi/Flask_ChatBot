# create  List for the queue

def create_queue():
    queue = []
    return queue


# create an empty queue
# def check_empty(queue):
#     return len(queue) == 0


# add an element to queue
def enqueue(queue, item):
    queue.append(item)
    print("Element enqueued in the myList is:" + item)


# Remove an element from the queue
def dequeue(queue):
    if len(queue) < 1:
        return None
    return queue.pop(0)


# Display the queue
def dispaly():
    print(queue)


def size():
    return len(queue)


queue = create_queue()
enqueue(queue, str(10))
enqueue(queue, str(20))
enqueue(queue, str(30))
enqueue(queue, str(40))
enqueue(queue, str(50))
enqueue(queue, str(60))

# Displaying element enqueued on the queue

dispaly()

# Removing elements in the queue
# dequeue(queue)

for i in queue:
    # Printing after removing an element
    print("After removing an element : " + dequeue(queue))
    dispaly()
