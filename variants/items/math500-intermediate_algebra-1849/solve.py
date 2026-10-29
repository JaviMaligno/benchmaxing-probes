# Count integer k in [lo,hi] with log(kx) = 2 log(x+c) having exactly one real solution.
# Equivalent: kx = (x+c)^2 with kx > 0 and x + c > 0. Solve quadratic exactly, filter domain.
import sympy as sp
import math

x = sp.symbols('x', real=True)

def count_solutions(k, c):
    if k == 0:
        return 0
    # x^2 + (2c-k)x + c^2 = 0, discriminant D = k(k-4c) (exact integer)
    D = k*(k - 4*c)
    if D < 0:
        return 0
    if D == 0:
        roots = {sp.Rational(k - 2*c, 2)}
    else:
        roots = {(k - 2*c + sp.sqrt(D))/2, (k - 2*c - sp.sqrt(D))/2}
    # roots are never exactly 0 or -c (plugging in gives c^2 != 0 and -kc != 0), so float sign tests are safe
    return sum(1 for r in roots if float(k*r) > 0 and float(r + c) > 0)

def numeric_check(k, c):
    # independent check: sign changes of f(x)=log(kx)-2log(x+c) on a fine grid, ignoring
    # float noise near zero, plus detection of a tangential (double) root
    import numpy as np
    if k == 0: return 0
    if k < 0:
        xs = -c + c*np.linspace(0, 1, 400001)[1:-1]
    else:
        xs = np.geomspace(1e-9, 1e7, 400001)
    f = np.log(k*xs) - 2*np.log(xs + c)
    tol = 1e-9
    sgn = np.sign(np.where(np.abs(f) < tol, 0, f))
    nz = sgn[sgn != 0]
    n = int(np.sum(nz[:-1] != nz[1:]))
    if n == 0 and np.min(np.abs(f)) < 1e-6:
        n = 1  # touches zero without crossing
    return n

def answer(lo, hi, c):
    return sum(1 for k in range(lo, hi + 1) if count_solutions(k, c) == 1)

orig = answer(-500, 500, 2)
print("original (c=2, [-500,500]):", orig, "expected 501:", orig == 501)
var = answer(-250, 400, 3)
print("variant (c=3, [-250,400]):", var)
# spot numeric checks on the variant
for k in [-250, -7, -1, 1, 11, 12, 13, 400]:
    print(" k=%d exact=%d numeric=%d" % (k, count_solutions(k, 3), numeric_check(k, 3)))
