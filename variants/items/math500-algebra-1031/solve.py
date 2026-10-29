from fractions import Fraction
import sympy as sp

x = sp.symbols('x', real=True)

def smallest_in_domain(a, b):
    # domain: (x-a)^2 - (x-b)^2 >= 0
    expr = (x - a)**2 - (x - b)**2
    sol = sp.solve_univariate_inequality(expr >= 0, x, relational=False)
    lo = sol.inf
    # independent exact check on a rational grid with step 1/20
    grid = [Fraction(k, 20) for k in range(-400, 601)]
    ok = [t for t in grid if (t - a)**2 - (t - b)**2 >= 0]
    assert Fraction(str(lo)) == min(ok), (lo, min(ok))
    assert sol.sup == sp.oo
    return sp.nsimplify(lo)

orig = smallest_in_domain(3, 8)
print("original:", orig)
assert orig == sp.Rational(11, 2)
var = smallest_in_domain(4, 11)
print("variant:", var, float(var))
