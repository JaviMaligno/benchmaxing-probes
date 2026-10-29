import sympy as sp
x = sp.symbols('x', real=True)

def excluded(p, q):
    # denominator |p|+|q| = 0 iff p = 0 and q = 0 (both nonnegative)
    common = set(sp.solve(p, x)) & set(sp.solve(q, x))
    # independent brute-force check over integer/rational grid
    brute = {sp.Rational(n, 4) for n in range(-200, 201)
             if sp.Abs(p.subs(x, sp.Rational(n, 4))) + sp.Abs(q.subs(x, sp.Rational(n, 4))) == 0}
    assert brute == common, (brute, common)
    return sorted(common)

orig = excluded(x**2 + 3*x - 4, x**2 + 9*x + 20)
print("original:", orig)
assert orig == [-4]
var = excluded(x**2 - x - 6, x**2 - 10*x + 21)
print("variant:", var)
assert len(var) == 1
