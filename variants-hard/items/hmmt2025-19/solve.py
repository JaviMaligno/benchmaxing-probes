"""hmmt2025-19 variant check.
Two uniform points in a regular hexagon; the line through them hits two edges.
Classify by edge-index gap d in {1 (adjacent), 2 (one edge between), 3 (opposite)}.
Method A (exact-ish): Blaschke-Petkantschin, dP dQ = |t1-t2| dt1 dt2 dG, so
P(class) = (1/A^2) * integral over lines in class of chord^3/3 dG.
For fixed direction the chord length is linear in p between vertex projections,
so the p-integral of chord^3 is done exactly by 2-pt Gauss; theta via mpmath quad.
Method B: Monte Carlo with explicit point sampling.
"""
import math, random
from fractions import Fraction
import mpmath as mp

V = [(mp.cos(mp.pi*k/3), mp.sin(mp.pi*k/3)) for k in range(6)]
E = [(V[k], V[(k+1) % 6]) for k in range(6)]  # edge k from V[k] to V[k+1]
A = 3*mp.sqrt(3)/2

def chord(th, p):
    n = (mp.cos(th), mp.sin(th))
    hits = []
    for k, (a, b) in enumerate(E):
        fa = n[0]*a[0]+n[1]*a[1]-p; fb = n[0]*b[0]+n[1]*b[1]-p
        if fa*fb < 0:
            t = fa/(fa-fb)
            hits.append((k, (a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1]))))
    if len(hits) != 2: return None
    (k1, x1), (k2, x2) = hits
    d = abs(k1-k2); d = min(d, 6-d)
    return d, mp.sqrt((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)

def theta_integrand(th):
    n = (mp.cos(th), mp.sin(th))
    ps = sorted(n[0]*v[0]+n[1]*v[1] for v in V)
    out = {1: 0, 2: 0, 3: 0}
    g = [(-1/mp.sqrt(3)), (1/mp.sqrt(3))]
    for lo, hi in zip(ps, ps[1:]):
        if hi-lo < mp.mpf(10)**-25: continue
        mid = (lo+hi)/2; half = (hi-lo)/2
        c = chord(th, mid)
        if c is None: continue
        d = c[0]
        s = sum(chord(th, mid+half*x)[1]**3 for x in g)*half
        out[d] += s/3
    return out

mp.mp.dps = 30
breaks = [mp.pi*k/6 for k in range(7)]  # vertex-projection order changes at multiples of pi/6
res = {}
for d in (1, 2, 3):
    res[d] = mp.quad(lambda t: theta_integrand(t)[d], breaks)/A**2
tot = sum(res.values())
print("total (should be 1):", mp.nstr(tot, 20))
for d, name in [(3, "opposite (ORIGINAL)"), (1, "adjacent (VARIANT)"), (2, "gap-one")]:
    print(name, mp.nstr(res[d], 20), Fraction(float(res[d])).limit_denominator(1000))

# Monte Carlo
random.seed(1)
Vf = [(math.cos(math.pi*k/3), math.sin(math.pi*k/3)) for k in range(6)]
def inside(x, y):
    for k in range(6):
        a, b = Vf[k], Vf[(k+1) % 6]
        if (b[0]-a[0])*(y-a[1])-(b[1]-a[1])*(x-a[0]) < 0: return False
    return True
def samp():
    while True:
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if inside(x, y): return x, y
cnt = {1: 0, 2: 0, 3: 0}; N = 300000
for _ in range(N):
    (x1, y1), (x2, y2) = samp(), samp()
    nx, ny = -(y2-y1), x2-x1
    p = nx*x1+ny*y1
    ks = []
    for k in range(6):
        a, b = Vf[k], Vf[(k+1) % 6]
        fa = nx*a[0]+ny*a[1]-p; fb = nx*b[0]+ny*b[1]-p
        if fa*fb < 0: ks.append(k)
    if len(ks) == 2:
        d = abs(ks[0]-ks[1]); cnt[min(d, 6-d)] += 1
print("MC:", {d: cnt[d]/N for d in cnt})
assert Fraction(float(res[3])).limit_denominator(1000) == Fraction(4, 9)
print("original check 4/9: OK")
