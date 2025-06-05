import matplotlib.pyplot as plt


def gauss(A, B):
    size = len(B)

    for i in range(size):
        max_row = max(range(i, size), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        for j in range(i + 1, size):
            factor = A[j][i] / A[i][i]
            for k in range(i, size):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    x = [0] * size

    for i in range(size - 1, -1, -1):
        x[i] = (B[i] - sum(A[i][j] * x[j] for j in range(i + 1, size))) / A[i][i]

    return x


def linear_approximate(points):
    n = len(points)

    A = sum(x * y for x, y in points)
    B = sum(x for x, _ in points)
    C = sum(y for _, y in points)
    D = sum(x ** 2 for x, _ in points)

    m = n * D - B ** 2

    if m == 0:
        raise ValueError("Dzielenie przez zero")

    a = (n * A - B * C) / m
    b = (C * D - A * B) / m

    return a, b


points = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2), (2.8, 3.6), (3.0, 4.2)]

a, b = linear_approximate(points)

x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

print("Zadanie 1:")
print(f"Zbiór punktów: {points}")
print(f"Dopasowany wielomian: y = {a:.4f}x + {b:.4f}\r\n")

x_min = min(x_points)
x_max = max(x_points)

x_line = [x_min, x_max]
y_line = [a * xi + b for xi in x_line]

plt.scatter(x_points, y_points, color='blue', label='Punkty danych')
plt.plot(x_line, y_line, color='red', label='Aproksymacja liniowa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Liniowa aproksymacja średniokwadratowa')
plt.legend()
plt.grid(True)
plt.show()


def exponential_approximate(points):
    n = len(points)

    sum_x = sum(x for x, _ in points)
    sum_x2 = sum(x**2 for x, _ in points)
    sum_x3 = sum(x**3 for x, _ in points)
    sum_x4 = sum(x**4 for x, _ in points)

    sum_y = sum(y for _, y in points)
    sum_xy = sum(x * y for x, y in points)
    sum_x2y = sum((x**2) * y for x, y in points)

    A = [
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x,  n]
    ]

    B = [sum_x2y, sum_xy, sum_y]

    return gauss(A, B)


points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
a, b, c = exponential_approximate(points)

print("Zadanie 2:")
print(f"Zbiór punktów: {points}")
print(f"Dopasowany wielomian: y = {a:.4f}x² + {b:.4f}x + {c:.4f}\r\n")

x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

x_line = [x/100.0 for x in range(int(min(x_vals)*100), int(max(x_vals)*100 + 1))]
y_line = [a*x**2 + b*x + c for x in x_line]

plt.scatter(x_vals, y_vals, color='blue', label='Punkty danych')
plt.plot(x_line, y_line, color='red', label='Aproksymacja kwadratowa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja średniokwadratowa (wielomian 2. stopnia)')
plt.legend()
plt.grid(True)
plt.show()


def approximate(points, degree):
    n = len(points)
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    A = [[0.0] * (degree + 1) for _ in range(degree + 1)]
    B = [0.0] * (degree + 1)

    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i][j] = sum(x_k ** (i + j) for x_k in x)
        B[i] = sum((x[k] ** i) * y[k] for k in range(n))

    c = gauss(A, B)

    def value(x_val, wsp):
        return sum(wsp[i] * (x_val ** i) for i in range(len(wsp)))

    y_pred = [value(x[i], c) for i in range(n)]

    mse = sum((y[i] - y_pred[i]) ** 2 for i in range(n)) / n

    return list(reversed(c)), mse


points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
degree = 2

print("Zadanie 3:")
print(f"Zbiór punktów: {points}\r\n")

c, mse = approximate(points, degree)

print(f"Współczynniki wielomianu: {c}")
print(f"Błąd średniokwadratowy (MSE): {mse:e}\r\n")

points = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2), (2.8, 3.6), (3.0, 4.2)]
print(f"Zbiór punktów: {points}\r\n")

c, mse = approximate(points, 1)

print(f"Współczynniki wielomianu (Zad 1): {c}")
print(f"Błąd średniokwadratowy (MSE) (Zad 1): {mse:e}\r\n")

points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
print(f"Zbiór punktów: {points}\r\n")

c, mse = approximate(points, 2)

print(f"Współczynniki wielomianu (Zad 2): {c}")
print(f"Błąd średniokwadratowy (MSE) (Zad 2): {mse:e}\r\n")
