def lagrange_interpolate(x_vals, y_vals, x):
    n = len(x_vals)
    result = 0.0

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if j != i:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term

    return result


x_vals = [4, 2, 0, 3]
y_vals = [63, 11, 7, 28]

values = [(x_vals[i], y_vals[i]) for i in range(len(x_vals))]
print(f"Zbiór punktów: {values}")

x_value = 1

result = lagrange_interpolate(x_vals, y_vals, x_value)
print(f"Wynik interpolacji Lagrange'a w punkcie x = 1: {result}")
