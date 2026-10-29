import sympy as sp
x, t = sp.symbols('x t', real=True)

def dist(px, py, m, c):
    # Method of the solution: perpendicular through the point, intersect, distance.
    b = py + px / m                      # perpendicular y = -x/m + b
    xi = sp.solve(sp.Eq(-x/m + b, m*x + c), x)[0]
    yi = m*xi + c
    d = sp.sqrt((px-xi)**2 + (py-yi)**2)
    # independent check: minimise squared distance over points (t, m t + c)
    f = (t-px)**2 + (m*t+c-py)**2
    tm = sp.solve(sp.diff(f, t), t)[0]
    d2 = sp.sqrt(f.subs(t, tm))
    assert sp.simplify(d - d2) == 0
    # formula check
    assert sp.simplify(d - sp.Abs(m*px - py + c)/sp.sqrt(m**2+1)) == 0
    return sp.nsimplify(sp.radsimp(d)), (xi, yi)

orig, foot = dist(sp.Integer(6), sp.Integer(0), sp.Integer(2), sp.Integer(-2))
print("original:", orig, "foot", foot)
assert sp.simplify(orig - 2*sp.sqrt(5)) == 0
var, foot = dist(sp.Integer(7), sp.Integer(0), sp.Integer(3), sp.Integer(-1))
print("variant:", var, "foot", foot, float(var))
