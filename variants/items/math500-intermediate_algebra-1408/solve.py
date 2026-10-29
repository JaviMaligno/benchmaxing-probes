import sympy as sp
z = sp.symbols('z')

def solve(s, n):
    # all roots of z^2 - s z + 1 = 0; compute z^n + z^-n exactly via minimal reduction, and numerically
    roots = sp.solve(sp.Eq(z**2 - s*z + 1, 0), z)
    vals = set()
    for r in roots:
        exact = sp.nsimplify(sp.N(r**n + r**(-n), 50), [sp.sqrt(5)], tolerance=1e-30)
        vals.add(exact)
    # independent check: Chebyshev-like recurrence t_k = s t_{k-1} - t_{k-2}
    t0, t1 = sp.Integer(2), s
    for _ in range(n - 1):
        t0, t1 = t1, sp.expand(s*t1 - t0)
    return vals, sp.nsimplify(sp.simplify(t1))

orig = solve((1 + sp.sqrt(5))/2, 85)
print("original:", orig)
assert orig[0] == {-2} and orig[1] == -2

var = solve((sp.sqrt(5) - 1)/2, 95)
print("variant:", var)
assert len(var[0]) == 1 and list(var[0])[0] == var[1]
print("ANSWER:", var[1])
