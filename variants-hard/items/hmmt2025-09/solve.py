from fractions import Fraction
from math import isqrt, factorial
from sympy import isprime, interpolate, symbols, Poly

def exact_r(p):
    """Exact rational coefficient of x^{p-2} in the Lagrange interpolant on nodes 1..p
    of the square indicator, then r = a * b^{-1} mod p."""
    nodes = range(1, p + 1)
    S = sum(nodes)
    c = Fraction(0)
    for k in range(1, isqrt(p) + 1):
        a = k * k
        # prod_{j != a} (a - j) = (a-1)! * (-1)^{p-a} (p-a)!
        den = factorial(a - 1) * factorial(p - a) * (-1) ** (p - a)
        c += Fraction(-(S - a), den)
    A, B = c.numerator, c.denominator
    assert B % p != 0
    return (A * pow(B, -1, p)) % p

def formula_r(p):
    # Over F_p: L_a(x) = 1 - (x-a)^{p-1}; x^{p-2} coefficient is -a.
    return (-sum(k * k for k in range(1, isqrt(p) + 1))) % p

def brute_r(p):
    x = symbols('x')
    pts = [(n, 1 if isqrt(n) ** 2 == n else 0) for n in range(1, p + 1)]
    f = Poly(interpolate(pts, x), x)
    c = Fraction(str(f.coeff_monomial(x ** (p - 2))))
    return (c.numerator * pow(c.denominator, -1, p)) % p

for p in [11, 13, 17, 19, 23, 29]:
    assert brute_r(p) == exact_r(p) == formula_r(p), p
print("small-prime brute force cross-check OK")

orig = exact_r(2027)
print("original p=2027:", orig, "formula:", formula_r(2027), "matches 1037:", orig == 1037)
assert isprime(2029)
var = exact_r(2029)
print("variant p=2029:", var, "formula:", formula_r(2029))
