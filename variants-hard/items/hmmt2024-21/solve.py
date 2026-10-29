"""hmmt2024-21 variant check.

Model: big equilateral triangle of side s centred at origin (inradius r = s/(2*sqrt3)),
BC horizontal at the bottom. Three congruent small equilateral triangles of side x,
sides parallel to the big one. A vertex touching a side from inside forces the small
triangles to be inverted (point-down). T1 has its bottom vertex on BC at (p, -r);
T2, T3 are its rotations by 120 and 240 degrees about the centre (pinwheel).
Pinwheel condition: a vertex of T1 lies on an edge of T2 (or T3).
The central hole between the three triangles must be an equilateral triangle of side t.

For each x: solve the pinwheel condition for p exactly (sympy), check validity
(inside big triangle, disjoint interiors, vertex strictly inside the edge), then compute
the hole numerically by ray casting from the centre and bisect x on its area.
Compare with the closed form x = (s - t)/3.
"""
import math
import sympy as sp

S3 = math.sqrt(3)

def rot(pt, k):
    a = 2 * math.pi * k / 3
    c, s_ = math.cos(a), math.sin(a)
    return (c * pt[0] - s_ * pt[1], s_ * pt[0] + c * pt[1])

def tris(s, x, p):
    r = s / (2 * S3)
    t1 = [(p, -r), (p + x / 2, -r + x * S3 / 2), (p - x / 2, -r + x * S3 / 2)]
    return [[rot(v, k) for v in t1] for k in range(3)]

def big(s):
    r = s / (2 * S3)
    return [(-s / 2, -r), (s / 2, -r), (0, 2 * r)]

def inside(pt, tri, eps=1e-9):
    sg = []
    for i in range(3):
        a, b = tri[i], tri[(i + 1) % 3]
        sg.append((b[0] - a[0]) * (pt[1] - a[1]) - (b[1] - a[1]) * (pt[0] - a[0]))
    return all(v >= -eps for v in sg) or all(v <= eps for v in sg)

def strictly_inside(pt, tri, eps=1e-7):
    sg = []
    for i in range(3):
        a, b = tri[i], tri[(i + 1) % 3]
        sg.append((b[0] - a[0]) * (pt[1] - a[1]) - (b[1] - a[1]) * (pt[0] - a[0]))
    return all(v > eps for v in sg) or all(v < -eps for v in sg)

def pinwheel_p(s, x):
    """All p such that some vertex of T1 lies strictly inside an edge of T2 or T3, valid config."""
    sols = set()
    # the incidence condition is a cross product, quadratic in p: fit it exactly from 3 samples
    for k in (1, 2):
        for vi in range(3):
            for i in range(3):
                def g(p):
                    T = tris(s, x, p)
                    v = T[0][vi]; a, b = T[k][i], T[k][(i + 1) % 3]
                    return (b[0] - a[0]) * (v[1] - a[1]) - (b[1] - a[1]) * (v[0] - a[0])
                g0, g1, gm = g(0.0), g(1.0), g(-1.0)
                A = (g1 + gm) / 2 - g0; Bc = (g1 - gm) / 2; C = g0
                if abs(A) < 1e-12:
                    roots = [] if abs(Bc) < 1e-12 else [-C / Bc]
                else:
                    D = Bc * Bc - 4 * A * C
                    roots = [] if D < 0 else [(-Bc + math.sqrt(D)) / (2 * A), (-Bc - math.sqrt(D)) / (2 * A)]
                sols.update(roots)
    valid = []
    for p in sols:
        T = tris(s, x, p)
        B = big(s)
        if not all(inside(v, B) for tri in T for v in tri):
            continue
        # disjoint interiors: no vertex strictly inside another, centroids outside others
        ok = True
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                pts = T[i] + [tuple(sum(c) / 3 for c in zip(*T[i]))]
                pts += [((T[i][a][0] + T[i][(a + 1) % 3][0]) / 2, (T[i][a][1] + T[i][(a + 1) % 3][1]) / 2) for a in range(3)]
                if any(strictly_inside(q, T[j]) for q in pts):
                    ok = False
        # vertex of T1 touching T2/T3 edge strictly between endpoints
        touch = False
        for v in T[0]:
            for j in (1, 2):
                for a in range(3):
                    A, Bp = T[j][a], T[j][(a + 1) % 3]
                    cr = (Bp[0] - A[0]) * (v[1] - A[1]) - (Bp[1] - A[1]) * (v[0] - A[0])
                    if abs(cr) < 1e-9:
                        L = math.dist(A, Bp)
                        u = ((v[0] - A[0]) * (Bp[0] - A[0]) + (v[1] - A[1]) * (Bp[1] - A[1])) / L**2
                        if 1e-6 < u < 1 - 1e-6:
                            touch = True
        # the touching vertex of T1 must not be the one on BC (it must be a different vertex)
        if ok and touch and not inside((0, 0), T[0]):
            valid.append(p)
    return valid

