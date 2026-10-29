# Probability that a uniform point in a convex polygon is closer to its center O
# than to every vertex. Exact: clip polygon by half-planes |P-O|^2 < |P-V|^2
# (linear in P) with sympy exact arithmetic; plus a Monte Carlo cross-check.
import random
import sympy as sp

def area(poly):
    return sp.Rational(1, 2) * abs(sum(poly[i][0]*poly[(i+1) % len(poly)][1]
                                       - poly[(i+1) % len(poly)][0]*poly[i][1]
                                       for i in range(len(poly))))

def clip(poly, a, b, c):  # keep a*x + b*y <= c
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i+1) % n]
        fp = a*P[0] + b*P[1] - c
        fq = a*Q[0] + b*Q[1] - c
        if float(fp) <= 1e-12:
            out.append(P)
        if float(fp)*float(fq) < -1e-12:
            t = fp / (fp - fq)
            out.append((sp.simplify(P[0] + t*(Q[0]-P[0])), sp.simplify(P[1] + t*(Q[1]-P[1]))))
    return out

def exact_prob(poly, O):
    region = list(poly)
    for V in poly:
        # |P-O|^2 <= |P-V|^2  <=>  2(V-O).P <= |V|^2 - |O|^2
        a, b = 2*(V[0]-O[0]), 2*(V[1]-O[1])
        c = V[0]**2 + V[1]**2 - O[0]**2 - O[1]**2
        region = clip(region, a, b, c)
    return sp.nsimplify(sp.simplify(area(region) / area(poly)))

def mc_prob(poly, O, N=100000, seed=1):
    rnd = random.Random(seed)
    xs = [float(p[0]) for p in poly]; ys = [float(p[1]) for p in poly]
    P = [(float(p[0]), float(p[1])) for p in poly]
    def inside(x, y):
        s = None
        for i in range(len(P)):
            (x1, y1), (x2, y2) = P[i], P[(i+1) % len(P)]
            cr = (x2-x1)*(y-y1) - (y2-y1)*(x-x1)
            if s is None: s = cr > 0
            elif (cr > 0) != s: return False
        return True
    ox, oy = float(O[0]), float(O[1])
    hit = tot = 0
    while tot < N:
        x = rnd.uniform(min(xs), max(xs)); y = rnd.uniform(min(ys), max(ys))
        if not inside(x, y): continue
        tot += 1
        d0 = (x-ox)**2 + (y-oy)**2
        if all(d0 < (x-vx)**2 + (y-vy)**2 for vx, vy in P): hit += 1
    return hit / tot

# ORIGINAL: rectangle, AB/AD = k, several k -> expect 1/2
for k in [sp.Rational(5, 2), 1, 3, sp.Rational(7, 4)]:
    rect = [(-k, 1), (k, 1), (k, -1), (-k, -1)]
    pe = exact_prob(rect, (0, 0))
    print(f"original k={k}: exact={pe}, MC={mc_prob(rect, (0,0)):.4f}")
    assert pe == sp.Rational(1, 2)

# VARIANT: equilateral triangle, O = center
tri = [(0, 2), (-sp.sqrt(3), -1), (sp.sqrt(3), -1)]
O = (0, 0)
pv = exact_prob(tri, O)
print(f"variant exact={pv}, MC={mc_prob(tri, O):.4f}")
