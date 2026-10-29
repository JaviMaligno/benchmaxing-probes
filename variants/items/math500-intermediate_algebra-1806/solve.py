import sympy as sp, math
x = sp.symbols('x', real=True)

def exact_max(k):
    # |z|=1, z=x+iy: |1+z| = sqrt(2+2x), |1-z+z^2| = |2x-1|
    f1 = sp.sqrt(2+2*x) + k*(1-2*x)   # x <= 1/2
    f2 = sp.sqrt(2+2*x) + k*(2*x-1)   # x >= 1/2
    cands = []
    for f, lo, hi in [(f1, -1, sp.Rational(1,2)), (f2, sp.Rational(1,2), 1)]:
        pts = [sp.Integer(lo), sp.Integer(hi) if hi==1 else hi]
        for s in sp.solve(sp.diff(f, x), x):
            if s.is_real and lo <= s <= hi: pts.append(s)
        cands += [sp.nsimplify(sp.simplify(f.subs(x, p))) for p in pts]
    return max(cands, key=lambda v: float(v))

def numeric_max(k, N=400000):
    best = 0
    for i in range(N):
        t = 2*math.pi*i/N
        z = complex(math.cos(t), math.sin(t))
        best = max(best, abs(1+z) + abs(k*(1 - z + z*z)))
    return best

orig = exact_max(1); print("original:", orig, numeric_max(1))
assert orig == sp.Rational(13,4)
var = exact_max(2); print("variant:", var, numeric_max(2))
assert abs(float(var) - numeric_max(2)) < 1e-6
