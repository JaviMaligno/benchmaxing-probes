# Square PQRS side s, P=(0,0), Q=(s,0), R=(s,s), S=(0,s). Line through midpoint of PQ
# with direction angle t (0<t<pi), must hit segment QR. Distances from P and R given.
import sympy as sp
from math import cos, sin, pi, isclose
from scipy.optimize import brentq

def solve(dA, dC):
    s, t = sp.symbols('s t', positive=True)
    M = sp.Matrix([s/2, 0]); d = sp.Matrix([sp.cos(t), sp.sin(t)])
    def dist(X):
        v = X - M
        return v[0]*d[1] - v[1]*d[0]   # signed cross product
    A = sp.Matrix([0, 0]); C = sp.Matrix([s, s])
    sols = []
    for sa in (1, -1):
        for sc in (1, -1):
            for sol in sp.solve([dist(A) - sa*dA, dist(C) - sc*dC], [s, t], dict=True):
                sv = sp.nsimplify(sp.simplify(sol[s])); tv = sol[t]
                tn = float(tv) % pi
                if float(sv) <= 0: continue
                # intersection with line x=s: y = (s/2) tan t, need 0<=y<=s
                y = float(sv)/2*sp.tan(tn)
                if 0 <= y <= float(sv) and 0 < tn < pi/2 + 1e-12:
                    sols.append(sp.nsimplify(sp.simplify(sv**2)))
    return set(sols)

def numeric(dA, dC):
    # independent numeric: scan angle, for each angle s from dA, check dC
    res = set()
    import numpy as np
    f = lambda t: (2*dA/np.sin(t))*np.cos(t) - (2*dA/np.sin(t))/2*np.sin(t) - dC
    ts = np.linspace(1e-4, np.arctan(2)-1e-9, 20000)
    v = f(ts)
    for i in range(len(ts)-1):
        if v[i]*v[i+1] < 0:
            r = brentq(f, ts[i], ts[i+1]); s = 2*dA/np.sin(r); res.add(round(s*s, 6))
    return res

print("original (4,7):", solve(4, 7), numeric(4, 7))
assert solve(4, 7) == {185}
print("variant (5,8):", solve(5, 8), numeric(5, 8))
