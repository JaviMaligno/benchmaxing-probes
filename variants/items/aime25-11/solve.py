import sympy as sp
from fractions import Fraction
import math

y = sp.symbols('y')

def f_num(x):
    m = x - 4*math.floor((x+1)/4)
    return m if m < 1 else 2 - m

def intersections(k):
    """Exact roots of x = k*y^2 against the period-4 sawtooth."""
    pts = []
    xmax = k  # |y|<=1 so x<=k
    for n in range(0, xmax//4 + 2):
        # rising piece: x in [4n-1, 4n+1), f = x - 4n
        for r in sp.solve(sp.Eq(k*y**2 - 4*n, y), y):
            x = k*r**2
            if sp.simplify(x - (4*n-1)) >= 0 and sp.simplify(x - (4*n+1)) < 0:
                pts.append(sp.nsimplify(r))
        # falling piece: x in [4n+1, 4n+3), f = 4n+2 - x
        for r in sp.solve(sp.Eq(4*n+2 - k*y**2, y), y):
            x = k*r**2
            if sp.simplify(x - (4*n+1)) >= 0 and sp.simplify(x - (4*n+3)) < 0:
                pts.append(sp.nsimplify(r))
    pts = list({sp.simplify(p) for p in pts})
    # independent numeric check of each point
    for p in pts:
        yv = float(p); xv = k*yv*yv
        assert abs(f_num(xv) - yv) < 1e-9, (k, p)
    return pts

def numeric_count(k, N=1_000_000):
    # independent brute force: roots of g(y)=f(k y^2)-y on a fine grid of [-1,1]
    cnt = 0; s = 0.0
    ys = [-1 + 2*i/N for i in range(N+1)]
    gs = [f_num(k*v*v) - v for v in ys]
    for i in range(N+1):
        if gs[i] == 0:
            cnt += 1; s += ys[i]
        elif i > 0 and gs[i-1] != 0 and (gs[i-1] < 0) != (gs[i] < 0):
            # linear interpolation of the root inside the cell
            t = gs[i-1] / (gs[i-1] - gs[i])
            cnt += 1; s += ys[i-1] + t*(ys[i]-ys[i-1])
    return cnt, s

def answer(k):
    pts = intersections(k)
    S = sp.nsimplify(sp.radsimp(sp.simplify(sum(pts))))
    # write S = (a + b sqrt c)/d
    S = sp.together(sp.radsimp(S))
    num, den = sp.fraction(S)
    num = sp.expand(num)
    a = sp.Integer(0); b = sp.Integer(0); c = None
    for term in sp.Add.make_args(num):
        if term.is_Rational: a += term
        else:
            coeff, rad = term.as_coeff_Mul()
            b += coeff; c = rad**2
    d = den
    g = sp.gcd(sp.gcd(a, b), d)
    a, b, d = a/g, b/g, d/g
    return len(pts), S, (a, b, c, d), a + b + c + d

for k, label in [(34, "ORIGINAL"), (66, "VARIANT")]:
    n, S, abcd, ans = answer(k)
    cnt, s = numeric_count(k)
    print(f"{label} k={k}: #points={n} (numeric sign changes {cnt}), sum={S} ~ {float(S):.10f} (numeric {s:.6f})")
    print(f"   (a,b,c,d)={abcd}, a+b+c+d={ans}")

assert answer(34)[3] == 259, "original answer not reproduced"
print("original check: 259 reproduced")
