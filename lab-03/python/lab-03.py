import math


class Matrix:
    def __init__(self, matrix):
        self.data = matrix

    def print(self):
        for row in self.data:
            print(row)

    def multiply_by_value(self, x):
        rows = len(self.data)
        cols = len(self.data[0])

        result = Matrix([[0.0 for _ in range(cols)] for _ in range(rows)])

        for row in range(rows):
            for col in range(cols):
                result.data[row][col] = self.data[row][col] * x

        return result

    def add(self, other):
        rows = len(self.data)
        cols = len(self.data[0])

        result = Matrix([[0.0 for _ in range(cols)] for _ in range(rows)])

        for row in range(rows):
            for col in range(cols):
                result.data[row][col] += self.data[row][col] + other.data[row][col]

        return result

    def multiply(self, other):
        if len(self.data[0]) != len(other.data):
            return

        rows_a = len(self.data)
        cols_a = len(self.data[0])
        cols_b = len(other.data[0])

        result = Matrix([[0.0 for _ in range(cols_b)] for _ in range(rows_a)])

        for row_a in range(rows_a):
            for col_b in range(cols_b):
                for col_a in range(cols_a):
                    result.data[row_a][col_b] += self.data[row_a][col_a] * other.data[col_a][col_b]

        return result


def euclidean_norm(vector):
    return math.sqrt(sum(map(lambda x: x ** 2, vector)))


def manhattan_norm(vector):
    return sum(map(lambda x: math.fabs(x), vector))


def maximum_norm(vector):
    return max(map(lambda x: math.fabs(x), vector))


def euclidean_metric(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]

    return math.sqrt(dx ** 2 + dy ** 2)


def manhattan_metric(p, q):
    dx = math.fabs(q[0] - p[0])
    dy = math.fabs(q[1] - p[1])

    return dx + dy


def river_metric(p, q):
    return math.fabs(p[1]) + math.fabs(q[0] - p[0]) + math.fabs(q[1])


def rail_metric(p, q):
    if (p[0] * q[1]) - (p[1] * q[0]) == 0:
        return euclidean_metric(p, q)
    else:
        return euclidean_metric(p, (0.0, 0.0)) + euclidean_metric(q, (0.0, 0.0))


def frobenius_matrix(matrix):
    matrix_sum = 0

    for row in matrix:
        for col in row:
            matrix_sum += col ** 2

    return math.sqrt(matrix_sum)


def manhattan_matrix(matrix):
    matrix_sum = 0

    for row in matrix:
        for col in row:
            matrix_sum += math.fabs(col)

    return matrix_sum


def maximum_matrix(matrix):
    max_element = None

    for row in matrix:
        for col in row:
            if max_element is None or col > max_element:
                max_element = col

    return max_element


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return

    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

    for row_a in range(rows_a):
        for col_b in range(cols_b):
            for col_a in range(cols_a):
                result[row_a][col_b] += a[row_a][col_a] * b[col_a][col_b]

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


print("Zadanie 1:")

vec = [1.0, 2.0, 5.0]
print(f"Wektor: {vec}")

print(f"Norma euklidesowa: {euclidean_norm(vec)}")
print(f"Norma Manhattan: {manhattan_norm(vec)}")
print(f"Norma maksimum: {maximum_norm(vec)}")

print()

print("Zadanie 2:")

p, q = (5.0, 7.2), (2.0, 4.1)
print(f"p: {p}, q: {q}")

print(f"Metryka euklidesowa: {euclidean_metric(p, q)}")
print(f"Metryka Manhattan: {manhattan_metric(p, q)}")
print(f"Metryka rzeki: {river_metric(p, q)}")
print(f"Metryka kolejowa: {rail_metric(p, q)}")

print()

print("Zadanie 3:")

matrix = [
    [2.0, 1.0],
    [3.0, 4.0]
]

print("Macierz:")
print_matrix(matrix)

print(f"Metryka Frobeniusa: {frobenius_matrix(matrix)}")
print(f"Metryka Manhattan: {manhattan_matrix(matrix)}")
print(f"Metryka maksimum: {maximum_matrix(matrix)}")

print()

print("Zadanie 4:")

matrix2 = [
    [2.0, 2.0],
    [4.0, 2.0]
]

print("Macierz A:")
print_matrix(matrix)

print()

print("Macierz B:")
print_matrix(matrix2)

print()

print("Wynik mnożenia A * B:")
print_matrix(multiply_matrices(matrix, matrix2))

print()

print("Sprawdzenie przemienności:")

print("Wynik mnożenia A * B:")
result_a = multiply_matrices(matrix, matrix2)
print_matrix(result_a)

print()

print("Wynik mnożenia B * A:")
result_b = multiply_matrices(matrix2, matrix)
print_matrix(result_b)

print()

print(f"Przemienność mnożenia macierzy: {result_a == result_b}")

print()

print("Sprawdzenie łączności:")

matrix3 = [
    [4.0, 5.0],
    [2.0, 1.0]
]

print("Macierz C:")
print_matrix(matrix3)

print()

print("Wynik mnożenia (A * B) * C:")

temp = multiply_matrices(matrix, matrix2)
result_a = multiply_matrices(temp, matrix3)

print_matrix(result_a)

print()

print("Wynik mnożenia A * (B * C):")

temp = multiply_matrices(matrix2, matrix3)
result_b = multiply_matrices(matrix, temp)

print_matrix(result_b)

print()

print(f"Łączność mnożenia macierzy: {result_a == result_b}")

print()

print("Zadanie 5:")

matrix_class = Matrix(matrix)

print("Macierz A utworzona klasą:")
matrix_class.print()

print()

print("Wynik mnożenia macierzy przez stałą x = 5:")
result = matrix_class.multiply_by_value(5.0)
result.print()

print()

matrix_class2 = Matrix(matrix2)

print("Macierz B utworzona klasą:")
matrix_class2.print()

print()

print("Wynik dodawania A + B:")
result = matrix_class.add(matrix_class2)
result.print()

print()

print("Wynik mnożenia A * B:")
result = matrix_class.multiply(matrix_class2)
result.print()

print()

print("Wynik mnożenia B * A:")
result = matrix_class2.multiply(matrix_class)
result.print()
