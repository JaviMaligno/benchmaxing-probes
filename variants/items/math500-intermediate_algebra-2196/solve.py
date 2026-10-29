# Max of (x - y)/(x^4 + y^4 + k) over reals.
import sympy as sp
import numpy as np

x, y = sp.symbols('x y', real=True)

def exact_max(k):
    # Critical points: numerators of the partial derivatives vanish.
    D = x**4 + y**4 + k
    e1 = sp.expand(D - 4*x**3*(x - y))      # d/dx
    e2 = sp.expand(-D - 4*y**3*(x - y))     # d/dy
    # e1 + e2 = -4(x-y)(x^3+y^3); x=y gives f=0, so real critical points with f != 0 have y = -x.
    assert sp.factor(e1 + e2) == sp.factor(-4*(x - y)*(x**3 + y**3))
    xs = [r for r in sp.solve(e1.subs(y, -x), x) if r.is_real]
    f = (x - y) / D
    vals = [sp.nsimplify(sp.simplify(f.subs({x: r, y: -r}))) for r in xs]
    return max(vals + [sp.Integer(0)])

def numeric_max(k):
    # Independent check: dense grid then local refinement grids.
    cx, cy, w = 0.0, 0.0, 6.0
    best = -1.0
    for _ in range(12):
        g = np.linspace(-w, w, 801)
        X, Y = np.meshgrid(cx + g, cy + g)
        F = (X - Y) / (X**4 + Y**4 + k)
        i = np.unravel_index(np.argmax(F), F.shape)
        best, cx, cy = F[i], X[i], Y[i]
        w /= 8
    return best

for label, k, expected in [("original", 6, sp.Rational(1, 4)), ("variant", 96, None)]:
    e = exact_max(k); n = numeric_max(k)
    print(label, "k =", k, "exact max =", e, "numeric =", n)
    assert abs(float(e) - n) < 1e-8
    if expected is not None:
        assert e == expected, (e, expected)
        print("original answer reproduced:", e == expected)
