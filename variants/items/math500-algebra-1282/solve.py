# Count real x >= 0 such that sqrt(N - sqrt(x)) is an integer k.
# Need k >= 0 integer, s = N - k^2 = sqrt(x) >= 0, so x = (N - k^2)^2. Count distinct x.
from math import isqrt
from fractions import Fraction

def count(N):
    xs = set()
    for k in range(0, 10 * N + 10):  # brute-force over a wide range of k
        s = N - k * k
        if s < 0:
            continue
        x = s * s
        # independent check: recompute expression exactly
        r = N - isqrt(x)
        assert isqrt(x) ** 2 == x and r >= 0 and isqrt(r) ** 2 == r and isqrt(r) == k
        xs.add(x)
    return len(xs)

orig = count(120)
print("original (N=120):", orig)
assert orig == 11
var = count(150)
print("variant (N=150):", var)
