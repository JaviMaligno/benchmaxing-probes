# Variant check: area of {(a,b) in [0,1]^2 : x^4 + k a x^3 - b x^2 + k a x + 1 has a real root}
# Original: k=1 (answer 1/4). Variant: k=2.
import numpy as np
from fractions import Fraction
import sympy as sp

def has_real_root(a, b, k):
    r = np.roots([1, k*a, -b, k*a, 1])
    return bool(np.any(np.abs(r.imag) < 1e-7))

def threshold_b(a, k):
    # smallest b in [0,1] with a real root (monotone in b); returns 1 if none
    if has_real_root(a, 0.0, k): return 0.0
    if not has_real_root(a, 1.0, k): return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(50):
        m = (lo+hi)/2
        if has_real_root(a, m, k): hi = m
        else: lo = m
    return hi

def numeric_area(k, n=4000):
    xs = (np.arange(n)+0.5)/n
    return float(np.mean([1 - threshold_b(a, k) for a in xs]))

def exact_area(k):
    # derived condition (y = x+1/x): k a + sqrt(k^2 a^2 + 4(b+2)) >= 4  <=>  2 k a + b >= 2
    a, b = sp.symbols('a b')
    # area = integral over a of (1 - clamp(2 - 2 k a, 0, 1))
    f = 1 - sp.Min(1, sp.Max(0, 2 - 2*k*a))
    return sp.nsimplify(sp.integrate(sp.Piecewise((f, True)), (a, 0, 1)).simplify())

for k, label in [(1, "original"), (2, "variant")]:
    ex = exact_area(k)
    nu = numeric_area(k)
    print(f"{label}: exact = {ex}, numeric = {nu:.6f}")
assert exact_area(1) == sp.Rational(1, 4)
assert exact_area(2) == sp.Rational(5, 8)
