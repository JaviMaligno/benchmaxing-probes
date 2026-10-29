from sympy import symbols, Rational, solve, sqrt, nsimplify
from fractions import Fraction

def exact(R):
    r = symbols('r', positive=True)
    # C = midpoint of QA (larger semicircle on diameter QA, radius R/2)
    # D on QB with DB = r (smaller semicircle on QB, ending at B), tangent externally to the larger one
    sols = solve((R - r)**2 + (Rational(R, 2))**2 - (Rational(R, 2) + r)**2, r)
    sols = [s for s in sols if 0 < s < R]
    assert len(sols) == 1
    return sols[0]

def numeric(R):
    # independent bisection: distance between centers minus sum of radii
    import math
    f = lambda r: math.hypot(R/2, R - r) - (R/2 + r)
    lo, hi = 1e-12, R/2
    for _ in range(200):
        mid = (lo + hi)/2
        if f(lo)*f(mid) <= 0: hi = mid
        else: lo = mid
    return (lo+hi)/2

orig = exact(14)
print("original R=14:", orig, "numeric", numeric(14))
assert orig == Rational(14, 3)
var = exact(20)
print("variant R=20:", var, "numeric", numeric(20))
assert abs(float(var) - numeric(20)) < 1e-9
