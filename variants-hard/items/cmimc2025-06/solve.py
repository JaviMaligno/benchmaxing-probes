# Exact probability that |x|+|y|+c <= k*min{|x+y+c|,|x+y-c|} for x,y uniform on [-1,1].
# Method: cut the square into convex cells by lines x=0, y=0, x+y=0, x+y=+-c, where every
# absolute value has fixed sign, so the condition is one linear half-plane; clip exactly
# with Fractions and sum areas. Independent Monte Carlo check.
from fractions import Fraction as F
import itertools, random

def clip(poly, a, b, d):  # keep a*x+b*y+d >= 0
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i+1) % n]
        fp = a*P[0]+b*P[1]+d; fq = a*Q[0]+b*Q[1]+d
        if fp >= 0: out.append(P)
        if (fp > 0 and fq < 0) or (fp < 0 and fq > 0):
            t = fp/(fp-fq)
            out.append((P[0]+t*(Q[0]-P[0]), P[1]+t*(Q[1]-P[1])))
    return out

def area(p):
    if len(p) < 3: return F(0)
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))/2

def exact(k, c):
    k, c = F(k), F(c)
    sq = [(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
    total = F(0)
    # sign choices: sx, sy for x,y ; s1 for (x+y+c), s2 for (x+y-c); which term is min: m
    for sx, sy, s1, s2, m in itertools.product([1,-1],[1,-1],[1,-1],[1,-1],[0,1]):
        cell = sq
        cell = clip(cell, sx, 0, 0)          # sx*x >= 0
        cell = clip(cell, 0, sy, 0)
        cell = clip(cell, s1, s1, s1*c)      # s1*(x+y+c) >= 0
        cell = clip(cell, s2, s2, -s2*c)
        # |x+y+c| = s1*(x+y+c), |x+y-c| = s2*(x+y-c); m=0 -> first is min: s1(.)-s2(.) <= 0
        A = s1 - s2; D = s1*c + s2*c   # s1(s+c) - s2(s-c) = A*s + D
        if m == 0: cell = clip(cell, -A, -A, -D)
        else: cell = clip(cell, A, A, D)
        if area(cell) == 0: continue
        if m == 0: ma, md = s1, s1*c
        else: ma, md = s2, -s2*c
        # k*(ma*(x+y)+md) - (sx*x+sy*y+c) >= 0
        cell = clip(cell, k*ma - sx, k*ma - sy, k*md - c)
        total += area(cell)
    # ties (measure zero) could double count only on lines; fine.
    return total / 4

def mc(k, c, N=400000, seed=1):
    r = random.Random(seed); h = 0
    for _ in range(N):
        x = r.uniform(-1,1); y = r.uniform(-1,1)
        if abs(x)+abs(y)+c <= k*min(abs(x+y+c), abs(x+y-c)): h += 1
    return h/N

orig = exact(3, 1)
print("original (k=3,c=1):", orig, "MC", mc(3,1))
assert orig == F(5,16)
for k in [2,4,5]:
    for c in [1, F(1,2)]:
        print("k=%s c=%s:" % (k,c), exact(k,c))
var = exact(4, 1)
print("variant (k=4,c=1):", var, float(var), "MC", mc(4,1))
