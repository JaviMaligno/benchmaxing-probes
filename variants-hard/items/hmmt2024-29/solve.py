# Independent numeric solve by coordinates + closed form check.
# A=(0,0), C=(b,0), B=(c cosA, c sinA). X on AB with angle BXC=60, P on CX with BP perp AC.
import math, sympy as sp

def numeric(c, b, d):
    sols = []
    N = 200000
    def geom(A):
        B = (c*math.cos(A), c*math.sin(A)); C = (b, 0.0)
        # find X = t*B on AB with angle BXC = 60 deg (t in (0,1))
        def ang(t):
            X = (t*B[0], t*B[1])
            u = (B[0]-X[0], B[1]-X[1]); v = (C[0]-X[0], C[1]-X[1])
            return math.acos((u[0]*v[0]+u[1]*v[1])/math.hypot(*u)/math.hypot(*v))
        lo, hi = 1e-9, 1-1e-9
        f = lambda t: ang(t) - math.pi/3
        if f(lo)*f(hi) > 0: return None
        for _ in range(100):
            m = (lo+hi)/2
            if f(lo)*f(m) <= 0: hi = m
            else: lo = m
        X = (lo*B[0], lo*B[1])
        # P on CX with x = B.x
        if abs(X[0]-C[0]) < 1e-12: return None
        s = (B[0]-C[0])/(X[0]-C[0])
        if not (0 <= s <= 1): return None
        P = (C[0]+s*(X[0]-C[0]), C[1]+s*(X[1]-C[1]))
        return B[1]-P[1], math.hypot(P[0]-C[0], P[1]-C[1])
    prev = None
    for i in range(1, N):
        A = math.pi*i/N
        g = geom(A)
        if g is None: prev = None; continue
        val = g[0]-d
        if prev is not None and prev[1]*val <= 0:
            lo, hi = prev[0], A
            for _ in range(80):
                m = (lo+hi)/2; gm = geom(m)
                if gm is None: break
                if (geom(lo)[0]-d)*(gm[0]-d) <= 0: hi = m
                else: lo = m
            sols.append(round(geom(lo)[1], 9))
        prev = (A, val)
    return sorted(set(sols))

def closed(c, b, d):
    x = sp.symbols('x', positive=True)
    return [s for s in sp.solve(x**2 + c*x + c**2 - b**2 - d**2, x)]

for name, (c, b, d) in [("original", (6, 7, 4)), ("variant", (6, 8, 3))]:
    cf = closed(c, b, d)
    print(name, "numeric CP:", numeric(c, b, d), "closed:", cf, [float(v) for v in cf])
print("original matches sqrt(38)-3:", float(sp.sqrt(38)-3))
