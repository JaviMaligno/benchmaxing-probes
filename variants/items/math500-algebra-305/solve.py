import sympy as sp
x = sp.symbols('x')

def total(f):
    num, den = sp.fraction(sp.together(f))
    vas = [r for r in sp.solve(den, x) if sp.simplify(num.subs(x, r)) != 0]
    assert len(vas) == 2
    c = sp.limit(f, x, sp.oo)
    assert c == sp.limit(f, x, -sp.oo)
    # independent numeric check of horizontal asymptote
    assert abs(float(f.subs(x, 10**8)) - float(c)) < 1e-6
    return sum(vas) + c

orig = total(2*x/(x**2 - 5*x - 14))
print("original:", orig)
assert orig == 5
var = total(3*x/(x**2 - 3*x - 40))
print("variant:", var)
