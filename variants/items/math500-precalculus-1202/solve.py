import sympy as sp
from mpmath import mp, mpf, acos, pi, findroot
mp.dps = 50
x = sp.symbols('x')

def solve(k1, k2, k3):
    # derive polynomial: sqrt((1-k1^2x^2)(1-k2^2x^2)) = k1k2 x^2 + k3 x, square
    P = sp.expand((1 - k1**2*x**2)*(1 - k2**2*x**2) - (k1*k2*x**2 + k3*x)**2)
    # find actual real roots of the arccos equation numerically (independent check)
    lim = mpf(1)/max(k1, k2, k3)
    f = lambda t: acos(k1*t) + acos(k2*t) + acos(k3*t) - pi
    sols = []
    N = 4000
    for i in range(N):
        a = -lim + 2*lim*i/N; b = -lim + 2*lim*(i+1)/N
        if f(a)*f(b) < 0:
            sols.append(findroot(f, (a, b), solver='bisect'))
    assert len(sols) == 1, sols
    r = sols[0]
    # minimal polynomial of the true root
    roots = [rt for rt in sp.Poly(P, x).nroots(n=40) if abs(sp.im(rt)) < 1e-30]
    assert any(abs(sp.re(rt) - sp.Float(str(r), 40)) < 1e-25 for rt in roots)
    mp_ = None
    for fac, _ in sp.factor_list(P)[1]:
        if abs(sp.N(fac.subs(x, sp.Float(str(r), 50)), 40)) < 1e-25:
            mp_ = sp.Poly(fac, x)
    assert mp_.degree() == 3, mp_   # irreducible cubic => cubics are integer multiples
    c = mp_.all_coeffs()
    g = sp.gcd_list(c)
    c = [ci // g for ci in c]
    return r, mp_, sum(abs(ci) for ci in c)

r, p, s = solve(1, 2, 3)
print("original: root", r, "poly", p.as_expr(), "answer", s)
assert s == 27
r, p, s = solve(1, 2, 4)
print("variant:  root", r, "poly", p.as_expr(), "answer", s)
