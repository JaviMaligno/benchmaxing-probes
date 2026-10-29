# Count monic quadratics x^2+ax+b whose root set R satisfies f(R) subset of R.
import sympy as sp
r, s = sp.symbols('r s')

def count(f):
    quads = set()
    targets = [r, s]
    for tr in targets:
        for ts in targets:
            sols = sp.solve([sp.expand(f(r) - tr), sp.expand(f(s) - ts)], [r, s], dict=True)
            for so in sols:
                rv, sv = sp.nsimplify(so[r]), sp.nsimplify(so[s])
                a = sp.simplify(-(rv + sv)); b = sp.simplify(rv * sv)
                quads.add((a, b))
    # independent numeric check: roots of each quadratic map into root set
    for a, b in quads:
        rts = sp.Poly(sp.Symbol('x')**2 + a*sp.Symbol('x') + b).all_roots()
        for c in rts:
            assert any(abs(complex(sp.N(f(c) - d))) < 1e-9 for d in rts)
    return sorted(quads, key=str)

orig = count(lambda c: c**2 - 2)
print("original:", len(orig), orig)
assert len(orig) == 6
var = count(lambda c: c**2 - 4*c + 6)
print("variant:", len(var), var)
