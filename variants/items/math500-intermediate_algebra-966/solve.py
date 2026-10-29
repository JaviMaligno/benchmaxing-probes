# Minimize x^4 + a*y^2 + b*z^4 subject to xyz = c (x,y,z>0).
from fractions import Fraction
import sympy as sp
from scipy.optimize import minimize
import numpy as np

def exact_min(a, b, c):
    # Lagrange / substitution y = c/(x z), solve gradient = 0 exactly
    x, z = sp.symbols('x z', positive=True)
    f = x**4 + a*(c/(x*z))**2 + b*z**4
    sols = sp.solve([sp.diff(f, x), sp.diff(f, z)], [x, z], dict=True)
    vals = [sp.nsimplify(sp.simplify(f.subs(s))) for s in sols]
    return min(vals), sols

def numeric_min(a, b, c):
    def f(v):
        x, z = np.exp(v)
        y = c/(x*z)
        return x**4 + a*y**2 + b*z**4
    best = min((minimize(f, np.random.randn(2), method='Nelder-Mead',
                         options={'xatol':1e-12,'fatol':1e-12,'maxiter':20000}) for _ in range(20)),
               key=lambda r: r.fun)
    return best.fun

np.random.seed(0)
# Original: a=4, b=4, c=2 -> 16
v, s = exact_min(4, 4, 2); n = numeric_min(4, 4, 2)
print("original exact:", v, s, "numeric:", n)
assert v == 16
# Variant: a=6, b=9, c=3
v, s = exact_min(6, 9, 3); n = numeric_min(6, 9, 3)
print("variant exact:", v, s, "numeric:", n)
