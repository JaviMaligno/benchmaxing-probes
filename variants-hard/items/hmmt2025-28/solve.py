import sympy as sp

def solve(AB, DE, R):
    """Isosceles trapezoid ABCD with CD > AB, circle center O=(0,0) radius R.
    A=(-a,y1), B=(a,y1), D=(-d,y0), C=(d,y0), E=(-d-k,y0) (D between E and C), M = mid AE.
    Return set of valid MD values (exact)."""
    a = sp.Rational(AB, 2); k = sp.Integer(DE); R = sp.Integer(R)
    d, y0, y1 = sp.symbols('d y0 y1', real=True)
    eqs = [a**2 + y1**2 - R**2, d**2 + y0**2 - R**2,
           ((-a - d - k)/2)**2 + ((y1 + y0)/2)**2 - R**2]
    sols = sp.solve(eqs, [d, y0, y1], dict=True)
    res = set()
    for s in sols:
        dv, y0v, y1v = [sp.nsimplify(sp.simplify(s[v])) for v in (d, y0, y1)]
        if not all(x.is_real for x in (dv, y0v, y1v)):
            continue
        if not (dv > a) or y0v == y1v:   # CD > AB, nondegenerate
            continue
        Mx, My = (-a - dv - k)/2, (y1v + y0v)/2
        MD = sp.sqrt((Mx + dv)**2 + (My - y0v)**2)
        res.add(sp.radsimp(sp.simplify(MD)))
    return res

def numeric_check(AB, DE, R):
    # independent brute force: scan y1 sign, y0 sign, solve for d via 1-D root
    import math
    a, k = AB/2, DE
    out = set()
    for s1 in (1, -1):
        y1 = s1*math.sqrt(R*R - a*a)
        for s0 in (1, -1):
            f = lambda d: ((-a-d-k)/2)**2 + ((y1 + s0*math.sqrt(max(R*R-d*d,0)))/2)**2 - R*R
            N = 200000
            prev = None
            for i in range(N+1):
                dd = a + (R - a)*i/N
                v = f(dd)
                if prev is not None and prev[1]*v <= 0:
                    lo, hi = prev[0], dd
                    for _ in range(80):
                        mid = (lo+hi)/2
                        if f(lo)*f(mid) <= 0: hi = mid
                        else: lo = mid
                    dsol = (lo+hi)/2; y0 = s0*math.sqrt(R*R-dsol*dsol)
                    if dsol > a + 1e-9 and abs(y0 - y1) > 1e-9:
                        Mx, My = (-a-dsol-k)/2, (y1+y0)/2
                        out.add(round(math.hypot(Mx+dsol, My-y0), 9))
                prev = (dd, v)
    return out

orig = solve(4, 2, 5)
print("original:", orig, "numeric:", numeric_check(4, 2, 5))
assert orig == {sp.sqrt(6)}
var = solve(6, 3, 7)
print("variant:", var, [sp.N(v) for v in var], "numeric:", numeric_check(6, 3, 7))
