from fractions import Fraction
from itertools import product

def inter(m1, k1, m2, k2):
    x = Fraction(k2 - k1, m1 - m2)
    return (x, m1 * x + k1)

def area(a, b, p, q):
    # parallelogram bounded by y=ax+p, y=ax+q, y=bx+p, y=bx+q (shoelace on vertices)
    V = [inter(a, p, b, p), inter(a, p, b, q), inter(a, q, b, q), inter(a, q, b, p)]
    s = 0
    for i in range(4):
        x1, y1 = V[i]; x2, y2 = V[(i + 1) % 4]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2

def best(S1, S2, N=40):
    res = None
    for a, b, c, d in product(range(1, N + 1), repeat=4):
        if a == b or c == d:
            continue
        if res is not None and a + b + c + d >= res:
            continue
        if area(a, b, c, d) == S1 and area(a, b, c, -d) == S2:
            res = a + b + c + d
    return res

orig = best(18, 72)
print("original (18, 72):", orig)
assert orig == 16
var = best(8, 50)
print("variant (8, 50):", var)
