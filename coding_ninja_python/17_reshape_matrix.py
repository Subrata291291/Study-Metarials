# #Reshape a matrix
# def reshapeMatrix(mat, r, c):

#     rows = len(mat)
#     cols = len(mat[0])

#     if rows * cols != r * c:
#         return mat

#     # Convert matrix into a single list
#     temp = []

#     for row in mat:
#         for element in row:
#             temp.append(element)

#     # Create new matrix
#     result = []
#     index = 0

#     for i in range(r):

#         new_row = []

#         for j in range(c):
#             new_row.append(temp[index])
#             index += 1

#         result.append(new_row)

#     return result


#Sum of each row in a matrix
# def rowWiseSum(mat, n , m):
#     for i in range(n):
#         sum = 0
#         for j in range(m):
#             sum = sum + mat[i][j]
#         print(sum, end = " ")


# Take number of rows and columns
# n = int(input("Enter number of rows: "))
# m = int(input("Enter number of columns: "))

# # Create an empty matrix
# matrix = []

# # Take matrix input
# print("Enter the matrix:")

# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# # Print row sums
# for i in range(n):

#     total = 0

#     for j in range(m):
#         total += matrix[i][j]

#     print(total, end=" ")


