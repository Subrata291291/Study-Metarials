# Find the row with the maximum number of 1s in a binary matrix
def rowWithMax1s(matrix):

    max_count = 0
    row_index = -1

    for i in range(len(matrix)):
        count = 0

        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1

        if count > max_count:
            max_count = count
            row_index = i

    return row_index