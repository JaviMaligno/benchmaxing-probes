# aime25-27 variant check. Fan from A1: r_i = A1A_i (i=2..N), r_i r_{i+1} = 2*Area/sin,
# so radii alternate a,b; each outer side^2 = s^2 - 2ab(1+cos), s=a+b.
# Perimeter: r_2 + r_N + (N-2)*side = P, with r_2 + r_N = a+b when N is odd.
import sympy as sp, math

def solve(N, area, cos, P):
    cos = sp.Rational(cos); sin = sp.sqrt(1 - cos**2)
    ab = 2*sp.Rational(area)/sin
    k = N - 2
    s = sp.symbols('s', positive=True)
    # square: k^2 (s^2 - 2ab(1+cos)) = (P - s)^2
    cands = sp.solve(sp.Eq(k**2*(s**2 - 2*ab*(1+cos)), (P - s)**2), s)
    good = [sp.radsimp(c) for c in cands if c.is_real and c > 0 and c < P and c**2 >= 4*ab]
    assert len(good) == 1, good
    sv = good[0]
    # numeric construction + independent checks
    a = float((sv + sp.sqrt(sv**2 - 4*ab))/2); b = float(ab)/a
    th = math.acos(float(cos))
    pts = [(0.0, 0.0)] + [((a if j % 2 == 0 else b)*math.cos(j*th), (a if j % 2 == 0 else b)*math.sin(j*th)) for j in range(N-1)]
    per = sum(math.dist(pts[i], pts[(i+1) % N]) for i in range(N))
    assert abs(per - P) < 1e-9, per
    for i in range(1, N-1):
        (x1, y1), (x2, y2) = pts[i], pts[i+1]
        assert abs(abs(x1*y2 - x2*y1)/2 - float(area)) < 1e-9
        assert abs((x1*x2 + y1*y2)/(math.hypot(x1, y1)*math.hypot(x2, y2)) - float(cos)) < 1e-9
    assert (N-2)*th < 2*math.pi  # fan does not wrap: simple polygon
    assert (N-2)*th > math.pi    # reflex angle at A1: non-convex
    def inter(p, q, r, t):
        def o(a, b, c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        return o(p, q, r)*o(p, q, t) < 0 and o(r, t, p)*o(r, t, q) < 0
    E = [(pts[i], pts[(i+1) % N]) for i in range(N)]
    for i in range(N):
        for j in range(i+2, N):
            if i == 0 and j == N-1: continue
            assert not inter(*E[i], *E[j]), (i, j)
    return sv

def mnpq(expr):
    # expr = (m sqrt n - p)/q
    expr = sp.nsimplify(expr)
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    rat = num.as_coeff_add()[0]
    rad = num - rat
    m, sq = rad.as_coeff_Mul()
    n = sq**2
    p = -rat; q = den
    g = sp.gcd(sp.gcd(m, p), q); m, p, q = m/g, p/g, q/g
    assert sp.simplify((m*sp.sqrt(n) - p)/q - expr) == 0 and m > 0 and p > 0 and q > 0
    return int(m), int(n), int(p), int(q)

orig = solve(11, 1, sp.Rational(12, 13), 20)
m, n, p, q = mnpq(orig)
print("original:", orig, (m, n, p, q), "answer", m+n+p+q)
assert m+n+p+q == 19
var = solve(11, 1, sp.Rational(4, 5), 20)
m, n, p, q = mnpq(var)
print("variant:", var, (m, n, p, q), "answer", m+n+p+q)
