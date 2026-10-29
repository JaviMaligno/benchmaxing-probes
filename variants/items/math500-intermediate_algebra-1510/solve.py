# Variant: distinct unit complex a,b,c,d with a+b+c+d=0; max |prod_{i<j}(z_i - z_j)|.
# Original: same constraint, max |prod_{i<j}(z_i + z_j)| (expected 0).
# Independent numeric search: sample a,b,c on the unit circle, solve for configs where
# d = -(a+b+c) is also on the unit circle (fix a=1 by rotation invariance; for given b,
# choose c on the circle such that |1+b+c|=1, solved exactly as circle intersection).
import cmath, math, itertools, random
from sympy import exp, I, pi, Abs, nsimplify, simplify, prod as sprod

def configs(N=4000):
    out = []
    for k in range(1, N):
        t = 2*math.pi*k/N
        a, b = 1, cmath.exp(1j*t)
        s = a + b  # need c with |c|=1, |s+c|=1: intersection of unit circle with circle centre -s radius 1
        r = abs(s)
        if r < 1e-12 or r >= 2: continue
        # points c with |c|=1 and |c+s|=1: c = -s/2 +- i*(s/r)*sqrt(1 - r^2/4)
        h = math.sqrt(max(0.0, 1 - r*r/4))
        for sg in (1, -1):
            c = -s/2 + sg*1j*(s/r)*h
            d = -(a+b+c)
            zs = [a, b, c, d]
            if min(abs(x-y) for x, y in itertools.combinations(zs, 2)) > 1e-6:
                out.append(zs)
    return out

cs = configs()
orig = max(abs(math.prod(x+y for x, y in itertools.combinations(z, 2))) for z in cs)
var = max(abs(math.prod(x-y for x, y in itertools.combinations(z, 2))) for z in cs)
print("configs:", len(cs))
print("original numeric max |prod (zi+zj)| =", round(orig, 9))
print("variant numeric max |prod (zi-zj)|  =", round(var, 9))
# exact value at the square configuration 1, i, -1, -i
sq = [1, I, -1, -I]
print("exact at square:", simplify(Abs(sprod([x-y for x, y in itertools.combinations(sq, 2)]))))
assert round(orig, 9) == 0
assert abs(var - 16) < 1e-6
print("ORIGINAL ANSWER 0 reproduced; VARIANT ANSWER = 16")
