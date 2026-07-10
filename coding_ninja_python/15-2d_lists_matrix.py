#A 2D array is simply a table having rows and columns.
#Example
# A[4][3]

# means

# 4 Rows
# 3 Columns

#         Column
#          0   1   2
#       +---+---+---+
# Row 0 |   |   |   |
#       +---+---+---+
# Row 1 |   |   |   |
#       +---+---+---+
# Row 2 |   |   |   |
#       +---+---+---+
# Row 3 |   |   |   |
#       +---+---+---+

#Formula
# Index of an element in a 2D array = (row_index * number_of_columns) + column_index

matrix = [
    ["Rahul", 80, 90],
    ["Priya", 75, 85],
    ["Amit", 95, 88]
]
print(matrix) #Output: [['Rahul', 80, 90], ['Priya', 75, 85], ['Amit', 95, 88]]

#Syntax to access elements in a 2D list
print(matrix[0][0]) #Output: Rahul
print(matrix[1][1]) #Output: 75
print(matrix[2][2]) #Output: 88

#Iterating through a 2D list
for row in matrix:
    for item in row:
        print(item)