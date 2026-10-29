from sympy import Rational, symbols, diff, solve, simplify
from fractions import Fraction

def min_dist_sq(k, c):
    """Min of x^2 + (k x^2 - c)^2 over real x, exact via sympy (t = x^2 >= 0)."""
    t = symbols('t', real=True)
    f = t + (k*t - c)**2
    crit = [r for r in solve(diff(f, t), t) if r >= 0]
    cands = [f.subs(t, 0)] + [f.subs(t, r) for r in crit]
    return simplify(min(cands))

def numeric_check(k, c):
    k, c = float(k), float(c)
    best = min(x*x + (k*x*x - c)**2 for x in [i/10000 for i in range(-200000, 200001)])
    return best

orig = min_dist_sq(Rational(1, 2), 9)
print("original a^2 =", orig, "numeric", round(numeric_check(0.5, 9), 6))
assert orig == 17

var = min_dist_sq(Rational(1, 4), 6)
print("variant a^2 =", var, "numeric", round(numeric_check(0.25, 6), 6))
