# Brute force: count pandigital numbers (over a digit set) equal to twice another pandigital.
from itertools import permutations

def count(digits, k=2):
    target = sorted(str(d) for d in digits)
    c = 0
    for p in permutations(digits):
        if p[0] == 0:
            continue
        n = int(''.join(map(str, p)))
        if sorted(str(k * n)) == target:
            c += 1  # k*n is a pandigital that is exactly twice the pandigital n
    return c

orig = count(range(10))
print("original (digits 0-9):", orig, "expected 184320", orig == 184320)
var = count(range(1, 10))
print("variant (digits 1-9):", var)
