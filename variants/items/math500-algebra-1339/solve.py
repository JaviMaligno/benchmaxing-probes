from sympy import sqrt, symbols, solve, Rational, nsimplify
x = symbols('x', positive=True)
def answer(x0, y0, y1):
    k = y0*sqrt(x0)            # y*sqrt(x) = k
    sol = solve(y1*sqrt(x) - k, x)
    assert len(sol) == 1
    return sol[0]
def brute(x0, y0, y1):
    # independent check: x1 = x0*(y0/y1)^2, exact rationals
    return Rational(x0)*Rational(y0, y1)**2
orig = answer(24, 15, 3); assert orig == 600 and brute(24, 15, 3) == 600
print("original:", orig)
var = answer(18, 20, 4); assert var == brute(18, 20, 4)
print("variant:", var)
