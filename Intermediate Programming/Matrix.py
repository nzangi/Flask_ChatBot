# def adding_maxtrix():
#     row_1 = int(input("Enter the rows of the first matrix: "))
#     column_1 = int(input("Enter the columns of the first matrix: "))
#     row_2 = int(input("Enter the rows of the second matrix: "))
#     column_2 = int(input("Enter the columns of the second matrix: "))
#
#     if row_1 != row_2 or column_1 != column_2:
#         print("Matrix cannot be added")
#     else:
#         maxtrix_1 = [[int(input("Enter the values of matrix one: ")) for i in range(column_1)] for j in range(row_1)]
#         maxtrix_2 = [[int(input("Enter the values of matrix two: ")) for i in range(column_2)] for j in range(row_2)]
#         result = [[maxtrix_1[i][j] + maxtrix_2[i][j] for j in range(column_1)] for i in range(row_1)]
#
#         print(f"Result of {maxtrix_1} + {maxtrix_2} == {result}")
#
#         for row in maxtrix_1:
#             print(row)
#         for row in maxtrix_2:
#             print(row)
#         for row in result:
#             print(row)
#
#     # return result
#
#
# adding_maxtrix()

def matrix():
    rows_1 = int(input("Enter the number of rows for matrix one: "))
    columns_1 = int(input("Enter the number of columns for matrix one: "))
    rows_2 = int(input("Enter the number of rows for matrix two: "))
    columns_2 = int(input("Enter the number of columns for matrix two: "))

    if rows_1 != rows_2 or columns_1 != columns_2:
        print("Sorry, your matrix cannot be added. For matrix to be added it, should have the same size of rows and "
              "columns")
    else:
        matrix_1 = [[int(input("Enter the values of matrix 1: ")) for i in range(rows_1)] for j in range(columns_1)]
        matrix_2 = [[int(input("Enter the values of matrix 2: ")) for i in range(rows_2)] for j in range(columns_2)]

        result = [[matrix_1[i][j] + matrix_2[i][j] for i in range(rows_1)] for j in range(columns_2)]

        for row in result:
            print(row)

matrix()

