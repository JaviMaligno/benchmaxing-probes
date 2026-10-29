# Min distance from origin to y = (1/sqrt(k)) (x^2 - c); answer sqrt(a)/b in simplest form -> a+b
import sympy as sp

def solve(k, c):
    u = sp.symbols('u', nonnegative=True)  # u = x^2
    d2 = u + sp.Rational(1, k) * (u - c)**2
    crit = [r for r in sp.solve(sp.diff(d2, u), u) if r >= 0] + [sp.Integer(0)]
    m = min(sp.nsimplify(d2.subs(u, r)) for r in crit)
    d = sp.sqrt(m)
    # write d = sqrt(a)/b with a squarefree: d^2 = p/q -> sqrt(p*q)/q, then simplify
    p, q = sp.fraction(sp.Rational(m))
    n = p * q
    # extract square factor of n
    sq = 1
    for prime, e in sp.factorint(n).items():
        sq *= prime ** (e // 2)
    a = n // sq**2
    b = sp.Rational(q, sq)
    assert b.q == 1, b
    assert sp.simplify(sp.sqrt(a) / b - d) == 0
    # independent numeric check by brute-force grid
    import math
    best = min(math.hypot(x, (x*x - c) / math.sqrt(k)) for x in [i / 10000 for i in range(-60000, 60001)])
    assert abs(best - float(d)) < 1e-6, (best, float(d))
    return d, a, int(b), a + int(b)

orig = solve(2, 3)
print("original:", orig)
assert orig[3] == 12
var = solve(3, 5)
print("variant:", var)
