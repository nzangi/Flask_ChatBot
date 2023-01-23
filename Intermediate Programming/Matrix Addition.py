def addition_matrix():
    rows = int(input("Enter the number of rows which you need to add: "))
    columns = int(input("Enter the number of columns you need to add: "))

    print("Enter the values of first matrix: ")
    matrix_1 = [[int(input()) for j in range(columns)] for i in range(rows)]
    print("Enter the values of second matrix: ")
    matrix_2 = [[int(input()) for j in range(columns)] for i in range(rows)]
    print(matrix_1)
    print(matrix_2)

    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Matrix cannot be added")
        return
    else:
        result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(columns)] for i in range(rows)]
        for row in result:
            print(row)
        print(f"Result of {matrix_1} + {matrix_2} == {result}")

    return result

addition_matrix()


