from fractions import Fraction as Fr
import sympy as sp

def solve(AC, BD, CE, DF, AF, CG, DG):
    A = 0; C = AC; F = AF; D = F - DF; B = D - BD; E = C + CE
    assert A < B < C < D < E < F, (A, B, C, D, E, F)
    # place G = (x, y), y > 0, with |CG|, |DG| given
    x, y = sp.symbols('x y', real=True)
    sols = sp.solve([(x - C)**2 + y**2 - CG**2, (x - D)**2 + y**2 - DG**2], [x, y], dict=True)
    sols = [s for s in sols if s[y] > 0]
    assert len(sols) == 1
    h = sols[0][y]
    area = sp.nsimplify(sp.Rational(1, 2) * (E - B) * h)
    # independent check: shoelace with numeric coordinates
    gx, gy = float(sols[0][x]), float(h)
    shoe = abs(B * (0 - gy) + E * (gy - 0) + gx * (0 - 0)) / 2
    assert abs(shoe - float(area)) < 1e-9
    return area

orig = solve(26, 22, 31, 33, 73, 40, 30)
print("original:", orig)
assert orig == 468
var = solve(24, 30, 37, 29, 74, 17, 10)
print("variant:", var)
