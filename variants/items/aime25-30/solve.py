"""aime25-30 variant: f(x)=(x-a)(x-b)(x-c)(x-k)/x on x>0 attains its minimum at exactly two points.
Exact method: min attained twice  <=>  P(x) - m x = (x^2 - s x + t)^2 with 0 < roots of the quadratic.
Independent numeric check: for each k, find all local minima via roots of P'(x)x - P(x) and compare
the two lowest; scan k to find every k where they tie."""
import itertools, numpy as np, sympy as sp
from scipy.optimize import brentq

k = sp.symbols('k')

def exact(a, b, c):
    r = [a, b, c, k]
    e1 = sum(r); e2 = sum(x*y for x, y in itertools.combinations(r, 2)); e4 = a*b*c*k
    S = e1/2; T = (e2 - S**2)/2
    out = []
    for kv in sp.solve(sp.Eq(T**2, e4), k):
        if kv.is_real and kv > 0:
            Sv, Tv = S.subs(k, kv), T.subs(k, kv)
            if Tv > 0 and Sv**2 > 4*Tv:
                out.append(sp.nsimplify(kv))
    return sorted(out)

def gap(a, b, c, kv):
    # local minima of f: zeros of x P'(x) - P(x) = 3x^4 - 2 e1 x^3 + e2 x^2 - e4
    P = np.poly([a, b, c, kv])
    num = np.polysub(np.polymul([1, 0], np.polyder(P)), P)
    xs = sorted(z.real for z in np.roots(num) if abs(z.imag) < 1e-9 and z.real > 0)
    f = lambda x: np.polyval(P, x)/x
    d2 = lambda x: np.polyval(np.polyder(num), x)  # sign of f'' at critical points ~ sign of num'
    mins = sorted(f(x) for x in xs if d2(x) > 0)
    if len(mins) < 2: return None
    return (mins[1] - mins[0])

def numeric(a, b, c, kmax=1000):
    # two lowest minima tie <=> h(k)= m1(k)-m2(k) changes sign, where m1,m2 = minima in left/right well
    def h(kv):
        P = np.poly([a, b, c, kv])
        num = np.polysub(np.polymul([1, 0], np.polyder(P)), P)
        xs = sorted(z.real for z in np.roots(num) if abs(z.imag) < 1e-9 and z.real > 0)
        f = lambda x: np.polyval(P, x)/x
        mins = [f(x) for x in xs if np.polyval(np.polyder(num), x) > 0]
        if len(mins) != 2: return np.nan
        return mins[0] - mins[1]
    grid = np.concatenate([np.linspace(0.01, 5, 500), np.linspace(5, kmax, 20000)])
    vals = [h(g) for g in grid]
    found = []
    for i in range(len(grid)-1):
        u, v = vals[i], vals[i+1]
        if np.isfinite(u) and np.isfinite(v) and u*v < 0:
            found.append(brentq(h, grid[i], grid[i+1], xtol=1e-12))
    return found

for label, (a, b, c), expected in [("original", (18, 72, 98), 240), ("variant", (8, 50, 72), None)]:
    ex = exact(a, b, c)
    nu = numeric(a, b, c)
    print(label, (a, b, c), "exact k:", ex, "sum:", sum(ex), "| numeric k:", [round(x, 6) for x in nu], "sum:", round(sum(nu), 6))
    assert len(ex) == 3 and len(nu) == 3 and all(abs(float(e) - n) < 1e-5 for e, n in zip(ex, nu))
    if expected is not None:
        assert sum(ex) == expected
        print("original check OK:", sum(ex))
