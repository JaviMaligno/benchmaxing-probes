from sympy import Rational, sqrt, Point, Line, Triangle, nsimplify, simplify

def area_foot(ab, ac, bc):
    # Place A at origin, B on x-axis; find C from side lengths (exact)
    A = Point(0, 0); B = Point(ab, 0)
    x = Rational(ab**2 + ac**2 - bc**2, 2*ab)
    y = sqrt(ac**2 - x**2)
    C = Point(x, y)
    D = Line(A, B).projection(C)
    return simplify(abs(Triangle(A, C, D).area))

def area_similar(ab, ac, bc):
    # solution-method formula (right angle at C)
    assert ac**2 + bc**2 == ab**2
    cd = Rational(bc*ac, ab); ad = Rational(ac*ac, ab)
    return Rational(1, 2)*ad*cd

orig = area_foot(17, 8, 15)
print("original (coords):", orig, " (similarity):", area_similar(17, 8, 15))
assert orig == Rational(3840, 289) == area_similar(17, 8, 15)

var = area_foot(25, 7, 24)
print("variant (coords):", var, " (similarity):", area_similar(25, 7, 24), float(var))
assert var == area_similar(25, 7, 24)
