# Count perfect matchings of the vertices of a regular n-gon by n/2 segments of equal length.
# Brute force: for each chord length (step k), count perfect matchings using only step-k chords
# via backtracking; also compare with the closed form (gcd cycle decomposition).
from math import gcd
from functools import lru_cache

def brute(n):
    total = 0
    for k in range(1, n // 2 + 1):
        @lru_cache(maxsize=None)
        def count(mask):
            if mask == (1 << n) - 1:
                return 1
            i = next(j for j in range(n) if not mask >> j & 1)
            res = 0
            for j in {(i + k) % n, (i - k) % n}:
                if j != i and not mask >> j & 1:
                    res += count(mask | 1 << i | 1 << j)
            return res
        total += count(0)
    return total

def formula(n):
    t = 0
    for k in range(1, n // 2 + 1):
        d = gcd(n, k); L = n // d
        t += 1 if L == 2 else (2 ** d if L % 2 == 0 else 0)
    return t

orig = brute(24); assert orig == formula(24)
print("original (24-gon):", orig, "expected 113 ->", orig == 113)
var = brute(28); assert var == formula(28)
print("variant (28-gon):", var)
