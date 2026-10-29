# Largest regular tetrahedron from a parallelogram net (strip of 4 equilateral
# triangles: parallelogram with sides 2a, a and angle 60 deg) cut from a square of side s.
# A convex polygon fits in an axis-aligned square iff, for some rotation, its bounding
# box fits. So a_max = s / min_theta max(width(theta), height(theta)) for the unit shape.
import math
from scipy.optimize import minimize_scalar
import sympy as sp

V = [(0,0),(2,0),(2+0.5, math.sqrt(3)/2),(0.5, math.sqrt(3)/2)]  # unit a=1

def box(t):
    c, s_ = math.cos(t), math.sin(t)
    xs = [x*c - y*s_ for x,y in V]; ys = [x*s_ + y*c for x,y in V]
    return max(max(xs)-min(xs), max(ys)-min(ys))

N = 200000
best_t = min((i*math.pi/N for i in range(N)), key=box)
res = minimize_scalar(box, bounds=(best_t-1e-4, best_t+1e-4), method='bounded',
                      options={'xatol':1e-14})
k = res.fun  # minimal bounding-square side for a=1
ratio = 1/k**2  # a_max^2 / s^2
print("a_max^2/s^2 numeric =", ratio, " (2/7 =", 2/7, ")")

def area(s):
    from fractions import Fraction
    r = Fraction(ratio).limit_denominator(100)
    assert abs(float(r)-ratio) < 1e-7
    a2 = sp.Rational(r.numerator, r.denominator) * s**2
    return sp.sqrt(3)*a2   # 4 * (sqrt3/4) a^2

orig = area(7); print("original s=7:", orig, " matches 14*sqrt(3):", sp.simplify(orig-14*sp.sqrt(3))==0)
var = area(14); print("variant s=14:", var, "=", float(var), "; numeric check:", math.sqrt(3)*ratio*196)
