import math


def f_a(x):
    return x ** 2


def f_b(x):
    return math.cos(x)


def f_c(x):
    return 1/x


def rectangle_method(f, a, b, n):
    h = (b - a) / n
    sum = 0

    for i in range(n):
        xi = a + i * h
        midpoint = xi + h / 2
        sum += f(midpoint)

    return h * sum


def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        sum += 2 * f(xi)

    return (h / 2) * sum


def simpson_method(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h

        if i % 2 == 0:
            sum += 2 * f(xi)
        else:
            sum += 4 * f(xi)

    return (h / 3) * sum


def calculate_error(i_num, i_dok):
    return math.fabs((i_num - i_dok) / i_dok)


a_1, b_1 = 0, 1
a_2, b_2 = 0, math.pi / 2
a_3, b_3 = math.e, math.e ** 2

functions = [rectangle_method, trapezoid_method, simpson_method]
i_doks = [1/3, 1, 1]

print("Przykład a):")
print()

result_a = rectangle_method(f_a, a_1, b_1, 100)
result_b = trapezoid_method(f_a, a_1, b_1, 100)
result_c = simpson_method(f_a, a_1, b_1, 100)

print("Wyniki:")
print("Prostokąty:", result_a)
print("Trapezy:", result_b)
print("Simpson:", result_c)
print()

err_a = calculate_error(result_a, i_doks[0])
err_b = calculate_error(result_b, i_doks[0])
err_c = calculate_error(result_c, i_doks[0])

print("Błąd względny:")
print("Prostokąty:", err_a)
print("Trapezy:", err_b)
print("Simpson:", err_c)
print()

print("====================================")
print()

print("Przykład b):")
print()

result_a = rectangle_method(f_b, a_2, b_2, 100)
result_b = trapezoid_method(f_b, a_2, b_2, 100)
result_c = simpson_method(f_b, a_2, b_2, 100)

print("Wyniki:")
print("Prostokąty:", result_a)
print("Trapezy:", result_b)
print("Simpson:", result_c)
print()

err_a = calculate_error(result_a, i_doks[1])
err_b = calculate_error(result_b, i_doks[1])
err_c = calculate_error(result_c, i_doks[1])

print("Błąd względny:")
print("Prostokąty:", err_a)
print("Trapezy:", err_b)
print("Simpson:", err_c)
print()

print("====================================")
print()

print("Przykład c):")
print()

result_a = rectangle_method(f_c, a_3, b_3, 100)
result_b = trapezoid_method(f_c, a_3, b_3, 100)
result_c = simpson_method(f_c, a_3, b_3, 100)

print("Wyniki:")
print("Prostokąty:", result_a)
print("Trapezy:", result_b)
print("Simpson:", result_c)
print()

err_a = calculate_error(result_a, i_doks[2])
err_b = calculate_error(result_b, i_doks[2])
err_c = calculate_error(result_c, i_doks[2])

print("Błąd względny:")
print("Prostokąty:", err_a)
print("Trapezy:", err_b)
print("Simpson:", err_c)
print()
