import time
import math


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
        print(f"[{", ".join(f"{val:>5.1f}" for val in row)}]")


def doolittle(matrix):
    n = get_square_matrix_size(matrix)

    vec_u = [[0.0] * n for _ in range(n)]
    vec_l = [[0.0] * n for _ in range(n)]

    for i in range(3):
        vec_l[i][i] = 1.0

    for i in range(n):
        for j in range(i, n):
            sum_u = 0.0
            sum_l = 0.0

            for k in range(i):
                sum_u += vec_l[i][k] * vec_u[k][j]
                sum_l += vec_l[j][k] * vec_u[k][i]

            vec_u[i][j] = matrix[i][j] - sum_u
            vec_l[j][i] = (matrix[j][i] - sum_l) / vec_u[i][i]

    return vec_l, vec_u


def solve_linear_equation(l_matrix, u_matrix, b):
    n = get_square_matrix_size(l_matrix)
    y = [[0.0] for _ in range(n)]

    for i in range(n):
        sum = 0.0

        for j in range(i):
            sum += l_matrix[i][j] * y[j][0]

        y[i][0] = sum * -1.0 + b[i][0]

    x = [[0.0] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        sum = 0.0

        for j in range(n - 1, i, -1):
            sum += u_matrix[i][j] * x[j][0]

        x[i][0] = (sum * -1.0 + y[i][0]) / u_matrix[i][i]

    return x


def cholesky(matrix):
    n = get_square_matrix_size(matrix)

    l_matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        sum_diag = 0.0

        for k in range(i):
            sum_diag += math.pow(l_matrix[i][k], 2)

        l_matrix[i][i] = math.sqrt(matrix[i][i] - sum_diag)

        for j in range(i + 1, n):
            sum_other = 0.0

            for k in range(i):
                sum_other += l_matrix[j][k] * l_matrix[i][k]

            l_matrix[j][i] = (1 / l_matrix[i][i]) * (matrix[j][i] - sum_other)

    return l_matrix


def solve_cholesky(l_matrix, b):
    n = get_square_matrix_size(l_matrix)
    y = [[0.0] for _ in range(n)]

    for i in range(n):
        sum = 0.0
        for j in range(i):
            sum += l_matrix[i][j] * y[j][0]

        y[i][0] = (b[i][0] - sum) / l_matrix[i][i]

    lt = transpose(l_matrix)
    x = [[0.0] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum += lt[i][j] * x[j][0]

        x[i][0] = (y[i][0] - sum) / lt[i][i]

    return x


def solve_gauss(a, b):
    n = get_square_matrix_size(a)
    a_matrix = [row[:] for row in a]
    b_matrix = [row[:] for row in b]

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = a_matrix[i][k] / a_matrix[k][k]

            for j in range(k + 1, n):
                a_matrix[i][j] = a_matrix[i][j] - factor * a_matrix[k][j]

            b_matrix[i][0] = b_matrix[i][0] - factor * b_matrix[k][0]

    x = [[0.0] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum += a_matrix[i][j] * x[j][0]

        x[i][0] = (b_matrix[i][0] - sum) / a_matrix[i][i]

    return x


def measure_zad_01(a, b):
    start = time.perf_counter()

    inv_lap = invert_laplacian(a)
    result = multiply(inv_lap, b)

    elapsed = time.perf_counter() - start

    print("Macierz wejściowa:")
    print_matrix(a)
    print()

    print("Macierz odwrotna:")
    print_matrix(inv_lap)
    print()

    print("Wynik:")
    print_matrix(result)
    print()

    print(f"Czas wykonania (Laplace): {elapsed:f}s")
    print()

    start = time.perf_counter()

    inv_gauss = invert_gauss_jordan(a)
    result = multiply(inv_gauss, b)

    elapsed = time.perf_counter() - start

    print("Macierz wejściowa:")
    print_matrix(a)
    print()

    print("Macierz odwrotna:")
    print_matrix(inv_gauss)
    print()

    print("Wynik:")
    print_matrix(result)
    print()

    print(f"Czas wykonania (Gauss): {elapsed:f}s")
    print()


def measure_zad_02(a, b):
    start = time.perf_counter()

    l_matrix, u_matrix = doolittle(a)
    result = solve_linear_equation(l_matrix, u_matrix, b)

    elapsed = time.perf_counter() - start

    lu_matrix = multiply(l_matrix, u_matrix)

    print("Macierz L:")
    print_matrix(l_matrix)
    print()

    print("Macierz U:")
    print_matrix(u_matrix)
    print()

    print("Macierz LU:")
    print_matrix(lu_matrix)
    print()

    print("Macierz wejściowa:")
    print_matrix(a)
    print()

    print("Wynik:")
    print_matrix(result)
    print()

    print(f"Czas wykonania (LU): {elapsed:f}s")
    print()


def measure_zad_03(a, b):
    start = time.perf_counter()

    l_matrix = cholesky(a)
    result = solve_cholesky(l_matrix, b)

    elapsed = time.perf_counter() - start

    print("Macierz wejściowa:")
    print_matrix(a)
    print()

    print("Macierz L:")
    print_matrix(l_matrix)
    print()

    print("Macierz LT:")
    print_matrix(transpose(l_matrix))
    print()

    print("Wynik:")
    print_matrix(result)
    print()

    print(f"Czas wykonania (Cholesky): {elapsed:f}s")
    print()


def measure_zad_04(a, b):
    start = time.perf_counter()

    result = solve_gauss(a, b)

    elapsed = time.perf_counter() - start

    print("Macierz wejściowa:")
    print_matrix(a)
    print()

    print("Wynik:")
    print_matrix(result)
    print()

    print(f"Czas wykonania (Gauss): {elapsed:f}s")
    print()


a1 = [
    [1.0, 2.0, 1.0],
    [3.0, -7.0, 2.0],
    [2.0, 4.0, 5.0]
]

b1 = [
    [-9.0],
    [61.0],
    [-9.0]
]

a2 = [
    [11.0, -5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [-5.0, 11.0, -5.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, -5.0, 11.0, -5.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, -5.0, 11.0, -5.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, -5.0, 11.0, -5.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, -5.0, 11.0, -5.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, -5.0, 11.0, -5.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -5.0, 11.0]
]

b2 = [
    [11.0],
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [0.0],
]

a3 = [
    [1.0, 6.0, 3.0, 8.0, 7.0, 6.0, 9.0, 4.0, 7.0, 3.0],
    [0.0, 8.0, 8.0, 4.0, 6.0, 7.0, 5.0, 2.0, 2.0, 2.0],
    [3.0, 3.0, 7.0, 7.0, 1.0, 6.0, 9.0, 1.0, 2.0, 10.0],
    [6.0, 9.0, 6.0, 9.0, 5.0, 10.0, 6.0, 1.0, 8.0, 4.0],
    [2.0, 1.0, 9.0, 4.0, 6.0, 7.0, 8.0, 8.0, 7.0, 5.0],
    [10.0, 6.0, 2.0, 7.0, 7.0, 2.0, 10.0, 6.0, 10.0, 7.0],
    [7.0, 1.0, 8.0, 9.0, 1.0, 4.0, 10.0, 6.0, 5.0, 3.0],
    [7.0, 1.0, 9.0, 6.0, 9.0, 3.0, 8.0, 10.0, 9.0, 7.0],
    [9.0, 6.0, 8.0, 7.0, 7.0, 2.0, 3.0, 10.0, 5.0, 10.0],
    [10.0, 6.0, 6.0, 5.0, 9.0, 2.0, 0.0, 9.0, 2.0, 2.0],
]

b3 = [
    [5.0],
    [10.0],
    [10.0],
    [6.0],
    [4.0],
    [10.0],
    [9.0],
    [0.0],
    [7.0],
    [2.0],
]

print("Zadanie 1:")
print()

measure_zad_01(a1, b1)
measure_zad_01(a2, b2)
measure_zad_01(a3, b3)

print("Zadanie 2:")
print()

measure_zad_02(a1, b1)
measure_zad_02(a2, b2)
measure_zad_02(a3, b3)

print("Zadanie 3:")
print()

a4 = [
    [4.0, 2.0],
    [2.0, 3.0]
]

b4 = [
    [10.0],
    [8.0]
]

measure_zad_03(a2, b2)
measure_zad_03(a4, b4)

print("Zadanie 4:")
print()

measure_zad_04(a1, b1)
measure_zad_04(a2, b2)
measure_zad_04(a3, b3)
