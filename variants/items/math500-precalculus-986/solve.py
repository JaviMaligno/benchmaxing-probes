# Variant check: squared distances d12, d13, d23 -> det^2 = (2*area)^2
from sympy import Matrix, sqrt, Rational, simplify, nsimplify
import random, math

def det_sq_from_coords(d12, d13, d23):
    # Place P1=(0,0), P2=(sqrt(d12),0), solve for P3 exactly
    a = sqrt(d12)
    x3 = (d13 - d23 + d12) / (2*a)
    y3 = sqrt(d13 - x3**2)
    M = Matrix([[0, 0, 1], [a, 0, 1], [x3, y3, 1]])
    return simplify(M.det()**2)

def det_sq_heron(d12, d13, d23):
    # 16*Area^2 = 2(ab+bc+ca) - (a^2+b^2+c^2) with squared sides; det^2 = 4*Area^2
    s = 2*(d12*d13 + d13*d23 + d23*d12) - (d12**2 + d13**2 + d23**2)
    return Rational(s, 4)

def numeric_random_check(d12, d13, d23, trials=5):
    # random rigid motion / reflection of a valid configuration
    a = math.sqrt(d12); x3 = (d13 - d23 + d12)/(2*a); y3 = math.sqrt(d13 - x3*x3)
    pts = [(0,0),(a,0),(x3,y3)]
    out = []
    for _ in range(trials):
        t = random.uniform(0, 2*math.pi); tx, ty = random.uniform(-9,9), random.uniform(-9,9)
        f = random.choice([1,-1])
        P = [(math.cos(t)*x - math.sin(t)*f*y + tx, math.sin(t)*x + math.cos(t)*f*y + ty) for x,y in pts]
        (x1,y1),(x2,y2),(x3_,y3_) = P
        D = x1*(y2-y3_) - y1*(x2-x3_) + (x2*y3_ - x3_*y2)
        out.append(round(D*D, 6))
    return out

orig = (9, 16, 25)
var = (25, 169, 144)
for name, d in [("original", orig), ("variant", var)]:
    print(name, det_sq_from_coords(*d), det_sq_heron(*d), numeric_random_check(*d))
assert det_sq_from_coords(*orig) == 144 and det_sq_heron(*orig) == 144
print("ORIGINAL_OK", det_sq_heron(*orig) == 144)
print("VARIANT_ANSWER", det_sq_heron(*var))
