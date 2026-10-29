"""aime25-09 variant: parabola y = x^2 - K rotated 60 deg CCW about origin;
unique fourth-quadrant intersection has y = (a - sqrt b)/c. Find a+b+c."""
import sympy as sp
from math import gcd
import numpy as np

def solve(K):
    x, y = sp.symbols('x y')
    c, s = sp.Rational(1, 2), sp.sqrt(3) / 2
    # (x,y) on image  <=>  R^{-1}(x,y) on original parabola
    u, v = c * x + s * y, -s * x + c * y
    sols = sp.solve([y - (x**2 - K), v - (u**2 - K)], [x, y], dict=True)
    q4 = [so for so in sols
          if abs(sp.im(sp.N(so[x]))) < 1e-12 and sp.N(so[x]) > 0 and sp.N(so[y]) < 0]
    assert len(q4) == 1, q4
    Y = sp.radsimp(sp.nsimplify(q4[0][y]))
    # match Y = (a - sqrt(b))/cc with positive ints, gcd(a,cc)=1, b squarefree-free form
    for cc in range(1, 50):
        t = sp.expand(Y * cc)
        rat = sum(term for term in sp.Add.make_args(t) if term.is_Rational)
        rad = sp.expand(rat - t)  # = sqrt(b)
        b = sp.expand(rad**2)
        if rat.is_Integer and rat > 0 and b.is_Integer and b > 0 and rad > 0 \
                and gcd(int(rat), cc) == 1:
            a = int(rat)
            # independent numeric check: rotate original points, find crossing numerically
            th = np.pi / 3
            ts = np.linspace(-10, 10, 2_000_001)
            px, py = ts, ts**2 - K
            ix, iy = np.cos(th) * px - np.sin(th) * py, np.sin(th) * px + np.cos(th) * py
            g = iy - (ix**2 - K)  # image point lies on original when g=0
            idx = np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]
            pts = [(ix[i], iy[i]) for i in idx if ix[i] > 0 and iy[i] < 0]
            assert len(pts) == 1 and abs(pts[0][1] - float(Y)) < 1e-4, (pts, float(Y))
            return Y, a, int(b), cc, a + int(b) + cc
    raise ValueError(Y)

orig = solve(4)
print("ORIGINAL (K=4):", orig)
assert orig[-1] == 62
var = solve(5)
print("VARIANT  (K=5):", var)
print("ANSWER", var[-1])
