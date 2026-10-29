from fractions import Fraction as F
import sympy as sp

def f(a, b):
    return (a + 1/b) * (1/b - a)

def solve(alo, ahi, blo, bhi):
    # exact: f = 1/b^2 - a^2; max over a box is at a minimising |a|, b minimising |b|
    a, b = sp.symbols('a b', real=True)
    expr = sp.expand((a + 1/b) * (1/b - a))
    assert sp.simplify(expr - (1/b**2 - a**2)) == 0
    cands = [sp.Rational(x) for x in (alo, ahi)]
    bc = [sp.Rational(x) for x in (blo, bhi)]
    exact = max(expr.subs({a: x, b: y}) for x in cands for y in bc)
    # independent brute force on a fine rational grid (includes endpoints)
    N = 200
    best = None
    for i in range(N + 1):
        av = F(alo) + (F(ahi) - F(alo)) * i / N
        for j in range(N + 1):
            bv = F(blo) + (F(bhi) - F(blo)) * j / N
            v = f(av, bv)
            if best is None or v > best:
                best = v
    assert sp.Rational(best.numerator, best.denominator) == exact
    return exact

orig = solve(-6, -2, 3, 5)
print("original:", orig)
assert orig == sp.Rational(-35, 9)
var = solve(-7, -3, 4, 6)
print("variant:", var, float(var))
