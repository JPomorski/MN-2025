def get_square_matrix_size(matrix):
    return len(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(f"[{", ".join(f"{val:>8.5f}" for val in row)}]")


def jacobi(a, b, limit):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]
    new_x = [[0.0] for _ in range(n)]

    for _ in range(limit):
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += a[i][j] * x[j][0]

            new_x[i][0] = (b[i][0] - sum) / a[i][i]
        x = [row[:] for row in new_x]

    return x


def jacobi_norm(a, b, tolerance):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]
    new_x = [[0.0] for _ in range(n)]

    k = 0

    while True:
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += a[i][j] * x[j][0]

            new_x[i][0] = (b[i][0] - sum) / a[i][i]

        diff = [abs(new_x[i][0] - x[i][0]) for i in range(n)]
        norm = max(diff)

        if norm < tolerance:
            print(f"Zakończono po {k + 1} iteracjach")
            break

        x = [row[:] for row in new_x]

        k += 1

    return x


def jacobi_zbieznosc(a, b, tolerance):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]
    new_x = [[0.0] for _ in range(n)]

    k = 0

    while True:
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += a[i][j] * x[j][0]

            new_x[i][0] = (b[i][0] - sum) / a[i][i]

        res = [0.0] * n

        for i in range(n):
            sum = 0.0
            for j in range(n):
                sum += a[i][j] * new_x[j][0]

            res[i] = abs(sum - b[i][0])

        diff = max(res)

        if diff < tolerance:
            print(f"Zakończono po {k + 1} iteracjach")
            break

        x = [row[:] for row in new_x]
        k += 1

    return x


def gauss_seidl(a, b, limit):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]

    for _ in range(limit):
        for i in range(n):
            sum_prev = 0.0
            for j in range(i):
                sum_prev += a[i][j] * x[j][0]

            sum = 0.0
            for j in range(i + 1, n):
                sum += a[i][j] * x[j][0]

            x[i][0] = (b[i][0] - sum_prev - sum) / a[i][i]

    return x


def gauss_seidl_norm(a, b, tolerance):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]

    k = 0

    while True:
        old_x = [row[0] for row in x]

        for i in range(n):
            sum_prev = 0.0
            for j in range(i):
                sum_prev += a[i][j] * x[j][0]

            sum = 0.0
            for j in range(i + 1, n):
                sum += a[i][j] * x[j][0]

            x[i][0] = (b[i][0] - sum_prev - sum) / a[i][i]

        diff = [abs(x[i][0] - old_x[i]) for i in range(n)]
        norm = max(diff)

        if norm < tolerance:
            print(f"Zakończono po {k + 1} iteracjach")
            break

        k += 1

    return x


def gauss_seidl_zbieznosc(a, b, tolerance):
    n = get_square_matrix_size(a)

    x = [[0.0] for _ in range(n)]

    k = 0

    while True:
        for i in range(n):
            sum_prev = 0.0
            for j in range(i):
                sum_prev += a[i][j] * x[j][0]

            sum = 0.0
            for j in range(i + 1, n):
                sum += a[i][j] * x[j][0]

            x[i][0] = (b[i][0] - sum_prev - sum) / a[i][i]

        res = [0.0] * n

        for i in range(n):
            s = 0.0
            for j in range(n):
                s += a[i][j] * x[j][0]
            res[i] = abs(s - b[i][0])
        norm_res = max(res)

        if norm_res < tolerance:
            print(f"Zakończono po {k + 1} iteracjach")
            break

        k += 1

    return x


przyklad_a = [
    [5.0, -1.0, 2.0],
    [3.0, 8.0, -2.0],
    [1.0, 1.0, 4.0]
]

przyklad_b = [
    [12.0],
    [-25.0],
    [6.0]
]

a1 = [
    [4.0, -2.0, 0.0, 0.0],
    [-2.0, 5.0, -1.0, 0.0],
    [0.0, -1.0, 4.0, 2.0],
    [0.0, 0.0, 2.0, 3.0]
]

b1 = [
    [0.0],
    [2.0],
    [3.0],
    [-2.0]
]

print("Zadanie 1:")
print("Jacobi - iteracje:")
result = jacobi(a1, b1, 100)
print_matrix(result)
print()

print("Jacobi - norma:")
result = jacobi_norm(a1, b1, 1e-9)
print_matrix(result)
print()

print("Jacobi - błąd (zbieżność):")
result = jacobi_zbieznosc(a1, b1, 1e-9)
print_matrix(result)
print()

print("====================================")
print()

print("Zadanie 2:")

print("Gauss - iteracje:")
result = gauss_seidl(a1, b1, 100)
print_matrix(result)
print()

print("Gauss - norma:")
result = gauss_seidl_norm(a1, b1, 1e-9)
print_matrix(result)
print()

print("Gauss - błąd (zbieżność):")
result = gauss_seidl_zbieznosc(a1, b1, 1e-9)
print_matrix(result)
