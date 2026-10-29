import sympy as sp
from mpmath import mp, polyroots
mp.dps = 50
x = sp.symbols('x')

def exact(a, n):
    # 1/r = a + z, z^n = -1; sum over conjugate pairs of |1/r|^2 = (n*a^2 + n)/2
    return sp.Rational(n * a**2 + n, 2)

def numeric(a, n):
    p = sp.Poly(x**n + (a*x - 1)**n, x)
    roots = polyroots([int(c) for c in p.all_coeffs()], maxsteps=500, extraprec=200)
    assert all(abs(r.imag) > 1e-20 for r in roots)  # all nonreal
    upper = [r for r in roots if r.imag > 0]
    assert len(upper) == n // 2
    return sum(1/(r*r.conjugate()) for r in upper).real

for a, n, label in [(13, 10, 'original'), (11, 10, 'variant')]:
    e = exact(a, n); v = numeric(a, n)
    print(label, 'a=%d n=%d exact=%s numeric=%s' % (a, n, e, mp.nstr(v, 30)))
    assert abs(v - e) < 1e-25
assert exact(13, 10) == 850
print('original check OK (850); variant answer =', exact(11, 10))
