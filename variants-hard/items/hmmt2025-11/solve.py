from itertools import permutations

def count(n, bound):
    """Labelled circular arrangements of 1..n (rotations/reflections distinct)
    with every adjacent product <= bound."""
    total = 0
    for p in permutations(range(1, n + 1)):
        if all(p[i] * p[(i + 1) % n] <= bound for i in range(n)):
            total += 1
    return total

def count_fixed(n, bound):
    """Independent check: fix 1 in position 0, count, multiply by n rotations."""
    t = 0
    for p in permutations(range(2, n + 1)):
        q = (1,) + p
        if all(q[i] * q[(i + 1) % n] <= bound for i in range(n)):
            t += 1
    return t * n

orig = count(7, 20)
assert orig == count_fixed(7, 20)
print("original (1..7, <=20):", orig)
assert orig == 56
var = count(8, 24)
assert var == count_fixed(8, 24)
print("variant (1..8, <=24):", var)
