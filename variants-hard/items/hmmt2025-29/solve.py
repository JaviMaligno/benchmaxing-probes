"""hmmt2025-29 variant: rectangle ABCD, BC=h, X inside with angle AXB=90,
triangles AXD, BXC acute with circumradii R1, R2. Compute AB.
Original: h=24, R1=13, R2=15 -> 14+4*sqrt(37). Variant: h=30, R1=17, R2=25."""
import itertools, math
import sympy as sp

a, x, y = sp.symbols('a x y', real=True)

def dot(p, q, r):
    return (q[0]-p[0])*(r[0]-p[0]) + (q[1]-p[1])*(r[1]-p[1])

def acute(p, q, r):
    return min(dot(p, q, r), dot(q, p, r), dot(r, p, q)) > 1e-9

def circumradius(p, q, r):
    A = math.dist(q, r); B = math.dist(p, r); C = math.dist(p, q)
    area = abs((q[0]-p[0])*(r[1]-p[1]) - (r[0]-p[0])*(q[1]-p[1])) / 2
    return A*B*C/(4*area)

def valid(h, R1, R2, fa, fx, fy):
    if not (fa > 0 and 0 < fx < fa and 0 < fy < h):
        return False
    A, B, C, D, X = (0, 0), (fa, 0), (fa, h), (0, h), (fx, fy)
    return (acute(A, X, D) and acute(B, X, C)
            and abs(circumradius(A, X, D) - R1) < 1e-7
            and abs(circumradius(B, X, C) - R2) < 1e-7
            and abs(dot(X, A, B)) < 1e-7)

def exact(h, R1, R2):
    # Acute triangle => circumcenter on X's side of AD / BC: O1=(d1,h/2), O2=(a-d2,h/2)
    m = sp.Rational(h, 2); d1 = sp.sqrt(R1**2 - m**2); d2 = sp.sqrt(R2**2 - m**2)
    eqs = [x**2 + y**2 - a*x,
           (x-d1)**2 + (y-m)**2 - R1**2,
           (x-a+d2)**2 + (y-m)**2 - R2**2]
    res = set()
    for s in sp.solve(eqs, [a, x, y], dict=True):
        A_, X_, Y_ = (sp.nsimplify(s[v]) for v in (a, x, y))
        if not all(v.is_real for v in (A_, X_, Y_)):
            continue
        if valid(h, R1, R2, float(A_), float(X_), float(Y_)):
            res.add(sp.simplify(A_))
    return res

def numeric(h, R1, R2):
    # Independent check without the circumcenter-location assumption: parametrise X on the
    # circle with diameter AB by t = angle XAB, X = (a cos^2 t, a cos t sin t); circumradii
    # from R = abc/(4K); solve with scipy from a grid of starts, keep valid configurations.
    from scipy.optimize import fsolve
    def F(v):
        A_, t = v
        X = (A_*math.cos(t)**2, A_*math.cos(t)*math.sin(t))
        try:
            return [circumradius((0, 0), X, (0, h)) - R1, circumradius((A_, 0), X, (A_, h)) - R2]
        except ZeroDivisionError:
            return [1e6, 1e6]
    out = set()
    for A0 in [h*k/8 for k in range(1, 41)]:
        for t0 in [k*math.pi/40 for k in range(1, 20)]:
            sol, info, ier, _ = fsolve(F, [A0, t0], full_output=True, xtol=1e-14)
            if ier != 1: continue
            A_, t = sol
            fx, fy = A_*math.cos(t)**2, A_*math.cos(t)*math.sin(t)
            if valid(h, R1, R2, A_, fx, fy):
                out.add(round(A_, 7))
    return out

for label, (h, R1, R2), expected in [("original", (24, 13, 15), 14 + 4*sp.sqrt(37)),
                                     ("variant", (30, 17, 25), None)]:
    ex = exact(h, R1, R2); nu = numeric(h, R1, R2)
    print(label, (h, R1, R2), "exact:", ex, "numeric:", nu)
    assert len(ex) == 1 and len(nu) == 1
    val = next(iter(ex))
    assert abs(float(val) - next(iter(nu))) < 1e-6
    if expected is not None:
        assert sp.simplify(val - expected) == 0
        print("original reproduced:", val)
    else:
        print("VARIANT ANSWER:", val, "=", float(val))
