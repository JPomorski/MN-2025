import math


def f_a(x):
    return 2 * x ** 2 + 2


def f_b(x):
    return 2 * x ** 4 - x ** 2 + 3 * x - 7


def f_c(x):
    return x ** 2 * math.exp(x)


def f_p_a(x):
    return x * 4


def f_p_b(x):
    return 8 * x ** 3 - 2 * x + 3


def f_p_c(x):
    return (2 * x + x ** 2) * math.exp(x)


def newton_method(f, x, h):
    return (f(x + h) - f(x)) / h


def backwards_difference(f, x, h):
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def forward_three_point_difference(f, x, h):
    return ((-3 * f(x)) + (4 * f(x + h)) - f(x + 2 * h)) / (2 * h)


def backwards_three_point_difference(f, x, h):
    return ((3 * f(x)) - (4 * f(x - h)) + f(x - 2 * h)) / (2 * h)


def central_four_point_difference(f, x, h):
    return ((f(x - 2 * h)) - (8 * f(x - h)) + (8 * f(x + h)) - f(x + 2 * h)) / (12 * h)


def lagrange_base(x, x_nodes, i):
    n = len(x_nodes)
    li = 1

    for j in range(n):
        if j != i:
            li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])

    return li


def lagrange_inter(x, x_nodes, y_nodes, n):
    sum = 0

    for i in range(n):
        sum += y_nodes[i] * lagrange_base(x, x_nodes, i)

    return sum


def lagrange(x, x_nodes, y_nodes, h, n):
    sum = lagrange_inter(x + h, x_nodes, y_nodes, n) - lagrange_inter(x - h, x_nodes, y_nodes, n)
    return sum / (2 * h)


def calculate_error(f_num, f_dok):
    return math.fabs((f_num - f_dok) / f_dok)


def calc(method):
    for h in [1e-2, 1e-4]:
        print(f"h = {h}")
        result_a = method(f_a, x_value, h)
        result_b = method(f_b, x_value, h)
        result_c = method(f_c, x_value, h)

        print(f"a): {result_a}")
        print(f"b): {result_b}")
        print(f"c): {result_c}")

        print()

        print(f"Błąd a) {calculate_error(result_a, dok_a):e}")
        print(f"Błąd b) {calculate_error(result_b, dok_b):e}")
        print(f"Błąd c) {calculate_error(result_c, dok_c):e}")

        print()

    print("===================================")
    print()


functions = [f_a, f_b, f_c]

x_value = 3

dok_a = f_p_a(x_value)
dok_b = f_p_b(x_value)
dok_c = f_p_c(x_value)

print("Wartości dokładne:")
print(f"a) {dok_a}")
print(f"b) {dok_b}")
print(f"c) {dok_c}")
print()


print("Zadanie 1:")
print("Metoda Newtona:")
calc(newton_method)

print("Zadanie 2:")
print("Metoda wsteczna:")
calc(backwards_difference)

print("Metoda centralna:")
calc(central_difference)

print("Zadanie 3:")
print("Metoda trzypunktowa:")
calc(forward_three_point_difference)

print("Metoda wsteczna trzypunktowa:")
calc(backwards_three_point_difference)

print("Metoda centralna czteropunktowa:")
calc(central_four_point_difference)

nodes = [(1, 4), (2, 10), (3, 20), (4, 34), (5, 52)]

x_nodes = [node[0] for node in nodes]
y_nodes = [node[1] for node in nodes]

print("Zadanie 4:")
print("Wielomian Lagrange'a:")
result = lagrange(3.5, x_nodes, y_nodes, 1e-4, len(nodes))
print(result)

