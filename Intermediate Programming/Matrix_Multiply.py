def multiply():
    row_1 = int(input("Enter the number of rows of matrix 1: "))
    column_1 = int(input("Enter thr number of columns of matrix 1:"))
    row_2 = int(input("Enter the number of rows of matrix 2: "))
    column_2 = int(input("Enter the number of columns of matrix 2: "))

    if column_1 != row_2:
        print("Sorry, Matrix cannot be multiplied")
    else:
        matrix_1 = [[int(input("Enter the values of matrix 1: ")) for i in range(column_1)] for j in range(row_1)]
        matrix_2 = [[int(input("Enter the values of matrix 2: ")) for i in range(column_2)] for j in range(row_2)]

        result = [[0 for i in range(column_2)] for i in range(row_1)]

        for i in range(row_1):
            for j in range(column_2):
                for k in range(row_2):
                    result [i][j] += matrix_1[i][k] * matrix_2[k][j]
        for row in result:
            print(row)

multiply()
