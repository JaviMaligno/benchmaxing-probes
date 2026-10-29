# Trapezoid ABCD, AD || BC, AC perp CD, AC bisects angle BAD. Given [ABCD], find [ACD].
import sympy as sp
from fractions import Fraction
import math

t, L = sp.symbols('t L', positive=True)  # t = angle CAD = half of angle BAD
A = sp.Matrix([0, 0])
C = sp.Matrix([L*sp.cos(t), L*sp.sin(t)])
D = sp.Matrix([L/sp.cos(t), 0])                 # on AD with angle ACD = 90
B = sp.Matrix([L*sp.sin(t)/sp.tan(2*t), L*sp.sin(t)])  # ray at angle 2t from A, on line through C parallel to AD

def area(*P):
    s = 0
    for i in range(len(P)):
        x1, y1 = P[i]; x2, y2 = P[(i+1) % len(P)]
        s += x1*y2 - x2*y1
    return sp.Abs(s)/2

ratio_sym = sp.simplify(sp.trigsimp((area(A, C, D)/area(A, B, C, D)).rewrite(sp.cos)))
print("symbolic ratio [ACD]/[ABCD] =", ratio_sym)

# independent numeric check across several angles (need 2t < 90 deg so B lies on the correct side)
ratios = []
for deg in [10, 20, 25, 30, 35, 40]:
    tv = math.radians(deg)
    Ax, Ay = 0.0, 0.0
    Cx, Cy = math.cos(tv), math.sin(tv)
    Dx, Dy = 1/math.cos(tv), 0.0
    Bx, By = math.sin(tv)/math.tan(2*tv), math.sin(tv)
    # sanity: AC perp CD, BA == BC
    assert abs((Cx-Ax)*(Dx-Cx) + (Cy-Ay)*(Dy-Cy)) < 1e-12
    assert abs(math.hypot(Bx, By) - math.hypot(Cx-Bx, Cy-By)) < 1e-12
    def ar(P):
        return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
    ratios.append(ar([(Ax,Ay),(Cx,Cy),(Dx,Dy)]) / ar([(Ax,Ay),(Bx,By),(Cx,Cy),(Dx,Dy)]))
print("numeric ratios:", [round(r, 12) for r in ratios])
r = Fraction(2, 3)
assert all(abs(x - float(r)) < 1e-12 for x in ratios)

orig = r * 42
print("ORIGINAL ([ABCD]=42): [ACD] =", orig)
assert orig == 28
var = r * 45
print("VARIANT ([PQRS]=45): [PRS] =", var)
