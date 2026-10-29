"""hmmt2024-30 variant check.
Method: the angle conditions say AB is tangent to circle (PAD) at A and to circle (PBC) at B,
CD likewise at D and C. So AB, CD are the common tangents, ABCD is an isosceles trapezoid
(AD || BC) and P lies on the radical axis = midline. Coordinates: A(-u,h), B(-v,-h), C(v,-h),
D(u,h), P(p,0) with p^2 = uv - h^2, which gives PA^2=u(s+2p), PB^2=v(s+2p), PC^2=v(s-2p).
Independent check: a generic numeric solver (no trapezoid assumption) over positions of
B, C, D around P, enforcing the four angle equalities, convexity and P inside."""
import numpy as np, sympy as sp
from scipy.optimize import fsolve

def closed_form(a, b, c):
    a, b, c = map(sp.Integer, (a, b, c))
    u, v = (a / b) ** 2, sp.Integer(1)
    s = u + v
    t2 = (b / c) ** 2
    p = s * (t2 - 1) / (2 * (t2 + 1))
    h2 = u * v - p ** 2
    assert h2 > 0
    k = a / sp.sqrt(u * (s + 2 * p))
    AB = sp.sqrt((v - u) ** 2 + 4 * h2)
    return sp.radsimp(sp.nsimplify(k * (2 * s + 2 * AB)))

def ang(X, Y, Z):
    p, q = X - Y, Z - Y
    return np.arccos(np.clip(p @ q / np.linalg.norm(p) / np.linalg.norm(q), -1, 1))

def numeric(a, b, c, starts=400):
    f = lambda r, t: r * np.array([np.cos(t), np.sin(t)])
    def pts(x):
        t1, t2, t3, d = x
        return np.zeros(2), f(a, 0), f(b, t1), f(c, t1 + t2), f(d, t1 + t2 + t3)
    def eqs(x):
        P, A, B, C, D = pts(x)
        return [ang(P, A, B) - ang(P, D, A), ang(P, A, D) - ang(P, D, C),
                ang(P, B, A) - ang(P, C, B), ang(P, B, C) - ang(P, C, D)]
    rng = np.random.default_rng(0); found = set()
    for _ in range(starts):
        x0 = [*rng.uniform(0.3, 2.8, 3), rng.uniform(0.5, 3 * c)]
        x, _, ier, _ = fsolve(eqs, x0, full_output=True)
        t1, t2, t3, d = x
        if ier != 1 or max(map(abs, eqs(x))) > 1e-10: continue
        if d <= 1e-6 or min(t1, t2, t3) <= 1e-4 or max(t1, t2, t3, 2*np.pi - t1 - t2 - t3) >= np.pi - 1e-4: continue  # reject degenerate (collinear) configurations
        P, A, B, C, D = pts(x); Q = [A, B, C, D]
        cr = [np.cross(Q[(i+1) % 4] - Q[i], Q[(i+2) % 4] - Q[(i+1) % 4]) for i in range(4)]
        if not all(z > 0 for z in cr): continue  # convex, counterclockwise, P inside (angles at P < pi)
        found.add(round(sum(np.linalg.norm(Q[(i+1) % 4] - Q[i]) for i in range(4)), 7))
    return found

for name, data, expected in [("original", (4, 5, 10), 9 * sp.sqrt(410) / 5),
                             ("variant", (3, 5, 10), None)]:
    cf = closed_form(*data); num = numeric(*data)
    print(name, data, "closed form:", cf, "=", float(cf), "| numeric perimeters:", num)
    assert len(num) == 1 and abs(next(iter(num)) - float(cf)) < 1e-6
    if expected is not None:
        assert sp.simplify(cf - expected) == 0
        print("original answer reproduced:", expected)
