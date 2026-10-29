from math import factorial
def count(n, k=3):
    N = factorial(n)
    x = 1; c = 0
    while x**k <= N:
        if N % x**k == 0: c += 1
        x += 1
    return c
orig = count(10)
print("original (10!, cubes):", orig); assert orig == 6
print("variant (12!, cubes):", count(12))
