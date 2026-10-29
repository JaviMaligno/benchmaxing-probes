import sympy as sp

def area_from_altitude(h):
    # Isosceles right triangle: right angle at A=(0,a), B=(a,0)... use legs of length L
    L = sp.symbols('L', positive=True)
    A, B, C = sp.Matrix([0, 0]), sp.Matrix([L, 0]), sp.Matrix([0, L])
    # distance from right-angle vertex A to hypotenuse BC
    BC = C - B
    dist = sp.Abs(BC[0]*(B[1]-A[1]) - BC[1]*(B[0]-A[0])) / sp.sqrt(BC.dot(BC))
    Lval = [s for s in sp.solve(sp.Eq(sp.simplify(dist), h), L) if s.is_positive][0]
    area = sp.nsimplify(sp.simplify(Lval**2 / 2))
    # independent numeric check: area = altitude * hypotenuse / 2
    num = float(h) * float(sp.sqrt(2) * Lval) / 2
    assert abs(num - float(area)) < 1e-9
    return area

orig = area_from_altitude(4*sp.sqrt(2))
print("original:", orig)
assert orig == 32
var = area_from_altitude(6*sp.sqrt(2))
print("variant:", var)
