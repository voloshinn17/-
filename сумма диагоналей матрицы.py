def sum_diagonals(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or j == len(matrix) - 1 - i:
                total += matrix[i][j]
    return total