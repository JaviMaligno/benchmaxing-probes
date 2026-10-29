import sympy as sp

def solve(be, ef, fc):
    s3 = sp.sqrt(3)
    L = be + ef + fc
    B = sp.Matrix([0, 0]); C = sp.Matrix([L, 0])
    A = sp.Matrix([sp.Rational(L, 2), L * s3 / 2])  # above line
    E = sp.Matrix([be, 0]); F = sp.Matrix([be + ef, 0])
    # D is apex of equilateral DEF on the same side as A (needed for D inside ABC)
    D = sp.Matrix([be + sp.Rational(ef, 2), ef * s3 / 2])
    # check D strictly inside ABC via barycentric signs
    def cross(o, p, q):
        return (p[0]-o[0])*(q[1]-o[1]) - (p[1]-o[1])*(q[0]-o[0])
    signs = [sp.sign(sp.simplify(cross(B, C, D))), sp.sign(sp.simplify(cross(C, A, D))), sp.sign(sp.simplify(cross(A, B, D)))]
    assert all(s == signs[0] and s != 0 for s in signs), "D not inside"
    # the other apex (below line) is outside, so D is unique
    AD = sp.sqrt(sp.simplify((A - D).dot(A - D)))
    return sp.nsimplify(sp.simplify(AD))

orig = solve(14, 15, 16)
print("original:", orig)
assert orig == 26
var = solve(11, 13, 24)
print("variant:", var)
# numeric cross-check
import math
L = 48; ax, ay = L/2, L*math.sqrt(3)/2; dx, dy = 11+6.5, 13*math.sqrt(3)/2
print("numeric:", math.hypot(ax-dx, ay-dy))
