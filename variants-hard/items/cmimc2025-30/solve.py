"""Verification for cmimc2025-30 variant.

Pipeline (same logic for original and variant), right angle at B:
  B=(0,0), C=(a,0), A=(0,c).
  1. Solve the given equation in theta = angle QJC (x=cos, y=sin) on the range
     of theta reachable by P on the open arc BC (not containing A).
  2. Recover P from theta (brute-force root find of the actual angle QJC).
  3. With P fixed, brute-force scan all directions of line l through B and
     find those where B, J, U, M are concyclic; discard degenerate roots
     (U coinciding with J, or I/U at infinity).
  4. BL = second intersection of l with the circumcircle.
Original data (a=8, c=6, given equation) must give 9.94.
"""
import numpy as np
from scipy.optimize import brentq


def pipeline(a, c, eq):
    A = np.array([0.0, c]); B = np.array([0.0, 0.0]); C = np.array([float(a), 0.0])
    O = (A + C) / 2; R = np.hypot(a, c) / 2

    def foot(P, X, Y):
        d = Y - X
        return X + np.dot(P - X, d) / np.dot(d, d) * d

    def inter(P1, d1, P2, d2):
        s = np.linalg.solve(np.array([d1, -d2]).T, P2 - P1)
        return P1 + s[0] * d1

    def det4(pts):
        return np.linalg.det(np.array([[p @ p, p[0], p[1], 1] for p in pts]))

    pb = np.arctan2(-O[1], -O[0]); pc = np.arctan2(-O[1], O[0])

    def geo(phi):
        P = O + R * np.array([np.cos(phi), np.sin(phi)])
        J = foot(P, B, C); Q = foot(P, A, C)
        v1, v2 = Q - J, C - J
        th = np.arccos(np.dot(v1, v2) / np.linalg.norm(v1) / np.linalg.norm(v2))
        return P, J, Q, th

    # 1. theta range over the arc, and roots of the equation in that range
    phis = np.linspace(pb + 1e-6, pc - 1e-6, 20001)
    ths = np.array([geo(p)[3] for p in phis])
    lo, hi = ths.min(), ths.max()
    g = lambda t: eq(np.cos(t), np.sin(t))
    ts = np.linspace(lo + 1e-9, hi - 1e-9, 200001); gv = g(ts)
    roots = [brentq(g, ts[i], ts[i + 1]) for i in range(len(ts) - 1)
             if np.sign(gv[i]) != np.sign(gv[i + 1])]
    results = []
    for th0 in roots:
        # 2. P with that theta
        hv = ths - th0
        idx = [i for i in range(len(phis) - 1) if np.sign(hv[i]) != np.sign(hv[i + 1])]
        for i in idx:
            phi = brentq(lambda f: geo(f)[3] - th0, phis[i], phis[i + 1])
            P, J, Q, _ = geo(phi); M = (B + Q) / 2

            def F(al):
                d = np.array([np.cos(al), np.sin(al)])
                I = inter(B, d, C, M - C); U = inter(A, I - A, J, Q - J)
                return det4([B, J, U, M])
            als = np.linspace(1e-3, np.pi - 1e-3, 20001); fv = [F(x) for x in als]
            for k in range(len(als) - 1):
                if np.sign(fv[k]) != np.sign(fv[k + 1]):
                    al = brentq(F, als[k], als[k + 1])
                    if abs(F(al)) > 1e-6:      # sign change through a pole
                        continue
                    d = np.array([np.cos(al), np.sin(al)])
                    I = inter(B, d, C, M - C); U = inter(A, I - A, J, Q - J)
                    if np.linalg.norm(U - J) < 1e-6 or np.linalg.norm(U - M) < 1e-6:
                        continue  # degenerate (points not distinct)
                    BL = -2 * np.dot(d, B - O)
                    results.append((th0, np.cos(th0), np.sin(th0), al, BL))
    return results


def orig_eq(x, y):
    return 768 * x * y - (16 - 8 * x**2 + 6 * x * y) * (
        x**2 * y**2 * (8 * x - 6 * y) ** 2 + (8 * x - 8 * x * y**2 + 6 * y**3) ** 2)


def var_eq(x, y):
    return 169 * x * y**4 + 120 * y**3 - 144 * x


print("ORIGINAL (AB=6, BC=8, AC=10):")
ro = pipeline(8, 6, orig_eq)
for r in ro:
    print("  theta=%.6f x=%.5f y=%.5f l-angle=%.6f BL=%.6f -> %.2f" % (*r, round(r[4], 2)))
assert len(ro) == 1 and round(ro[0][4], 2) == 9.94, ro
print("  original check OK (9.94); closed form 8x+6y =", round(8 * 0.72951 + 6 * 0.68400, 4))

print("VARIANT (AB=5, BC=12, AC=13):")
rv = pipeline(12, 5, var_eq)
for r in rv:
    print("  theta=%.6f x=%.5f y=%.5f l-angle=%.6f BL=%.6f -> %.2f" % (*r, round(r[4], 2)))
assert len(rv) == 1, rv
print("  closed form 12x+5y =", round(12 * rv[0][1] + 5 * rv[0][2], 6))
print("VARIANT ANSWER:", "%.2f" % rv[0][4])
