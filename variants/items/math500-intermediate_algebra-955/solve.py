# Max |a|+|b|+|c| subject to |a x^2 + b x + c| <= M for all x in [0, L].
# Method 1 (exact, sympy): interpolation at x=0, L/2, L + triangle inequality bound,
#   attained by the scaled Chebyshev polynomial (checked exactly).
# Method 2 (independent numeric): LP over each sign pattern with constraints on a dense grid.
from fractions import Fraction as F
import itertools
import sympy as sp
import numpy as np
from scipy.optimize import linprog

def exact(L, M):
    a, b, c, p, q, r = sp.symbols('a b c p q r')
    x = sp.Symbol('x')
    f = a*x**2 + b*x + c
    sol = sp.solve([f.subs(x, 0) - p, f.subs(x, L/sp.Integer(2)) - q, f.subs(x, L) - r], [a, b, c])
    bound = sum(sum(abs(coef) for coef in sp.Poly(sol[v], p, q, r).coeffs()) for v in (a, b, c)) * M
    # extremal: M*T2(2x/L - 1) = M*(2(2x/L-1)^2 - 1)
    g = sp.expand(M*(2*(2*x/L - 1)**2 - 1))
    co = sp.Poly(g, x).all_coeffs()
    # check |g|<=M on [0,L]: g is parabola with vertex at L/2 value -M, endpoints M
    assert g.subs(x, 0) == M and g.subs(x, L) == M and g.subs(x, L/sp.Integer(2)) == -M
    attained = sum(abs(t) for t in co)
    assert sp.simplify(attained - bound) == 0
    return sp.nsimplify(bound)

def numeric(L, M, n=4001):
    xs = np.linspace(0, L, n)
    best = 0
    for s in itertools.product([1, -1], repeat=3):
        A = np.stack([xs**2, xs, np.ones_like(xs)], axis=1)
        A_ub = np.vstack([A, -A]); b_ub = np.full(2*n, M)
        res = linprog(-np.array(s, float), A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)]*3)
        best = max(best, -res.fun)
    return best

orig = exact(sp.Integer(1), sp.Integer(1))
print("original exact:", orig, " numeric LP:", round(numeric(1, 1), 6))
assert orig == 17
var = exact(sp.Integer(2), sp.Integer(1))
print("variant exact:", var, " numeric LP:", round(numeric(2, 1), 6))
