import sympy as sp
a = sp.symbols('a')

def solve(f, n, k):
    """All a1 with a3 = a1 (sequence defined), return set of (a_n)^k."""
    a2 = sp.simplify(f(a)); a3 = sp.simplify(f(a2))
    num, den = sp.fraction(sp.together(a3 - a))
    vals = set()
    for r in sp.roots(sp.Poly(num, a)).keys():
        # check sequence defined up to a_n
        x = r; ok = True; seq = [x]
        for _ in range(n - 1):
            d = sp.simplify(sp.denom(sp.together(f(sp.Symbol('t')))).subs(sp.Symbol('t'), x))
            if d == 0: ok = False; break
            x = sp.nsimplify(sp.simplify(f(x)))
            seq.append(x)
        if ok and sp.simplify(seq[2] - seq[0]) == 0:
            vals.add(sp.nsimplify(sp.simplify(sp.expand(seq[n-1]**k))))
        # numeric check
        z = complex(sp.N(r)); zs = [z]
        for _ in range(n - 1): zs.append(complex(sp.N(f(zs[-1])) ) if False else None) if False else None
    return vals

def numeric(fnum, r, n, k):
    z = complex(r)
    for _ in range(n - 1): z = fnum(z)
    return z**k

orig = solve(lambda x: 1/(1 - x), 9, 9)
print("original:", orig)
var = solve(lambda x: -1/(1 + x), 9, 9)
print("variant:", var)
for r in sp.Poly(sp.symbols('a')**2 + sp.symbols('a') + 1).nroots():
    print("numeric variant root", r, numeric(lambda z: -1/(1 + z), complex(r), 9, 9))
assert orig == {-1} and var == {1}
