import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


def exp_maclaurin(x, n=10):
    result = 0
    factorial = 1

    for n in range(n):
        if n > 0:
            factorial *= n
        result += (x ** n) / factorial

    return result


def sin_maclaurin(x, n=10):
    result = 0
    factorial = 1
    sign = 1

    for n in range(n):
        exponent = 2 * n + 1
        if n > 0:
            factorial *= (2 * n) * (2 * n + 1)
        result += sign * (x ** exponent) / factorial
        sign *= -1

    return result


def newton_coefficients(x, y):
    n = len(x)
    p = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            p[i] = (p[i] - p[i - 1]) / (x[i] - x[i - j])

    return p


def newton_interpolate(x, y, x_point):
    n = len(x)
    p = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            p[i] = (p[i] - p[i - 1]) / (x[i] - x[i - j])

    result = p[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_point - x[i]) + p[i]

    return result


x = 5

mc_start = perf_counter()
mclaren = exp_maclaurin(x, 25)
mc_elapsed = perf_counter() - mc_start

np_start = perf_counter()
numpy = np.exp(x)
np_elapsed = perf_counter() - np_start

print(f"Wynik (McLaren):    {mclaren}")
print(f"Wynik (NumPy):      {numpy}\r\n")

print(f"Błąd bezwzględny:   {abs(mclaren - numpy)}\r\n")

print(f"Czas (McLaren):     {mc_elapsed:f}s")
print(f"Czas (NumPy):       {np_elapsed:f}s\r\n")

x = np.pi / 3

mc_start = perf_counter()
mclaren = sin_maclaurin(x, 25)
mc_elapsed = perf_counter() - mc_start

np_start = perf_counter()
numpy = np.sin(x)
np_elapsed = perf_counter() - np_start

print(f"Wynik (McLaren):    {mclaren}")
print(f"Wynik (NumPy):      {numpy}\r\n")

print(f"Błąd bezwzględny:   {abs(mclaren - numpy)}\r\n")

print(f"Czas (McLaren):     {mc_elapsed:f}s")
print(f"Czas (NumPy):       {np_elapsed:f}s\r\n")

x_vals = [4, 2, 0, 3]
y_vals = [63, 11, 7, 28]

a = newton_coefficients(x_vals, y_vals)
print(f"Wynik (interpolacja Newtona):   {a}")

x_plot = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 100)
y = [newton_interpolate(x_vals, y_vals, x) for x in x_plot]

plt.figure(figsize=(8, 5))
plt.plot(x_plot, y, label="Wielomian Newtona", color="blue")
plt.scatter(x_vals, y_vals, color="red", label="Punkty danych", zorder=5)
plt.title("Interpolacja Newtona")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

x_vals = [4, 2, 0, 3]
y_vals = [63, 11, 7, 28]

x = 1

a = newton_interpolate(x_vals, y_vals, x)
print(f"Wynik (Newton z Hornerem):      {a}")


