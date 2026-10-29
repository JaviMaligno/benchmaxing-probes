"""Shortest path on the walls+ceiling (no floor) of a box room.
Method: for every face sequence from the gecko's side wall to the fly's side wall
(no floor, no face repeated, up to 5 faces), the path is piecewise linear with crossing
points on shared edges; total length is convex in the crossing parameters, so we
minimise it numerically (bounded). Exact value then identified by unfolding (sympy)."""
import itertools, math
import numpy as np
from scipy.optimize import minimize
import sympy as sp

def faces(L, W, H):
    # each face: fixed coordinate (axis, value)
    return {'S0': (0, 0), 'SL': (0, L), 'B': (1, 0), 'F': (1, W), 'C': (2, H)}

def edge(f1, f2, L, W, H):
    fs = faces(L, W, H)
    (a1, v1), (a2, v2) = fs[f1], fs[f2]
    if a1 == a2:
        return None
    free = 3 - a1 - a2
    lo = np.zeros(3); hi = np.zeros(3)
    lo[a1] = hi[a1] = v1; lo[a2] = hi[a2] = v2
    hi[free] = [L, W, H][free]
    return lo, hi

def shortest(L, W, H, g, f):
    names = ['B', 'F', 'C']
    best = (math.inf, None)
    for k in range(0, 4):
        for mid in itertools.permutations(names, k):
            seq = ['SL'] + list(mid) + ['S0']
            edges = [edge(seq[i], seq[i+1], L, W, H) for i in range(len(seq)-1)]
            if any(e is None for e in edges):
                continue
            def length(t):
                pts = [np.array(g, float)] + [lo + ti*(hi-lo) for ti, (lo, hi) in zip(t, edges)] + [np.array(f, float)]
                return sum(np.linalg.norm(pts[i+1]-pts[i]) for i in range(len(pts)-1))
            n = len(edges)
            vals = []
            for start in itertools.product([0.2, 0.5, 0.8], repeat=n):
                r = minimize(length, start, bounds=[(0, 1)]*n, method='L-BFGS-B')
                vals.append(r.fun)
            v = min(vals)
            if v < best[0] - 1e-9:
                best = (v, seq)
    return best

def exact_candidates(L, W, H, gb, gt, ff, fb):
    """Unfolding formulas (gecko gb from back wall, gt from ceiling; fly ff from front wall,
    fb from floor). Returns exact sympy expressions for the classic cases."""
    L, W, H = map(sp.Integer, (L, W, H))
    cands = {}
    yg, yf = gb, W - ff          # distances from back wall
    zg, zf = H - gt, fb          # heights
    # side walls + back wall only / front wall only
    cands['back'] = sp.sqrt((yg + L + yf)**2 + (zg - zf)**2)
    cands['front'] = sp.sqrt(((W-yg) + L + (W-yf))**2 + (zg - zf)**2)
    # side walls + ceiling only
    cands['ceiling'] = sp.sqrt((gt + L + (H-fb))**2 + (yg - yf)**2)
    # ceiling then front/back wall (unfolded onto the ceiling plane)
    cands['ceil+front'] = sp.sqrt((gt + L + (W-yf))**2 + (W + (H-zf) - yg)**2)
    cands['ceil+back'] = sp.sqrt((gt + L + yf)**2 + (yg + (H-zf))**2)
    # front/back wall then ceiling
    cands['front+ceil'] = sp.sqrt(((W-yg) + L + (H-zf))**2 + ((W + gt) - yf)**2)
    cands['back+ceil'] = sp.sqrt((yg + L + (H-zf))**2 + (yf + gt)**2)
    return {k: sp.nsimplify(sp.radsimp(v)) for k, v in cands.items()}

def run(label, L, W, H, gb, gt, ff, fb):
    # coordinates: x along length (gecko wall x=L, fly wall x=0), y from back wall (y=0) to front (y=W), z up
    g = (L, gb, H-gt)
    f = (0, W-ff, fb)
    num, seq = shortest(L, W, H, g, f)
    ex = exact_candidates(L, W, H, gb, gt, ff, fb)
    mn = min(ex.values(), key=lambda e: float(e))
    print(f"{label}: numeric shortest = {num:.9f} via {seq}")
    print(f"  unfolding candidates: " + ", ".join(f"{k}={sp.simplify(v)}" for k, v in ex.items()))
    print(f"  exact minimum = {sp.simplify(mn)} = {float(mn):.9f}; agree = {abs(float(mn)-num) < 1e-6}")
    return mn, num

orig, _ = run("ORIGINAL", 12, 10, 8, 1, 1, 1, 1)
assert sp.simplify(orig - 2*sp.sqrt(113)) == 0, orig
print("Original reproduces 2*sqrt(113):", True)
var, _ = run("VARIANT", 15, 12, 9, 1, 1, 1, 1)
assert sp.simplify(var - 5*sp.sqrt(26)) == 0
print("VARIANT ANSWER:", sp.simplify(var))
