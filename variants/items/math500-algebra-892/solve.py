# f(x) = a x^2 (x >= a), a x + c a (x < a). Largest a such that every horizontal line meets the graph.
from fractions import Fraction as F
import sympy as sp

def covers(a, c):
    """Exact interval analysis of the range of f (union of the two pieces' ranges must be all of R)."""
    if a == 0:
        return False
    # parabola piece on [a, inf)
    if a > 0:
        par = (a * a * a, True, None)          # [a^3, +inf)
        lin = (None, a * a + c * a, False)      # (-inf, a^2+ca)
        lo_par = a ** 3
        hi_lin = a * a + c * a
        return hi_lin >= lo_par               # gap closed (equality: line open end covered by parabola closed end)
    else:
        # a<0: x>=a contains 0, a x^2 ranges over (-inf, 0]; line slope<0 on x<a gives (a^2+ca, inf)
        return a * a + c * a <= 0

HEIGHTS = [k / 1000 for k in range(-200000, 200001)]

def numeric_check(a, c, heights=HEIGHTS):
    """Independent check: does each horizontal line y=h hit the graph? Solve each piece directly."""
    a = float(a)
    for h in heights:
        hit = False
        # parabola: a x^2 = h, x >= a
        if a != 0 and h / a >= 0:
            r = (h / a) ** 0.5
            if r >= a - 1e-12 or -r >= a - 1e-12:
                hit = True
        # line: a x + c a = h, x < a
        if not hit and a != 0:
            x = h / a - c
            if x < a - 1e-12:
                hit = True
        if not hit:
            return False
    return True

def largest_a(c):
    grid = [F(k, 100) for k in range(-2000, 2001)]
    good = [a for a in grid if covers(a, c)]
    best = max(good)
    # agree with numeric check around the boundary
    for a in grid:
        if abs(a - best) <= F(1, 10):
            assert covers(a, c) == numeric_check(a, c), (a, c)
    # exact symbolic boundary for a>0: a^2 + c a >= a^3  <=> a^2 - a - c <= 0
    A = sp.symbols('a', positive=True)
    root = max(sp.solve(sp.Eq(A**2 - A - c, 0), A))
    assert sp.nsimplify(best) == root, (best, root)
    return root

orig = largest_a(2)
print("original (c=2):", orig)
assert orig == 2
var = largest_a(6)
print("variant (c=6):", var)
