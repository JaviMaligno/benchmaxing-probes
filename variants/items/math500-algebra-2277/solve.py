import sympy as sp
x = sp.symbols('x', real=True)

def finv(a, cubic, y):
    sols = set()
    for s in sp.solve(sp.Eq(a - x, y), x):
        if s.is_real and s <= a: sols.add(sp.nsimplify(s))
    for s in sp.solve(sp.Eq(cubic, y), x):
        if s.is_real and s > a: sols.add(sp.nsimplify(s))
    assert len(sols) == 1, sols
    return sols.pop()

def check_bijective(a, cubic):
    # cubic piece strictly decreasing on (a, inf) with value at a <= 0; linear piece covers [0, inf)
    d = sp.diff(cubic, x)
    assert all(d.subs(x, a + sp.Rational(k, 10)) < 0 for k in range(1, 400))
    assert cubic.subs(x, a) == 0

def answer(a, cubic, ys):
    check_bijective(a, cubic)
    return sum(finv(a, cubic, y) for y in ys)

orig = answer(3, -x**3 + 2*x**2 + 3*x, [0, 6])
print("original:", orig)
assert orig == 0

var = answer(4, -x**3 + 3*x**2 + 4*x, [0, 12])
print("variant:", var)

# independent numeric check by brute-force scan
import numpy as np
def f(t): return 4 - t if t <= 4 else -t**3 + 3*t**2 + 4*t
xs = np.linspace(-50, 50, 2000001)
def inv(y):
    vals = np.array([abs(f(t) - y) for t in xs[::10]])
    return xs[::10][vals.argmin()]
print("numeric variant:", inv(0) + inv(12))
