import math
import numpy as np


def generate_vector(n, m):
    vector = np.zeros(n, dtype=np.float32)

    for k in range(n):
        a = np.float32(1.0) / ((k % m + np.float32(1.0)) * (k % m + np.float32(2.0)))
        vector[k] = a

    return vector


def generate_vector_double(n, m):
    vector = [0.0 for _ in range(n)]

    for k in range(n):
        a = 1.0 / ((k % m + 1.0) * (k % m + 2.0))
        vector[k] = a

    return vector


def sum_vector(vector):
    sum = np.float32(0.0)

    for k in range(len(vector)):
        sum += vector[k]

    return sum


def sum_vector_double(vector):
    sum = 0.0

    for k in range(len(vector)):
        sum += vector[k]

    return sum


def sum_gill_moller(vector):
    sum = np.float32(0.0)
    p = np.float32(0.0)
    sum_old = np.float32(0.0)

    for i in range(len(vector)):
        sum = sum_old + vector[i]
        p = p + (vector[i] - (sum - sum_old))
        sum_old = sum

    return sum + p


def sum_gill_moller_double(vector):
    sum = 0.0
    p = 0.0
    sum_old = 0.0

    for i in range(len(vector)):
        sum = sum_old + vector[i]
        p = p + (vector[i] - (sum - sum_old))
        sum_old = sum

    return sum + p


def sum_kahan(vector):
    sum = np.float32(0.0)
    e = np.float32(0.0)

    for i in range(len(vector)):
        temp = sum
        y = vector[i] + e
        sum = temp + y
        e = (temp - sum) + y

    return sum


def sum_kahan_double(vector):
    sum = 0.0
    e = 0.0

    for i in range(len(vector)):
        temp = sum
        y = vector[i] + e
        sum = temp + y
        e = (temp - sum) + y

    return sum


def check_precision(n, m, sum):
    precise_sum = n / (m + 1)
    absolute_error = math.fabs(sum - precise_sum) / precise_sum

    return absolute_error


n = 2 ** 20
m = 512

print("Zadanie 1:")
vec = generate_vector(n, m)
print(f"Wektor: {vec}")

print()

print("Zadanie 2:")
sum = sum_vector(vec)
print(f"Suma zwykła: {sum:.16f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")

print()

print("Zadanie 3:")
sum = sum_gill_moller(vec)
print(f"Suma Gilla-Møllera: {sum:.16f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")

print()

print("Zadanie 4:")
sum = sum_kahan(vec)
print(f"Suma Kahana: {sum:.16f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")

print()

print("Zadanie 5:")

vec = generate_vector_double(n, m)

sum = sum_vector_double(vec)
print(f"Suma zwykła: {sum:.32f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")

print()

sum = sum_gill_moller_double(vec)
print(f"Suma Gilla-Møllera: {sum:.32f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")

print()

sum = sum_kahan_double(vec)
print(f"Suma Kahana: {sum:.32f}")

error = check_precision(n, m, sum)
print(f"Błąd: {error:e}")
