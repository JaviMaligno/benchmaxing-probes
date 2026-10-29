from fractions import Fraction as F
import sympy as sp

def min_rate(wage, target, years=3):
    x = sp.symbols('x', positive=True)
    poly = sum(wage * x**k for k in range(years)) - target
    roots = [r for r in sp.solve(sp.Eq(poly, 0), x) if r.is_real and r > 0]
    assert len(roots) == 1
    r = (roots[0] - 1) * 100
    # independent exact check: brute force over rates in hundredths of a percent
    best = None
    for bp in range(0, 10000):
        g = 1 + F(bp, 10000)
        if sum(wage * g**k for k in range(years)) >= target:
            best = F(bp, 100); break
    assert best == sp.Rational(r), (best, r)
    return sp.nsimplify(r)

orig = min_rate(20000, 66200)
print("original:", orig)
assert orig == 10
var = min_rate(25000, 84360)
print("variant:", var)
