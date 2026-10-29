"""apex2025-03 variant check.
Method: O2, O3 lie on the perpendicular bisectors of angles ADB, ADC at D (right angle at D).
With phi = (angle ADB)/2, s = sin^2 phi: DO2 = r2/sin phi, DO3 = r3/cos phi, so
r2^2/s + r3^2/(1-s) = d^2, and (Sawayama-Thebault) r = r2 cos^2 phi + r3 sin^2 phi.
Sum r over both roots s. Formula checked numerically on random acute triangles,
and each root is realised by an explicit acute triangle (numeric search)."""
import math, random
import sympy as sp
import numpy as np
from scipy.optimize import minimize

def exact_sum(r2, r3, d):
    s = sp.symbols('s')
    roots = sp.solve(sp.Eq(r2**2*(1-s) + r3**2*s, d**2*s*(1-s)), s)
    assert len(roots) == 2 and all(r.is_real and 0 < r < 1 for r in roots)
    return sp.nsimplify(sp.simplify(sum(r2*(1-x) + r3*x for x in roots))), roots

def thebault(A, B, C, t):
    """triangle on circumcircle (center 0, R=1), D = B + t(C-B); returns r2, r3, theta=angle ADB, inradius"""
    D = B + t*(C-B)
    def circ(P):  # circle tangent to rays D->P and D->A, internally tangent to unit circle
        u1 = (P-D)/np.linalg.norm(P-D); u2 = (A-D)/np.linalg.norm(A-D)
        ang = math.acos(np.clip(u1@u2, -1, 1)); w = (u1+u2)/np.linalg.norm(u1+u2)
        sn = math.sin(ang/2)
        # |D + x w| = 1 - x sn  -> quadratic in x
        a = 1 - sn*sn; b = 2*(D@w) + 2*sn; c = D@D - 1
        x = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        return x*sn, D + x*w, ang
    r2, O2, th = circ(B); r3, O3, _ = circ(C)
    a, b, c = np.linalg.norm(B-C), np.linalg.norm(C-A), np.linalg.norm(A-B)
    sarea = abs(np.cross(B-A, C-A))/2; r = 2*sarea/(a+b+c)
    return r2, r3, th, r, np.linalg.norm(O2-O3)

def pt(a): return np.array([math.cos(a), math.sin(a)])

def acute(angs):
    P = [pt(x) for x in angs]
    for i in range(3):
        u = P[(i+1)%3]-P[i]; v = P[(i+2)%3]-P[i]
        if u@v <= 0: return False
    return True

# 1) numeric check of the formula on random acute triangles
random.seed(1); checked = 0
while checked < 200:
    angs = [random.uniform(0, 2*math.pi) for _ in range(3)]
    if not acute(angs): continue
    A, B, C = [pt(x) for x in angs]
    r2, r3, th, r, dist = thebault(A, B, C, random.uniform(0.05, 0.95))
    phi = th/2
    assert abs(r - (r2*math.cos(phi)**2 + r3*math.sin(phi)**2)) < 1e-9
    assert abs(dist**2 - (r2**2/math.sin(phi)**2 + r3**2/math.cos(phi)**2)) < 1e-9
    checked += 1
print("formula verified numerically on", checked, "random acute triangles")

# 2) realisability: for each root s, find an acute triangle with angle ADB = 2 asin(sqrt s), r3/r2 = target
def realise(s_val, ratio):
    th_t = 2*math.asin(math.sqrt(s_val))
    def loss(p):
        a1, a2, a3, t = p
        if not (0.01 < t < 0.99): return 1e3
        A, B, C = pt(a1), pt(a2), pt(a3)
        r2, r3, th, r, _ = thebault(A, B, C, t)
        return (th - th_t)**2 + (r3/r2 - ratio)**2
    rng = np.random.default_rng(0)
    for _ in range(400):
        p0 = [rng.uniform(0, 2*math.pi) for _ in range(3)] + [rng.uniform(0.1, 0.9)]
        if not acute(p0[:3]): continue
        res = minimize(loss, p0, method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-16,'maxiter':4000})
        if res.fun < 1e-14 and acute(res.x[:3]) and 0.01 < res.x[3] < 0.99:
            return res.x
    return None

def full(r2, r3, d, label):
    total, roots = exact_sum(r2, r3, d)
    for x in roots:
        p = realise(float(x), r3/r2)
        assert p is not None, "root not realisable by an acute triangle"
        A, B, C = pt(p[0]), pt(p[1]), pt(p[2])
        R2, R3, th, r, dist = thebault(A, B, C, p[3])
        k = r2/R2  # scale
        print(f"  {label}: root s={float(x):.6f} realised acute: r2={R2*k:.6f} r3={R3*k:.6f} dist={dist*k:.6f} inradius={r*k:.6f}")
    print(f"{label}: radii {r2},{r3}, distance {d} -> sum of inradii = {total} = {float(total):.10f}")
    return total

orig = full(5, 7, 13, "ORIGINAL")
assert orig == sp.Rational(1980, 169), orig
print("original check OK (1980/169)")
var = full(4, 6, 11, "VARIANT")
print("VARIANT ANSWER:", var)