def ray_hit(o, d, segs):
    best = math.inf
    for a, b in segs:
        ex, ey = b[0] - a[0], b[1] - a[1]
        den = d[0] * (-ey) - d[1] * (-ex)
        if abs(den) < 1e-15:
            continue
        wx, wy = a[0] - o[0], a[1] - o[1]
        tt = (wx * (-ey) - wy * (-ex)) / den
        uu = (d[0] * wy - d[1] * wx) / den
        if tt > 0 and -1e-12 <= uu <= 1 + 1e-12:
            best = min(best, tt)
    return best

def hole(s, x, p, n=1500):
    T = tris(s, x, p)
    segs = [(tri[i], tri[(i + 1) % 3]) for tri in T for i in range(3)]
    segs += [(big(s)[i], big(s)[(i + 1) % 3]) for i in range(3)]
    pts = []
    for k in range(n):
        a = 2 * math.pi * (k + 0.5) / n
        d = (math.cos(a), math.sin(a))
        h = ray_hit((0, 0), d, segs)
        pts.append((h * d[0], h * d[1]))
    area = 0.5 * abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n)))
    rmax = max(math.hypot(*q) for q in pts)
    rmin = min(math.hypot(*q) for q in pts)
    return area, rmax, rmin

def solve_x(s, t):
    target = S3 / 4 * t * t
    def f(x):
        ps = pinwheel_p(s, x)
        if not ps:
            return None
        return hole(s, x, ps[0])[0] - target, ps[0]
    # scan for a bracket
    lo, hi = None, None
    xs = [s * k / 400 for k in range(1, 200)]
    prev = None
    for x in xs:
        v = f(x)
        if v is None:
            prev = None
            continue
        if prev is not None and (prev[1] > 0) != (v[0] > 0):
            lo, hi = prev[0], x
            break
        prev = (x, v[0])
    assert lo is not None, "no valid configuration with that hole size"
    for _ in range(40):
        m = (lo + hi) / 2
        if (f(m)[0] > 0) == (f(lo)[0] > 0):
            lo = m
        else:
            hi = m
    x = (lo + hi) / 2
    p = f(x)[1]
    area, rmax, rmin = hole(s, x, p)
    # equilateral hole of side t: circumradius t/sqrt3, inradius t/(2sqrt3)
    return x, p, rmax, rmin

for label, s, t, expected in [("ORIGINAL", 6, 1, sp.Rational(5, 3)), ("VARIANT", 9, 2, None)]:
    x, p, rmax, rmin = solve_x(s, t)
    closed = sp.Rational(s - t, 3)
    print(f"{label}: s={s}, t={t}: numeric x={x:.9f}, p={p:.6f}, hole circumradius={rmax:.5f} (expect {t/S3:.5f}), inradius={rmin:.5f} (expect {t/(2*S3):.5f})")
    print(f"   closed form (s-t)/3 = {closed} = {float(closed):.9f}; match={abs(float(closed)-x)<1e-5}")
    if expected is not None:
        print(f"   original answer {expected} reproduced: {abs(float(expected)-x)<1e-5}")
