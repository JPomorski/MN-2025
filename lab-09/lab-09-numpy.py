import numpy as np
import matplotlib.pyplot as plt


def gauss(A, B):
    n = len(B)

    for i in range(n):
        max_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        B[i], B[max_row] = B[max_row], B[i]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (B[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x


def linear_approximate(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    n = len(points)

    A = np.sum(x * y)
    B = np.sum(x)
    C = np.sum(y)
    D = np.sum(x**2)

    m = n * D - B ** 2

    if m == 0:
        raise ValueError("Dzielenie przez zero")

    a = (n * A - B * C) / m
    b = (C * D - A * B) / m

    return a, b


points = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2), (2.8, 3.6), (3.0, 4.2)]

a, b = linear_approximate(points)

x_points = np.array([p[0] for p in points])
y_points = np.array([p[1] for p in points])

print("Zadanie 1:")
print(f"Zbiór punktów: {points}")
print(f"Dopasowany wielomian: y = {a:.4f}x + {b:.4f}\r\n")

x_min = x_points.min()
x_max = x_points.max()

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
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    n = len(x)

    A = np.array([
        [np.sum(x**4), np.sum(x**3), np.sum(x**2)],
        [np.sum(x**3), np.sum(x**2), np.sum(x)],
        [np.sum(x**2), np.sum(x), n]
    ])

    B = np.array([
        np.sum(x**2 * y),
        np.sum(x * y),
        np.sum(y)
    ])

    return gauss(A, B)


points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
a, b, c = exponential_approximate(points)

print("Zadanie 2:")
print(f"Zbiór punktów: {points}")
print(f"Dopasowany wielomian: y = {a:.4f}x² + {b:.4f}x + {c:.4f}\r\n")

x_vals = np.array([p[0] for p in points])
y_vals = np.array([p[1] for p in points])

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
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    A = np.zeros((degree + 1, degree + 1))
    B = np.zeros(degree + 1)

    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i, j] = np.sum(x ** (i + j))
        B[i] = np.sum((x ** i) * y)

    c = gauss(A, B)

    y_pred = sum(c[i] * x ** i for i in range(degree + 1))
    mse = np.mean((y - y_pred) ** 2)

    return c[::-1], mse


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
