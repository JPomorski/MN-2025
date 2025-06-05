import cmath


def horner(coefficients, x):
    result = coefficients[0]

    for c in coefficients[1:]:
        result = result * x + c

    return result


def derivative_at(coefficients, x):
    n = len(coefficients) - 1

    result = coefficients[0] * n

    for i in range(1, n):
        result = result * x + coefficients[i] * (n - i)

    return result


def second_derivative_at(coefficients, x):
    n = len(coefficients) - 1

    if n < 2:
        return 0

    der = [coefficients[i] * (n - i) for i in range(n)]
    return derivative_at(der, x)


def derivative(coefficients):
    n = len(coefficients) - 1

    result = [0 for _ in range(n)]

    for i in range(n):
        result[i] = coefficients[i] * (n - i)

    return result


def second_derivative(coefficients):
    return derivative(derivative(coefficients))


def laguerre(coefficients, x0, max_iter=100, tolerance=1e-12):
    n = len(coefficients) - 1
    x = x0

    for _ in range(max_iter):
        p = horner(coefficients, x)

        if abs(p) < tolerance:
            return x

        p_prime = derivative_at(coefficients, x)
        p_double_prime = second_derivative_at(coefficients, x)

        g = p_prime / p
        h = g * g - p_double_prime / p
        d_sqrt = cmath.sqrt((n - 1) * (n * h - g * g))

        d1 = g + d_sqrt
        d2 = g - d_sqrt
        d = d1 if abs(d1) > abs(d2) else d2

        a = n / d
        x_new = x - a

        if abs(x_new - x) < tolerance:
            return x_new

        x = x_new

    return x


def deflate(coefficients, root):
    n = len(coefficients)
    new_c = [coefficients[0]]

    for i in range(1, n - 1):
        new_c.append(coefficients[i] + new_c[-1] * root)

    r = coefficients[-1] + new_c[-1] * root

    return new_c, r


def all_roots(coefficients, max_iter=100, tolerance=1e-12):
    roots = []
    c = coefficients[:]

    while len(c) > 2:
        x0 = complex(0.4, 0.9)
        root = laguerre(c, x0, max_iter, tolerance)
        roots.append(root)
        c, _ = deflate(c, root)

    if len(c) == 2:
        root = -c[1] / c[0]
        roots.append(root)

    return roots


c_1 = [1, -6, 11, -6]
c_2 = [1, -6, 11, -1]
c_3 = [39205740, -147747493, 173235338, 2869080, -158495872, 118949888, -28016640]
c_4 = [39205740, -147747493, 173235338, 2869080, -158495872, 118949888, -28016640, 1]

x_value = 4

result_a = horner(c_1, x_value)
result_b = horner(c_2, x_value)
result_c = horner(c_3, x_value)
result_d = horner(c_4, x_value)

print("Zadanie 1:")
print(f"x = {x_value}")
print(f"a) {result_a}")
print(f"b) {result_b}")
print(f"c) {result_c}")
print(f"d) {result_d}")

print()

result_a = derivative_at(c_1, x_value)
result_b = derivative_at(c_2, x_value)
result_c = derivative_at(c_3, x_value)
result_d = derivative_at(c_4, x_value)

print("Zadanie 2:")
print(f"x = {x_value}")

print("Pierwsza pochodna:")
print(f"a) {result_a}")
print(f"b) {result_b}")
print(f"c) {result_c}")
print(f"d) {result_d}")

print()

result_a = second_derivative_at(c_1, x_value)
result_b = second_derivative_at(c_2, x_value)
result_c = second_derivative_at(c_3, x_value)
result_d = second_derivative_at(c_4, x_value)

print("Druga pochodna:")
print(f"a) {result_a}")
print(f"b) {result_b}")
print(f"c) {result_c}")
print(f"d) {result_d}")

print()

print("Zadanie 3:")
print(f"x = {x_value}")

result_a = laguerre(c_1, x_value)
result_b = laguerre(c_2, x_value)
result_c = laguerre(c_3, x_value)
result_d = laguerre(c_4, x_value)

print("Laguerre:")
print(f"a) {result_a}")
print(f"b) {result_b}")
print(f"c) {result_c}")
print(f"d) {result_d}")

print()

print("Zadanie 4:")
print(f"x = {x_value}")

result_a = all_roots(c_1)
result_b = all_roots(c_2)
result_c = all_roots(c_3)
result_d = all_roots(c_4)

print("Wszystkie pierwiastki:")
print(f"a) {result_a}")
print(f"b) {result_b}")
print(f"c) {result_c}")
print(f"d) {result_d}")
