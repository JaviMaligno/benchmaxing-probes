"""aime25-29 variant check.
Independent numeric construction: A at origin, B on x-axis, C on y-axis.
AK=AL=KL=s => K at angle t from AB, L at angle t+60.  BK=s => AB=2s cos t;
CL=s => AC=2s cos(30deg - t).  Solve BC^2 = AB^2+AC^2 for t by bisection on
[0,15deg] (f symmetric about 15deg; the other root mirrors B<->C, same area),
build coordinates, verify all constraints and interiority, shoelace area / sqrt3.
Also cross-check with exact sympy closed form."""
import math
import sympy as sp

def solve(s, BC2):
    f = lambda t: (2*s*math.cos(t))**2 + (2*s*math.cos(math.pi/6 - t))**2 - BC2
    lo, hi = 0.0, math.pi/12
    assert f(lo) * f(hi) < 0, "no root in [0,15deg]"
    for _ in range(200):
        mid = (lo+hi)/2
        if f(lo)*f(mid) <= 0: hi = mid
        else: lo = mid
    t = (lo+hi)/2
    A = (0.0, 0.0); B = (2*s*math.cos(t), 0.0); C = (0.0, 2*s*math.cos(math.pi/6 - t))
    K = (s*math.cos(t), s*math.sin(t)); L = (s*math.cos(t+math.pi/3), s*math.sin(t+math.pi/3))
    d = lambda P, Q: math.hypot(P[0]-Q[0], P[1]-Q[1])
    for v in (d(A,K), d(A,L), d(B,K), d(C,L), d(K,L)):
        assert abs(v - s) < 1e-9
    assert abs(d(B,C)**2 - BC2) < 1e-6
    def inside(P):
        return P[0] > 0 and P[1] > 0 and P[0]/B[0] + P[1]/C[1] < 1
    assert inside(K) and inside(L)
    poly = [B, K, L, C]
    area = 0.5*abs(sum(poly[i][0]*poly[(i+1)%4][1] - poly[(i+1)%4][0]*poly[i][1] for i in range(4)))
    return area / math.sqrt(3)

def exact(s, BC2):
    t = sp.symbols('t', real=True)
    c = 2*s*sp.cos(t); b = 2*s*sp.cos(sp.pi/6 - t)
    # solve via cos t = x
    x = sp.symbols('x', positive=True)
    eq = sp.expand((2*s*x)**2 + (2*s*(sp.sqrt(3)/2*x + sp.Rational(1,2)*sp.sqrt(1-x**2)))**2 - BC2)
    sols = [r for r in sp.solve(eq, x) if r.is_real and sp.cos(sp.pi/12) < r <= 1]
    assert len(sols) == 1
    X = sols[0]; S = sp.sqrt(1-X**2)
    AB = 2*s*X; AC = 2*s*(sp.sqrt(3)/2*X + S/2)
    sin30mt = sp.Rational(1,2)*X - sp.sqrt(3)/2*S
    area = AB*AC/2 - sp.Rational(1,2)*AB*s*S - sp.sqrt(3)/4*s**2 - sp.Rational(1,2)*AC*s*sin30mt
    return sp.nsimplify(sp.simplify(area/sp.sqrt(3)))

orig = solve(14, 38**2); orig_exact = exact(14, 38**2)
print("original numeric n =", orig, " exact =", orig_exact)
assert round(orig) == 104 and orig_exact == 104
var = solve(26, 4816); var_exact = exact(26, 4816)
print("variant numeric n =", var, " exact =", var_exact)
assert abs(var - round(var)) < 1e-6 and var_exact == round(var)
print("VARIANT ANSWER:", var_exact)
