import numpy as np


def f1(x):
    return x ** 2 - 4


def df1(x):
    return 2 * x


def ddf1(_x):
    return 2


def f2(x):
    return np.sin(x) - 0.5


def df2(x):
    return np.cos(x)


def ddf2(x):
    return np.sin(x) * -1


def bisection(f, a, b, tolerance=1e-6, iterations=0):
    if f(a) * f(b) >= 0:
        print("Oba punkty są tego samego znaku, nie można zagwarantować miejsca zerowego")
        return

    i = 0
    c = 0

    while i < iterations or iterations == 0:
        c = (a + b) / 2

        if np.abs(f(c)) < tolerance:
            break

        if np.abs(f(c)) == 0:
            print(f"a={a}, b={b} zajęło {i + 1} iteracji")
            return np.abs(c)
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        i += 1

    print(f"a={a}, b={b} zajęło {i + 1} iteracji")

    return np.abs(c)


def newton_method(f, df, ddf, a, b, tolerance=1e-6, iterations=100):
    if f(a) * f(b) >= 0:
        print("Oba punkty są tego samego znaku, nie można zagwarantować miejsca zerowego")
        return

    x = 0
    i = 0

    x0 = (a + b) / 2

    if df(x0) * ddf(x0) < 0:
        x = a
    if df(x0) * ddf(x0) > 0:
        x = b

    while i < iterations:
        h = f(x) / df(x)
        x = x - h

        if np.abs(h) < tolerance:
            break

        i += 1

    print(f"Zakończono po {i + 1} iteracjach")
    return x


def sieczna(f, a, b, tolerance=1e-6, iterations=100):
    x_prev = a
    x_curr = b

    for i in range(iterations):
        f_prev = f(x_prev)
        f_curr = f(x_curr)

        if np.abs(f_curr - f_prev) < 1e-14:
            print("Różnica f(b) - f(a) jest zbyt mała. Metoda zawodzi.")

        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)

        if np.abs(x_next - x_curr) < tolerance:
            print(f"Zakończono po {i + 1} iteracjach")
            return x_next

        x_prev, x_curr = x_curr, x_next

    return x_curr


x_range = (0, 2.2)

x1 = bisection(f1, x_range[0], x_range[1])
x2 = bisection(f2, x_range[0], x_range[1])

print()

print("Zadanie 1:")
print(f"x1: {x1}")
print(f"x2: {x2}")

print()

x1 = newton_method(f1, df1, ddf1, x_range[0], x_range[1])
x2 = newton_method(f2, df2, ddf2, x_range[0], x_range[1])

print()

print("Zadanie 2:")
print(f"x1: {x1}")
print(f"x2: {x2}")

print()

x1 = sieczna(f1, x_range[0], x_range[1])
x2 = sieczna(f2, x_range[0], x_range[1])

print()

print("Zadanie 3:")
print(f"x1: {x1}")
print(f"x2: {x2}")
