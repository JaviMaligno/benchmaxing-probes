# Numeric construction (independent of the closed form r2^2 = r1*R):
# S3: centre O=(0,0), radius R, diameter AB on x-axis, arc above.
# S2: tangent to AB at C=(c,0), so centre M=(c,r2); its diameter is a chord of S3
#     with midpoint M, hence r2^2 + |OM|^2 = R^2 -> c^2 = R^2 - 2 r2^2.
# S1: diameter horizontal (parallel to AB) and a chord of S2 -> centre N = M + (0,t),
#     r1^2 + t^2 = r2^2; arc tangent to S2's diameter line L (through M, normal OM):
#     dist(N, L) = r1. S1 must lie on the arc side of L (the side containing C).
import math
from fractions import Fraction

def residual(r2, r1, R):
    c = math.sqrt(R*R - 2*r2*r2)
    u = (c/math.hypot(c, r2), r2/math.hypot(c, r2))   # unit normal of L (direction OM)
    if r2 < r1: return None
    t = -math.sqrt(r2*r2 - r1*r1)                     # N below M: towards C (arc side)
    # check side: C - M = (0,-r2); sign of (C-M).u must equal sign of (N-M).u
    sC = (0*u[0] + (-r2)*u[1]); sN = t*u[1]
    assert sC*sN > 0
    return abs(t*u[1]) - r1, c

def solve(r1, R):
    lo, hi = r1*(1+1e-12), R/math.sqrt(2)*(1-1e-12)
    f = lambda x: residual(x, r1, R)[0]
    assert f(lo)*f(hi) < 0
    for _ in range(200):
        mid = (lo+hi)/2
        if f(lo)*f(mid) <= 0: hi = mid
        else: lo = mid
    r2 = (lo+hi)/2
    _, c = residual(r2, r1, R)
    # verify S1's chord endpoints lie on S2's circle
    M = (c, r2); N = (c, r2 - math.sqrt(r2*r2 - r1*r1))
    for e in ((N[0]-r1, N[1]), (N[0]+r1, N[1])):
        assert abs(math.hypot(e[0]-M[0], e[1]-M[1]) - r2) < 1e-9
        assert e[1] > -1e-12  # inside S3's half-plane
    AC_CB = (R - c)*(R + c)
    return AC_CB, r2, c

orig, r2o, co = solve(1, 10)
print("ORIGINAL (r1=1,R=10): AC*CB =", orig, " r2 =", r2o, " c =", co)
assert abs(orig - 20) < 1e-9
var, r2v, cv = solve(3, 12)
print("VARIANT  (r1=3,R=12): AC*CB =", var, " r2 =", r2v, " c =", cv)
print("closed form 2*r1*R:", Fraction(2*3*12), " rounded numeric:", round(var))
assert abs(var - 72) < 1e-9
