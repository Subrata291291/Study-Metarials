def setMaxZeros(mat, n, m):

    max_zeros = 0
    row = -1

    for i in range(n):

        zeros = 0

        for j in range(m):
            if mat[i][j] == 0:
                zeros += 1

        if zeros > max_zeros:
            max_zeros = zeros
            row = i

    return row