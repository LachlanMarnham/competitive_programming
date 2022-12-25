def flipping_matrix(matrix):
    n = len(matrix) // 2
    max_vals = []
    for i in range(n):
        for j in range(n):
            a = matrix[i][j]
            b = matrix[i][2 * n - j - 1]
            c = matrix[2 * n - i - 1][j]
            d = matrix[2 * n - i - 1][2 * n - j - 1]
            new_max_val = max(a, b, c, d)
            max_vals.append(new_max_val)
    return sum(max_vals)
