"""aime25-14 variant check.
Pentagon ABCDE convex, angle B = angle E = 60 deg. Build it numerically (coordinates),
minimise f(X)=sum of distances numerically (multi-start Nelder-Mead), and compare with
the closed form m + n*sqrt(p) found by exact rational arithmetic
(BE + Fermat sum of triangle ACD). Search (m,n,p) independently from the float value too."""
import math
from fractions import Fraction as Fr
from math import isqrt
import numpy as np
from scipy.optimize import brentq, minimize

def build(AB, BC, CD, DE, EA):
    A = np.array([0.0, 0.0]); B = np.array([AB, 0.0])
    C = B + BC*np.array([math.cos(math.radians(120)), math.sin(math.radians(120))])
    def pts(t):
        E = EA*np.array([math.cos(t), math.sin(t)])
        da = math.atan2(-E[1], -E[0]); dd = da + math.radians(60)
        D = E + DE*np.array([math.cos(dd), math.sin(dd)])
        return D, E
    g = lambda t: np.linalg.norm(C - pts(t)[0]) - CD
    ts = np.linspace(1e-3, math.pi - 1e-3, 4001); out = []
    for i in range(len(ts) - 1):
        if g(ts[i]) * g(ts[i+1]) < 0:
            t = brentq(g, ts[i], ts[i+1], xtol=1e-15)
            D, E = pts(t); out.append(np.array([A, B, C, D, E]))
    return out

def convex(P):
    s = []
    for i in range(5):
        a, b, c = P[i], P[(i+1) % 5], P[(i+2) % 5]
        s.append((b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0]))
    return all(x > 0 for x in s)

def fmin(P):
    f = lambda X: float(np.linalg.norm(P - X, axis=1).sum())
    best = min(f(p) for p in P)
    starts = [P.mean(0)] + list(P) + [np.random.default_rng(i).uniform(P.min(0), P.max(0)) for i in range(20)]
    for s in starts:
        r = minimize(f, s, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-13, 'maxiter': 40000})
        best = min(best, r.fun)
    return best

def rsq(q):
    n, d = q.numerator, q.denominator
    rn, rd = isqrt(n), isqrt(d)
    return Fr(rn, rd) if rn*rn == n and rd*rd == d else None

def closed_form(a, b, c):
    # AB=2a, BC=a, DE=b, EA=2b, CD=c -> AC=a*sqrt3, AD=b*sqrt3 (30-60-90 triangles)
    cs = Fr(3*a*a + 3*b*b - c*c, 6*a*b)        # cos CAD
    s = rsq((1 - cs*cs) / 3)                   # sin CAD = s*sqrt3
    cBAE = cs/2 - Fr(3, 2)*s                   # cos(60deg + CAD)
    BE = rsq(4*a*a + 4*b*b - 8*a*b*cBAE)
    F2 = Fr(3*a*a + 3*b*b + c*c, 2) + 9*a*b*s  # Fermat-sum^2 of ACD
    n = rsq(F2 / 3)
    return BE, n, 3

def ident(v):
    out = []
    for p in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]:
        for n in range(1, 300):
            m = v - n*math.sqrt(p)
            if m > 0.5 and abs(m - round(m)) < 1e-6:
                out.append((round(m), n, p))
    return out

def run(label, AB, BC, CD, DE, EA):
    Ps = [P for P in build(AB, BC, CD, DE, EA) if convex(P)]
    assert len(Ps) == 1, f"{label}: expected unique convex pentagon, got {len(Ps)}"
    v = fmin(Ps[0])
    m, n, p = closed_form(BC, DE, CD)
    exact = float(m) + float(n)*math.sqrt(p)
    print(f"{label}: numeric min f = {v:.10f}; closed form {m} + {n}*sqrt({p}) = {exact:.10f}; "
          f"float identification {ident(v)}; m+n+p = {m+n+p}")
    assert abs(v - exact) < 1e-6
    return int(m + n + p)

orig = run("ORIGINAL", 14, 7, 24, 13, 26)
assert orig == 60, orig
var = run("VARIANT", 38, 19, 48, 19, 38)
print("ORIGINAL answer:", orig)
print("VARIANT answer:", var)
