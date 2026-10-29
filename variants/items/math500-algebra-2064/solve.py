from sympy import symbols, diff, solve, Rational, simplify
from fractions import Fraction
x = symbols('x', real=True)

def max_val(k, a, b):
    # maximum of k(x+a)(b-x), k>0 (downward parabola)
    f = k*(x+a)*(b-x)
    crit = solve(diff(f, x), x)
    assert len(crit) == 1
    v = simplify(f.subs(x, crit[0]))
    # independent numeric check: scan a fine rational grid
    best = max(Fraction(k)*(Fraction(t, 100)+a)*(b-Fraction(t, 100)) for t in range(-3000, 3001))
    assert best <= v
    return v

orig = max_val(4, 7, 2)
print("original:", orig)
assert orig == 81
var = max_val(3, 5, 7)
print("variant:", var)
