import numpy as np
import math


def f(x):
    return math.sqrt((x ** 2) + 1.0) - 1.0


def g(x):
    return x ** 2 / (math.sqrt((x ** 2) + 1.0) + 1.0)


def epsilon_float(eps: np.float32):
    return 1.0 == 1.0 + eps


def epsilon(eps):
    return 1.0 == 1.0 + eps


a = 0.1
b = 0.2

sum64 = a + b
sum32 = np.float32(a) + np.float32(b)

print("Zadanie 1:")

print("Suma (float):", sum32)
print("Suma (double):", sum64)

print()

expected = 0.3

print(f"Czy suma float = 0.3? {sum32 == expected}")
print(f"Czy suma double = 0.3? {sum64 == expected}")

print()

print("Zadanie 2:")

a = 100000000.0
b = 0.1

print(f"Wynik działania {a} + {b} - {a}: {a + b - a}")

print()

print("Zadanie 3:")

a = 0.1
b = 0.2

c = a + b

print(f"Wynik działania {a} + {b}:")
print(f"Double: {c:.20f}")
print(f"Float: {np.float32(c):.20f}")

print()

print("Zadanie 4:")

a = 0.3
b = 3
c = 0.1

result = a * b + c

print(f"Wynik działania {a} * {b} + {c}: {result}")
print(f"Floor: {math.floor(result)}")
print(f"Ceil: {math.ceil(result)}")

print()

print("Zadanie 5:")

print(f"Wynik działania 1.0000001 - 1.0000000: {1.0000001 - 1.0000000}")
print(f"Wynik działania 1.0000002 - 1.0000001: {1.0000002 - 1.0000001}")

print()

print("Zadanie 6:")

try:
    result_a = 1.0 / 0.0
except ZeroDivisionError as e:
    result_a = f"Błąd: '{e}'"

try:
    result_b = 0.0 / 0.0
except ZeroDivisionError as e:
    result_b = f"Błąd: '{e}'"

print(f"Wynik dzielenia 1.0 / 0.0: {result_a}")
print(f"Wynik dzielenia 0.0 / 0.0: {result_b}")

print()

print("Zadanie 7:")

e_f = np.float32(1.0)

while not epsilon_float(e_f):
    e_f = e_f / 2

e_d = 1.0

while not epsilon(e_d):
    e_d = e_d / 2

print(f"Końcowy epsilon dla float: {e_f:.32f}")
print(f"Końcowy epsilon dla double: {e_d:.32f}")

print()

print("Zadanie 8:")

sum_a = 0.0

for _ in range(1000000):
    sum_a += 0.0001

result_b = 1000000 * 0.0001

print(f"Wynik sumowania: {sum_a:.20f}")
print(f"Wynik mnożenia: {result_b:.20f}")

print()

print("Zadanie 9:")

sum_a = 0.0

for number in range(1, 1000001):
    sum_a += 1.0 / number

sum_b = 0.0

for number in range(1000000, 0, -1):
    sum_b += 1.0 / number

print(f"Wynik sumowania w górę: {sum_a:.20f}")
print(f"Wynik sumowania w dół: {sum_b:.20f}")

print()

print("Zadanie 10:")

iterations = 10

for i in range(1, iterations + 1):
    print(f"f(x) dla x = 8^-{i}: {f(8 ** -i):.24f}")
    print(f"g(x) dla x = 8^-{i}: {g(8 ** -i):.24f}")
    print()
