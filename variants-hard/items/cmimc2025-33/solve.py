from fractions import Fraction
from sympy import integer_nthroot

def iterate_exact(f, x, k):
    for _ in range(k):
        x = f(x)
    return x

def check_identity(f, d):
    # f^k(n+1/n) == n^(d^k) + n^-(d^k), checked with exact rationals
    for n in range(1, 6):
        for k in range(1, 4):
            x = Fraction(n*n+1, n)
            e = d**k
            assert iterate_exact(f, x, k) == Fraction(n)**e + Fraction(1, n**e)

def works(n, d, P, kmax=4):
    for k in range(1, kmax+1):
        e = d**k
        N = n**e
        val = Fraction(N) + Fraction(1, N)      # = f^k((n^2+1)/n) exactly
        r, _ = integer_nthroot(int(val), P)
        for c in (r-1, r, r+1, r+2):
            if c >= 1 and abs(val - c**P) < Fraction(1, 100):
                return (k, c)
    return None

def smallest(d, P, f, limit=5000):
    check_identity(f, d)
    for n in range(1, limit):
        w = works(n, d, P)
        if w:
            return n, w

f_orig = lambda x: x**4 - 4*x**2 + 2
f_var = lambda x: x**3 - 3*x
o = smallest(4, 144, f_orig)
print("original:", o)
assert o[0] == 512
v = smallest(3, 72, f_var)
print("variant:", v)
