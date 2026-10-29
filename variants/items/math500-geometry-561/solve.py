# Equiangular octagon: walk the boundary turning 45 deg each side, alternating lengths; shoelace area (exact, sympy).
import sympy as sp

def area(a, b):
    pts = [(sp.Integer(0), sp.Integer(0))]
    x = y = sp.Integer(0)
    for k in range(8):
        L = a if k % 2 == 0 else b
        th = sp.pi * k / 4
        x += L * sp.cos(th); y += L * sp.sin(th)
        pts.append((sp.simplify(x), sp.simplify(y)))
    assert sp.simplify(pts[-1][0]) == 0 and sp.simplify(pts[-1][1]) == 0, "not closed"
    s = sum(pts[i][0]*pts[i+1][1] - pts[i+1][0]*pts[i][1] for i in range(8))
    return sp.nsimplify(sp.simplify(sp.Abs(s) / 2))

orig = area(sp.Integer(1), sp.sqrt(2)/2)
print("original:", orig, "matches 7/2:", orig == sp.Rational(7, 2))
var = area(sp.Integer(3), sp.sqrt(2))
print("variant:", var, float(var))
# independent check: bounding square minus 4 corner triangles, legs b/sqrt2
a, b = 3, sp.sqrt(2)
print("formula check:", sp.simplify((a + sp.sqrt(2)*b)**2 - b**2))
