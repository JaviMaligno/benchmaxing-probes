# Rectangle inscribed in small circle; equal-area triangles condition.
import sympy as sp
from fractions import Fraction

def tri_area(P, Q, R):
    return sp.Abs((Q[0]-P[0])*(R[1]-P[1]) - (R[0]-P[0])*(Q[1]-P[1])) / 2

def solve(r1, r2):
    A = (0, 0); B = (r1, 0); O = (r1 - r2, 0); C = (r1 - 2*r2, 0)
    yD = sp.sqrt(r2**2 - (r2 - r1)**2)
    D = (0, yD)  # AD perpendicular to BC, D on omega2
    assert sp.simplify((D[0]-O[0])**2 + (D[1]-O[1])**2 - r2**2) == 0
    a, b = sp.symbols('a b', positive=True)
    # E=(a,-b), F=(a,b), G=(-a,b), H=(-a,-b): EF vertical (perp BC), GH nearer C, FG nearer D
    E, F, G, H = (a, -b), (a, b), (-a, b), (-a, -b)
    eqs = [a**2 + b**2 - r1**2,
           (a*(yD - b)) - (b*(-C[0] - a))]  # areas DGF and CHG (signs valid for a<r1, b<yD)
    sols = sp.solve(eqs, [a, b], dict=True)
    res = []
    for s in sols:
        av, bv = s[a], s[b]
        assert av < r1 and bv < yD
        # independent numeric check of triangle areas with shoelace
        dgf = tri_area(D, (-av, bv), (av, bv)); chg = tri_area(C, (-av, -bv), (-av, bv))
        assert abs(float(dgf - chg)) < 1e-12
        area = sp.nsimplify(sp.simplify(4*av*bv))
        res.append(area)
    assert len(res) == 1
    q = sp.Rational(res[0])
    return q, q.p + q.q

q0, ans0 = solve(6, 15)
print("original: area =", q0, " m+n =", ans0, " matches 293:", ans0 == 293)
q1, ans1 = solve(4, 20)
print("variant:  area =", q1, " m+n =", ans1)
