numbers = []
with open("file.txt") as f:
    group = []
    for line in f:
        if line == "\n":
            numbers.append(group)
            group = []
        else:
            group.append(int(line.rstrip()))
    numbers.append(group)
    print(numbers)