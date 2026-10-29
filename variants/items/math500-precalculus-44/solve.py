import sympy as sp
from fractions import Fraction

def expr(a, b, c, d):
    r = lambda t: sp.rad(t)
    num = sp.cos(r(a))*sp.cos(r(b)) + sp.cos(r(c))*sp.cos(r(d)) - sp.sin(r(a))*sp.sin(r(b)) - sp.sin(r(c))*sp.sin(r(d))
    den = sp.sin(r(a))*sp.cos(r(b)) - sp.sin(r(c))*sp.cos(r(d)) + sp.cos(r(a))*sp.sin(r(b)) - sp.cos(r(c))*sp.sin(r(d))
    return num / den

def least_angle(a, b, c, d):
    val = sp.N(expr(a, b, c, d), 50)
    # brute force: scan integer degrees 1..179, then confirm exactly via closed form
    cands = [t for t in range(1, 180) if t != 90 and abs(sp.N(sp.tan(sp.rad(t)), 50) - val) < 1e-30]
    t = cands[0]
    # exact check: tan(theta) equals the expression symbolically
    assert sp.simplify(sp.nsimplify(sp.N(sp.tan(sp.rad(t)) - expr(a, b, c, d), 60), tolerance=1e-40)) == 0
    return t, val

t0, v0 = least_angle(5, 20, 35, 50)
print("original:", t0, "deg; tan value", sp.N(v0, 15))
assert t0 == 120
t1, v1 = least_angle(10, 5, 55, 80)
print("variant:", t1, "deg; tan value", sp.N(v1, 15), "(-1/sqrt3 =", sp.N(-1/sp.sqrt(3), 15), ")")
