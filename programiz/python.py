value_x2 = int(input("Enter the value of X2 : "))
value_x = int(input("Enter the value of X : "))
value_c = int(input("Enter the value of C : "))

# calculate the value of d
d = value_x ** 2 - (4 * value_x2 * value_c)
square_d = d ** 0.5

solution_A = (-value_x + square_d) / 2 * value_x2
solution_B = (-value_x - square_d) / 2 * value_x2

print(f"The first solution of the equation is : {solution_A}")
print(f"The second solution of the equation is : {solution_B}")

