

def is_matrix_square(matrix):
    row_count = len(matrix)

    for row in matrix:
        if len(row) != row_count:
            return False

    return True


def get_square_matrix_size(matrix):
    return len(matrix)


def get_matrix_size(matrix):
    return len(matrix), len(matrix[0])


def get_minor(matrix, i, j):
    minor = [row[:] for row in matrix]
    minor.pop(i)

    for row in minor:
        row.pop(j)

    return minor


def det(matrix):
    n = get_square_matrix_size(matrix)

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    elif n == 3:
        n = get_square_matrix_size(matrix)
        sarrus_matrix = [[0.0] * (n + 2) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                sarrus_matrix[i][j] = matrix[i][j]

        for i in range(n):
            for j in range(2):
                sarrus_matrix[i][n + j] = matrix[i][j]

        det_value = 0.0
        offset = 0

        for _ in range(3):
            d = 1.0

            for j in range(n):
                d *= sarrus_matrix[j][j + offset]

            det_value += d
            offset += 1

        offset = 0

        for _ in range(3):
            d = 1.0

            for j in range(n - 1, -1, -1):
                d *= sarrus_matrix[(n - 1) - j][j + offset]

            det_value -= d
            offset += 1

        return det_value

    elif n > 3:
        det_value = 0.0

        for j in range(n):
            c = get_minor(matrix, 0, j)
            det_value += pow(-1.0, j) * matrix[0][j] * det(c)

        return det_value


def transpose(matrix):
    m, n = get_matrix_size(matrix)
    transposed = [[0.0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]

    return transposed


def multiply(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0.0] * cols_b for _ in range(rows_a)]

    for row_a in range(rows_a):
        for col_b in range(cols_b):
            for col_a in range(cols_a):
                result[row_a][col_b] += a[row_a][col_a] * b[col_a][col_b]

    return result


def get_cofactor(matrix):
    n = get_square_matrix_size(matrix)
    cofactor = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            minor_det = det(minor)

            cofactor[i][j] = pow(-1.0, (i + j)) * minor_det

    return cofactor


def invert_laplacian(matrix):
    det_value = det(matrix)

    if det_value == 0.0:
        print("Nie można odwrócić macierzy o wyznaczniku 0!")
        return

    cofactor = get_cofactor(matrix)
    adj = transpose(cofactor)

    n = get_square_matrix_size(adj)

    for i in range(n):
        for j in range(n):
            adj[i][j] /= det_value

    return adj


def invert_gauss_jordan(matrix):
    det_value = det(matrix)

    if det_value == 0.0:
        print("Nie można odwrócić macierzy o wyznaczniku 0!")
        return

    n = get_square_matrix_size(matrix)
    augmented = [[0.0] * (n * 2) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            augmented[i][j] = matrix[i][j]

        augmented[i][n + i] = 1.0

    for i in range(n):
        max_row = i
        max_val = abs(augmented[i][i])

        for j in range((i + 1), n):
            if abs(augmented[j][i]) > max_val:
                max_val = abs(augmented[j][i])
                max_row = j

        if max_row != i:
            augmented[max_row], augmented[i] = augmented[i], augmented[max_row]

        pivot = augmented[i][i]

        for j in range(n * 2):
            augmented[i][j] /= pivot

        for j in range(n):
            if j != i:
                factor = augmented[j][i]

                for k in range(n * 2):
                    augmented[j][k] -= factor * augmented[i][k]

    inverse = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            inverse[i][j] = augmented[i][n + j]

    return inverse


def print_matrix(matrix):
    for row in matrix:
        print(row)


print("Zadanie 1:")
print()

square_matrix = [
    [2.0, 4.0],
    [1.0, 3.0]
]

print_matrix(square_matrix)

det_value = det(square_matrix)
print(f"Wspolczynnik: {det_value}")

print()

big_square_matrix = [
    [2.0, 4.0, 3.0],
    [1.0, 3.0, 2.0],
    [1.0, 2.0, 3.0]
]

print_matrix(big_square_matrix)

det_value = det(big_square_matrix)
print(f"Wspolczynnik: {det_value}")

print()

przyklad = [
    [15.0, 11.0, 10.0, 15.0],
    [19.0, 9.0, 0.0, 17.0],
    [6.0, 9.0, 6.0, 13.0],
    [0.0, 12.0, 12.0, 11.0]
]

print_matrix(przyklad)

det_value = det(przyklad)
print(f"Wspolczynnik: {det_value}")

print()

print("Zadanie 2:")

transposed = transpose(square_matrix)
print_matrix(transposed)

print()

matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

transposed = transpose(matrix)
print_matrix(transposed)

print()

print("Zadanie 3:")

inv = invert_gauss_jordan(przyklad)
if inv:
    print_matrix(inv)
    det_value = det(inv)
    print(det_value)

print()

aaa = multiply(przyklad, inv)
print_matrix(aaa)

print()

aaa = multiply(inv, przyklad)
print_matrix(aaa)

print()

inverse = invert_laplacian(big_square_matrix)
if inverse:
    print_matrix(inverse)

print()

inverse = invert_gauss_jordan(big_square_matrix)
if inverse:
    print_matrix(inverse)

print("==================")

inverse = invert_laplacian(przyklad)
if inverse:
    print_matrix(inverse)

print()

inverse = invert_gauss_jordan(przyklad)
if inverse:
    print_matrix(inverse)
