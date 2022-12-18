value_x2 = float(input("Enter the value of X2 : "))
value_x = float(input("Enter the value of X : "))
value_c = float(input("Enter the value of C : "))

if value_x2 > 1:
    value_x22 = value_x2/value_x2
    value_xx = value_x/value_x2
    value_cc = value_c/value_x2

# calculate the value of d
    d = value_xx ** 2 - (4 * value_x22 * value_cc)
    square_d = d ** 0.5

    solution_A = (-value_xx + square_d) / 2 * value_x22
    solution_B = (-value_xx - square_d) / 2 * value_x22

    print(f"The first solution of the equation is : {solution_A}")
    print(f"The second solution of the equation is : {solution_B}")

else:
    d = value_x ** 2 - (4 * value_x2 * value_c)
    square_d = d ** 0.5

    solution_A = (-value_x + square_d) / 2 * value_x2
    solution_B = (-value_x - square_d) / 2 * value_x2

    print(f"The first solution of the equation is : {solution_A}")
    print(f"The second solution of the equation is : {solution_B}")

