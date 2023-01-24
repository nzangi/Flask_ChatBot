def multiply_matrix():
    rows_1 = int(input("Enter the number of rows in matrix 1: "))
    columns_1 = int(input("Enter the number of columns in matrix 1: "))
    rows_2 = int(input("Enter the number of rows in matrix 2: "))
    columns_2 = int(input("Enter the number of columns in matrix 2: "))

    if columns_1 != rows_2:
        print("Sorry, your matrix cannot be multiplied")

    else:
        matrix_1 = [[int(input("Enter the values of matrix 1: ")) for i in range(columns_1)] for j in range(rows_1)]
        matrix_2 = [[int(input("Enter the values of matrix 2: ")) for i in range(columns_2)] for j in range(rows_2)]
        # result = 0
        result = [[0 for i in range(columns_2)] for j in range(rows_1)]
        for i in range(rows_1):
            for j in range(columns_2):
                for k in range(rows_2):
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
        for row in result:
            print(row)


multiply_matrix()
