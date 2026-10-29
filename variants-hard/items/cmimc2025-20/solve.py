# Brute-force a_n mod 3 (ordered sums of powers of 3) up to 3^K, record
# f(k) = sum_{n=1}^{3^k} b_n, fit a closed form on k>=2, verify on all data,
# then evaluate at original exponent 2025 and variant exponent 2030.
from fractions import Fraction
K = 13
N = 3**K
P = [3**i for i in range(K+1)]
a = [0]*(N+1); a[0] = 1
for n in range(1, N+1):
    s = 0
    for p in P:
        if p > n: break
        s += a[n-p]
    a[n] = s % 3
f = {}; S = 0
for n in range(1, N+1):
    S += a[n]
    if n in P: f[P.index(n)] = S
print("brute f(k):", f)
# fit quadratic through k=2,3,4 by Lagrange, check on k=2..K
pts = [(2, f[2]), (3, f[3]), (4, f[4])]
def lag(x):
    tot = Fraction(0)
    for i, (xi, yi) in enumerate(pts):
        t = Fraction(yi)
        for j, (xj, _) in enumerate(pts):
            if j != i: t *= Fraction(x - xj, xi - xj)
        tot += t
    return tot
assert all(lag(k) == f[k] for k in range(2, K+1)), "quadratic fit fails"
assert all(lag(k) == k*k + k + 2 for k in range(2, K+1))
orig = lag(2025); var = lag(2030)
print("original (3^2025):", orig, "expected 4102652, match:", orig == 4102652)
print("variant  (3^2030):", var)
