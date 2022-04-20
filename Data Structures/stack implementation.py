# stack implementation

# creating a stack

def create_stack():
    stack = []
    return stack


# creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# adding items to stack
def add_item(stack, item):
    stack.append(item)
    print("Pushed Item :" + item)


# Removing items in stack
def delete_item(stack):
    if check_empty(stack):
        return "Stack Is Empty, Nothing to Remove"
    return stack.pop()


stack = create_stack()

add_item(stack, str(10))
add_item(stack, str(20))
add_item(stack, str(30))
add_item(stack, str(40))
add_item(stack, str(50))
for i in stack:
    print("Popped Item :" + delete_item(stack))
    print("Stack after Popping Element :" + str(stack))
