# Brute force: find all pairwise intersection points of the three ellipses
# (foci at two vertices, distance sum = k * side), enumerate all triangles of
# intersection points whose edges do not meet the edges of ABC, and report the
# ratio (largest side of GHI)/(side of ABC). Exact value via sympy on the
# symmetry line, numeric search as independent check.
import itertools, math
import numpy as np
import sympy as sp

A = np.array([0.0, 0.0]); B = np.array([1.0, 0.0]); C = np.array([0.5, math.sqrt(3) / 2])
V = {'A': A, 'B': B, 'C': C}

def intersections(f1, f2, f3, k):
    # E_{f1 f2} and E_{f2 f3}: PF1+PF2=k, PF2+PF3=k. Grid seed + Newton.
    def F(p):
        return np.array([np.linalg.norm(p - V[f1]) + np.linalg.norm(p - V[f2]) - k,
                         np.linalg.norm(p - V[f2]) + np.linalg.norm(p - V[f3]) - k])
    pts = []
    for sx in np.linspace(-3, 4, 15):
        for sy in np.linspace(-3, 4, 15):
            p = np.array([sx, sy])
            for _ in range(30):
                h = 1e-7
                J = np.column_stack([(F(p + [h, 0]) - F(p)) / h, (F(p + [0, h]) - F(p)) / h])
                try:
                    p = p - np.linalg.solve(J, F(p))
                except np.linalg.LinAlgError:
                    break
            if np.linalg.norm(F(p)) < 1e-10 and not any(np.linalg.norm(p - q) < 1e-6 for q in pts):
                pts.append(p)
    return pts

def seg_intersect(p1, p2, q1, q2):
    def cr(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    d1, d2 = cr(q1, q2, p1), cr(q1, q2, p2)
    d3, d4 = cr(p1, p2, q1), cr(p1, p2, q2)
    return (d1 * d2 <= 0) and (d3 * d4 <= 0)

def numeric_ratio(k):
    pts = []
    for trip in [('A', 'B', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B')]:
        # pairs (E_AB,E_BC), (E_BC,E_CA), (E_CA,E_AB)
        for p in intersections(*trip, k):
            if not any(np.linalg.norm(p - q) < 1e-6 for q in pts):
                pts.append(p)
    tri = [A, B, C]
    abc_edges = [(tri[i], tri[(i + 1) % 3]) for i in range(3)]
    ratios = set()
    for G, H, I in itertools.combinations(pts, 3):
        area = abs((H[0]-G[0])*(I[1]-G[1]) - (H[1]-G[1])*(I[0]-G[0]))
        if area < 1e-9:
            continue
        edges = [(G, H), (H, I), (I, G)]
        if any(seg_intersect(e[0], e[1], f[0], f[1]) for e in edges for f in abc_edges):
            continue
        ratios.add(round(max(np.linalg.norm(G-H), np.linalg.norm(H-I), np.linalg.norm(I-G)), 9))
    return len(pts), sorted(ratios)

def exact_ratio(k):
    # E_AB ∩ E_BC lies on PA = PC: line from B through midpoint M of AC; take far point beyond B.
    t = sp.symbols('t', real=True)
    Bx, By = 1, 0; Mx, My = sp.Rational(1, 4), sp.sqrt(3) / 4
    Px, Py = Bx + t * (Mx - Bx), By + t * (My - By)
    PA = sp.sqrt(Px**2 + Py**2); PB = sp.sqrt((Px - 1)**2 + Py**2)
    sols = [s for s in sp.solve(sp.Eq(PA + PB, k), t) if s < 0]
    assert len(sols) == 1
    R = (sp.Rational(2, 3) - sols[0]) * sp.sqrt(3) / 2   # distance from centroid
    return sp.radsimp(sp.nsimplify(sp.simplify(sp.sqrt(3) * R)))

for label, k in [('ORIGINAL (sum = 2*side, through C)', 2), ('VARIANT (sum = 3/2*side)', sp.Rational(3, 2))]:
    n, rs = numeric_ratio(float(k))
    ex = exact_ratio(k)
    print(label, '| intersection points:', n, '| valid-triangle ratios:', rs,
          '| exact:', ex, '=', float(ex))

orig = (12 * sp.sqrt(3) + 4) / 13
print('original check:', sp.simplify(exact_ratio(2) - orig) == 0)
