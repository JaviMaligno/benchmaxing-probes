# Minimise (a+b+c)[(P(a+b))^2 + (a+b+K c)^2] / (abc) over positive reals.
# Original: P=1, K=4 -> 100.  Variant: P=2, K=1 -> 64.
import sympy as sp
import numpy as np
from scipy.optimize import minimize

def exact_min(P, K):
    # Homogeneous of degree 0: set c=1. The numerator depends only on s=a+b and
    # the denominator is ab <= s^2/4, so the minimum has a=b=x (s=2x).
    x = sp.symbols('x', positive=True)
    f = (2*x + 1) * ((2*P*x)**2 + (2*x + K)**2) / x**2
    num = sp.Poly(sp.numer(sp.together(sp.diff(f, x))), x)
    crit = [r for r in sp.real_roots(num) if r > 0]
    vals = [sp.nsimplify(sp.simplify(f.subs(x, r))) for r in crit]
    return min(vals), crit

def numeric_min(P, K):
    g = lambda v: (lambda a, b, c: (a+b+c)*((P*(a+b))**2 + (a+b+K*c)**2)/(a*b*c))(*np.exp(v))
    rng = np.random.default_rng(0)
    best = min((minimize(g, rng.normal(size=3), method='Nelder-Mead',
                         options={'xatol': 1e-12, 'fatol': 1e-12, 'maxiter': 20000})
                for _ in range(30)), key=lambda r: r.fun)
    return best.fun, np.exp(best.x) / np.exp(best.x)[2]

for name, P, K, expected in [("original", 1, 4, 100), ("variant", 2, 1, None)]:
    ex, sols = exact_min(P, K)
    nm, pt = numeric_min(P, K)
    print(f"{name}: exact min = {ex}, critical points (c=1) = {sols}, numeric min = {nm:.9f} at (a,b,c)~{pt}")
    if expected is not None:
        assert ex == expected and abs(nm - expected) < 1e-6
        print(f"{name} check OK (matches {expected})")
    else:
        assert abs(nm - float(ex)) < 1e-6
        print(f"variant answer = {ex}")
