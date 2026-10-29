from sympy import Rational, sqrt, symbols, solve, nsimplify
import math

def exact(HC, HD, CD):
    # triangle HCD: foot P of altitude from H on CD; PD=a
    a = Rational(CD**2 + HD**2 - HC**2, 2*CD)
    assert 0 < a < CD, "foot must lie on segment CD"
    x = sqrt(HD**2 - a**2)
    return nsimplify(HC + HD - x)

def numeric(HC, HD, CD, N=200000):
    # build 3D configuration: O origin, C south (0,-c), D east (d,0), H (0,0,h)
    h2 = (HC**2 + HD**2 - CD**2) / 2
    assert h2 > 0
    h = math.sqrt(h2); c = math.sqrt(HC**2 - h2); d = math.sqrt(HD**2 - h2)
    C = (0, -c, 0); D = (d, 0, 0); H = (0, 0, h)
    best = min(math.dist(H, tuple(C[k] + t/N*(D[k]-C[k]) for k in range(3))) for t in range(N+1))
    return HC + HD - best

for name, data in [("original", (150, 130, 140)), ("variant", (145, 125, 180))]:
    e = exact(*data); n = numeric(*data)
    print(name, data, "exact:", e, "numeric:", round(n, 4))
assert exact(150, 130, 140) == 160
print("original check OK")
