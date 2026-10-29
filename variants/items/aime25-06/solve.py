# Isosceles tangential trapezoid: incircle radius R, area A, parallel sides r != s. Find r^2+s^2.
import sympy as sp
import math

def solve(R, A):
    r, s = sp.symbols('r s', positive=True)
    h = 2*R
    leg = (r + s) / 2                      # Pitot: r + s = 2*leg
    eqs = [sp.Eq((r + s) / 2 * h, A),      # area
           sp.Eq(leg**2, h**2 + ((r - s) / 2)**2)]  # leg from height and half-difference
    sols = [x for x in sp.solve(eqs, [r, s], dict=True) if sp.simplify(x[r] - x[s]) != 0]
    vals = {sp.nsimplify(sp.simplify(x[r]**2 + x[s]**2)) for x in sols}
    assert len(vals) == 1, vals
    v = vals.pop()
    # independent numeric check: build trapezoid, verify the circle of radius R
    # centred on the axis at height R is tangent to all four sides and area matches
    x = sols[0]
    rv, sv = float(x[r]), float(x[s])
    P = [(-rv/2, 0), (rv/2, 0), (sv/2, 2*R), (-sv/2, 2*R)]
    c = (0.0, R)
    def dist(p, q):
        (x1, y1), (x2, y2) = p, q
        return abs((y2-y1)*c[0] - (x2-x1)*c[1] + x2*y1 - y2*x1) / math.hypot(x2-x1, y2-y1)
    for i in range(4):
        assert abs(dist(P[i], P[(i+1) % 4]) - R) < 1e-9
    area = 0.5*abs(sum(P[i][0]*P[(i+1)%4][1] - P[(i+1)%4][0]*P[i][1] for i in range(4)))
    assert abs(area - A) < 1e-9
    assert abs(rv**2 + sv**2 - float(v)) < 1e-6
    return v

orig = solve(3, 72)
print("original (R=3, A=72):", orig)
assert orig == 504
var = solve(5, 160)
print("variant (R=5, A=160):", var)
