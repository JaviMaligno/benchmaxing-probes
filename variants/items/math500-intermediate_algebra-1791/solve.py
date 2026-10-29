from sympy import symbols, Rational, diff, solve, simplify
from fractions import Fraction
x, y = symbols('x y')

def best_x(a, c, b):
    z = (a*x - y)**2 - c*y**2 - b*y
    assert diff(z, y, 2) < 0  # concave in y: Brahmagupta's max exists
    ystar = solve(diff(z, y), y)[0]
    g = simplify(z.subs(y, ystar))
    assert diff(g, x, 2) > 0  # convex in x: Archimedes' min exists
    return solve(diff(g, x), x)[0]

def brute(a, c, b):
    # independent numeric check: grid over x in rationals, max over y via exact vertex of quadratic
    best = None
    for k in range(-2000, 2001):
        X = Fraction(k, 1000)
        # z = -(c-1) y^2 - (2aX + b) y + a^2 X^2
        A = -(c - 1); B = -(2*a*X + b); C = a*a*X*X
        zmax = C - B*B/(4*A)
        if best is None or zmax < best[0]:
            best = (zmax, X)
    return best[1]

orig = best_x(2, 2, 3)
print("original:", orig, "brute:", brute(2, 2, 3))
assert orig == Rational(-3, 8)
var = best_x(3, 3, 5)
print("variant:", var, "brute:", brute(3, 3, 5))
