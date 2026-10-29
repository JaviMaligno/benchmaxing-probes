import sympy as sp
from scipy.optimize import minimize
import numpy as np

def solve(a, b, p, q):
    # f = sqrt(x^2+a^2)+sqrt(y^2+b^2)+sqrt((x-p)^2+(y-q)^2) on [0,p]x[0,q]
    f = lambda v: np.sqrt(v[0]**2+a*a)+np.sqrt(v[1]**2+b*b)+np.hypot(v[0]-p, v[1]-q)
    # numeric: grid + local refinement
    xs = np.linspace(0, p, 401); ys = np.linspace(0, q, 401)
    X, Y = np.meshgrid(xs, ys)
    F = np.sqrt(X**2+a*a)+np.sqrt(Y**2+b*b)+np.hypot(X-p, Y-q)
    i = np.unravel_index(F.argmin(), F.shape)
    r = minimize(f, [X[i], Y[i]], bounds=[(0, p), (0, q)])
    # exact: QM-AM bound sqrt2*(a+b+p+q)/2, attained at x=a, y=b iff p-a == q-b
    assert p - a == q - b
    exact = sp.sqrt(2)*sp.Rational(a+b+p+q, 2)
    assert abs(float(exact) - r.fun) < 1e-6, (exact, r.fun)
    return sp.nsimplify(exact), r.fun

o = solve(20, 30, 40, 50)
print("original:", o)
assert o[0] == 70*sp.sqrt(2)
# variant: x^2+225, y^2+400, x^2+y^2-70x-80y+2825 on [0,35]x[0,40]
x, y = sp.symbols('x y')
assert sp.expand((x-35)**2+(y-40)**2) == x**2+y**2-70*x-80*y+2825
v = solve(15, 20, 35, 40)
print("variant:", v)
