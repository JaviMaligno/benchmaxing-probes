# hmmt2024-25 variant check. Coordinates: A=(0,0), B=(AB,0), D=(0,DA), C=(AB,BC).
# Center O=(AB,t) on line BC; |OA| = dist(O, line CD), tangency point T on segment CD.
# CT = sqrt(|CO|^2 - r^2) (tangent length from C). Independent numeric check: bisection + direct T.
import sympy as sp, math

def exact(da, ab, bc):
    t = sp.symbols('t', real=True)
    A = sp.Matrix([0, 0]); D = sp.Matrix([0, da]); C = sp.Matrix([ab, bc]); O = sp.Matrix([ab, t])
    r2 = O.dot(O); d = C - D; n = sp.Matrix([-d[1], d[0]])
    dist2 = ((O - D).dot(n))**2 / n.dot(n)
    out = []
    for tv in sp.solve(sp.Eq(r2, dist2), t):
        Ov = O.subs(t, tv)
        s = sp.simplify((Ov - D).dot(d) / d.dot(d))
        if 0 <= s <= 1:
            out.append(sp.radsimp(sp.sqrtdenest(sp.simplify(sp.sqrt((C - Ov).dot(C - Ov) - r2.subs(t, tv))))))
    assert len(out) == 1
    return out[0]

def numeric(da, ab, bc):
    # scan t, find roots of f(t)=|OA|-dist(O,CD), keep those with foot on segment, compute |CT| directly
    dx, dy = ab, bc - da; L = math.hypot(dx, dy)
    def f(t): return math.hypot(ab, t) - abs((ab - 0) * dy - (t - da) * dx) / L
    sols = []; N = 200000; lo, hi = -100.0, 100.0
    prev = f(lo)
    for i in range(1, N + 1):
        x = lo + (hi - lo) * i / N; v = f(x)
        if prev * v <= 0:
            a, b = x - (hi - lo) / N, x
            for _ in range(200):
                m = (a + b) / 2
                if f(a) * f(m) <= 0: b = m
                else: a = m
            tv = (a + b) / 2
            s = ((ab - 0) * dx + (tv - da) * dy) / L**2
            if 0 <= s <= 1:
                T = (s * dx, da + s * dy)
                sols.append(math.hypot(ab - T[0], bc - T[1]))
        prev = v
    return sols

orig = exact(2, 3, 8)
print("original exact:", orig, "numeric:", numeric(2, 3, 8))
assert sp.simplify(orig - (4*sp.sqrt(5) - sp.sqrt(7))) == 0
print("original check OK (4*sqrt(5)-sqrt(7))")
var = exact(3, 4, 9)
print("variant exact:", var, "=", float(var), "numeric:", numeric(3, 4, 9))
