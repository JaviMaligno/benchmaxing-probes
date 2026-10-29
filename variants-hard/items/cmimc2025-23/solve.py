from sympy import Point, Circle, Polygon, Line, sqrt, simplify, nsimplify

def build(L):
    A, B = Point(-L/2, 0), Point(L/2, 0)
    C, D = Circle(A, A.distance(B)).intersection(Circle(B, A.distance(B)))
    if C.y < 0: C, D = D, C          # C above line AB
    r = C.distance(D)
    E, F = Circle(C, r).intersection(Circle(D, r))
    if E.x > F.x: E, F = F, E        # E, A, B, F in order
    r2 = E.distance(F)
    G, H = Circle(E, r2).intersection(Circle(F, r2))
    if H.y > 0: G, H = H, G          # H opposite side from C
    return dict(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H)

def area(P, names):
    pts = [P[n] for n in names]
    poly = Polygon(*pts)
    # check simple polygon: no non-adjacent edges intersect
    n = len(pts)
    from sympy import Segment
    segs = [Segment(pts[i], pts[(i+1) % n]) for i in range(n)]
    for i in range(n):
        for j in range(i+2, n):
            if i == 0 and j == n-1: continue
            assert not segs[i].intersection(segs[j]), "self-intersecting"
    return simplify(abs(poly.area))

from sympy import Rational
orig = area(build(1), "ACFHE")
print("original AB=1, pentagon ACFHE:", orig)
assert simplify(orig - Rational(11, 4)*sqrt(3)) == 0
var = area(build(2), "ACFGE")
print("variant AB=2, pentagon ACFGE:", var, "=", float(var))
