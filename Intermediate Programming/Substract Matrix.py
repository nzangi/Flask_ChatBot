def substract_matrix():
    rows_1 = int(input("Enter the number of rows in matrix 1: "))
    columns_1 = int(input("Enter the number of columns in matrix 1: "))
    rows_2 = int(input("Enter the number of rows for matrix 2; "))
    columns_2 = int(input("Enter the number of columns of matrix 2: "))

    if rows_1 != rows_2 or columns_1 != columns_2:
        print("The matrix cannot be subtracted. It should have the same number of rows and columns")
    else:
        matrix_1 = [[int(input("Enter the values of matrix 1: ")) for i in range(columns_1)] for i in range(rows_1)]
        matrix_2 = [[int(input("Enter thr values of matrix 2: ")) for i in range(columns_2)] for j in range(rows_2)]

        result = [[matrix_1[i][j] - matrix_2[i][j] for i in range(columns_1)] for j in range(rows_1)]

        for row in result:
            print(row)

substract_matrix()


