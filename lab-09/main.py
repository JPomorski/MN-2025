import numpy as np
import matplotlib.pyplot as plt

points = [(1.1, 2.1), (1.4, 2.3), (1.8, 2.9), (2.5, 3.2), (2.8, 3.6), (3.0, 4.2)]
x = np.array([p[0] for p in points])
y = np.array([p[1] for p in points])

n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
b = y_mean - a * x_mean

print(f"Wynik aproksymacji: y = {a:.4f}x + {b:.4f}\r\n")

plt.scatter(x, y, color='blue', label='Punkty danych')
plt.plot(x, a * x + b, color='red', label='Aproksymacja liniowa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Liniowa aproksymacja średniokwadratowa')
plt.legend()
plt.grid(True)
plt.show()

points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
x = np.array([p[0] for p in points])
y = np.array([p[1] for p in points])

coefficients = np.polyfit(x, y, deg=2)
a, b, c = coefficients
print(f"Wynik aproksymacji: y = {a:.4f}x² + {b:.4f}x + {c:.4f}\r\n")

x_vals = np.linspace(min(x), max(x), 100)
y_vals = a * x_vals**2 + b * x_vals + c

plt.scatter(x, y, color='blue', label='Punkty danych')
plt.plot(x_vals, y_vals, color='red', label='Aproksymacja kwadratowa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja średniokwadratowa (wielomian 2. stopnia)')
plt.legend()
plt.grid(True)
plt.show()


def approximate(points, degree):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    c = np.polyfit(x, y, deg=degree)

    y_pred = np.polyval(c, x)

    mse = np.mean((y - y_pred) ** 2)

    return c, mse


points = [(0, 2), (0.5, 2.48), (1, 2.84), (1.5, 3), (2, 2.91)]
degree = 2

c, mse = approximate(points, degree)
print(f"Współczynniki wielomianu: {c}")
print(f"Błąd średniokwadratowy (MSE): {mse:.4f}")

