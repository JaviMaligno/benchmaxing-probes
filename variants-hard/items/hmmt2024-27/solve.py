# Numeric construction: find A=(x,h) over BC on x-axis with altitude feet such that AQ matches,
# then compute orthic perimeter directly; compare with exact closed form 2*h*sinA.
import math, sympy as sp
from scipy.optimize import brentq

def foot(P, U, V):
    ux, uy = V[0]-U[0], V[1]-U[1]
    t = ((P[0]-U[0])*ux + (P[1]-U[1])*uy)/(ux*ux+uy*uy)
    return (U[0]+t*ux, U[1]+t*uy)
d = lambda P, R: math.hypot(P[0]-R[0], P[1]-R[1])

def config(x, a, h):
    A, B, C = (x, h), (0.0, 0.0), (a, 0.0)
    D, E, F = foot(A, B, C), foot(B, C, A), foot(C, A, B)
    Q = foot(A, E, F)
    return A, B, C, D, E, F, Q

def acute(A, B, C):
    def ang_ok(P, R, S):
        return (R[0]-P[0])*(S[0]-P[0]) + (R[1]-P[1])*(S[1]-P[1]) > 0
    return ang_ok(A,B,C) and ang_ok(B,A,C) and ang_ok(C,A,B)

def solve(AQ, a, h):
    # scan x in (0, a/2] (symmetry), find roots of AQ(x)-AQ among acute triangles
    f = lambda x: d(config(x,a,h)[0], config(x,a,h)[6]) - AQ
    xs = [a/2*i/20000 for i in range(1, 20001)]
    res = []
    for x0, x1 in zip(xs, xs[1:]):
        if f(x0)*f(x1) < 0:
            r = brentq(f, x0, x1, xtol=1e-14)
            A,B,C,D,E,F,Q = config(r,a,h)
            if acute(A,B,C):
                res.append(d(D,E)+d(E,F)+d(F,D))
    if abs(f(a/2)) < 1e-9:
        A,B,C,D,E,F,Q = config(a/2,a,h)
        if acute(A,B,C): res.append(d(D,E)+d(E,F)+d(F,D))
    return res

def exact(AQ, h):
    c = sp.Rational(AQ, h)          # AQ = AD cos A
    return sp.nsimplify(sp.simplify(2*h*sp.sqrt(1-c**2)))  # perimeter = 2K/R = 2 h sin A

for name, (AQ, a, h), expect in [("original", (20,15,24), 8*sp.sqrt(11)),
                                 ("variant",  (15,16,20), None)]:
    ex = exact(AQ, h)
    nums = solve(AQ, a, h)
    print(name, "exact:", ex, float(ex), "numeric perimeters (acute solutions):", nums)
    assert nums and all(abs(n-float(ex))<1e-7 for n in nums)
    if expect is not None:
        assert sp.simplify(ex-expect)==0
        print("original reproduced:", ex)
