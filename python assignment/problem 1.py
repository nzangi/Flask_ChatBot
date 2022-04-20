file = open("/home/nzangi/student grades", 'r')
contents = file.read()
print(contents)

# 1. student dictionary
jack = {"name": "Baker",
        "id": 111452,
        "test1": [80],
        "test2": [83],
        "test3": [84]
        }

# 2. student dictionary
james = {"name": "Simpson",
         "id": 111657,
         "test1": [88],
         "test2": [92],
         "test3": [95]
         }

# 3. student dictionary
dylan = {"name": "Mathews",
         "id": 111932,
         "test1": [77],
         "test2": [75],
         "test3": [78]
         }
cindy = {"name": "Williams",
         "id": 1117,
         "test1": [65],
         "test2": [71],
         "test3": [81]
         }

# 4. student dictionary
jess = {"name": "Jacobs",
        "id": 111873,
        "test1": [67],
        "test2": [72],
        "test3": [68]
        }

# 5. student dictionary
tom = {"name": "Albright",
       "id": 11262,
       "test1": [91],
       "test2": [95],
       "test3": [92]
       }
# storing data of students
students = [jack, james, dylan, jess, tom, cindy]


# calcualting the sum of marks of students
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


# Function calculates total average
def calculate_total_average(students):
    test1 = get_average(students["test1"])
    test2 = get_average(students["test2"])
    test3 = get_average(students["test3"])

    # Return the result based
    # on weightage supplied, 30,30,40 respectively
    return (0.3 * test1 +
            0.3 * test2 + 0.4 * test3)


# Calculate letter grade of each student scored
def assign_letter_grade(score):
    if score > 90:
        return "A"
    elif score >= 85 and score >= 89.99:
        return "A-"
    elif score >= 80 and score >= 84.99:
        return "B+"
    elif score >= 70 and score >= 79.99:
        return "B"
    elif score >= 60 and score >= 69.99:
        return "C"
    elif score >= 50 and score >= 59.99:
        return "D"
    else:
        return "E"


open('examfile.txt', 'w').close()
print('{a:^8}{b:^8}{c:^8}'.format(a='Last Name', b='ID', c='Grade'), file=open('examfile.txt', 'a'))
for i in students:
    print(i["name"], '\t', i["id"], '\t', assign_letter_grade(calculate_total_average(i)), file=open('examfile.txt', 'a'))
