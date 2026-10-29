import sympy as sp

def solve(p, q, x1, x0, maxdeg=6):
    a = sp.sqrt(p) + sp.sqrt(q)
    b = sp.sqrt(p) - sp.sqrt(q)
    for n in range(1, maxdeg + 1):
        cs = sp.symbols(f"c0:{n}")  # c0..c_{n-1}, monic leading
        x = sp.Symbol("x")
        P = x**n + sum(cs[i] * x**i for i in range(n))
        expr = sp.expand(P.subs(x, a) - P.subs(x, b))
        # separate into rational-linear coefficients of radical basis elements
        d = sp.collect(expr, [sp.sqrt(p), sp.sqrt(q), sp.sqrt(p * q)], evaluate=False)
        eqs = [sp.expand(v) for v in d.values()]
        sol = sp.solve(eqs, cs, dict=True)
        if not sol:
            continue
        s = sol[0]
        Ps = sp.expand(P.subs(s))
        free = Ps.free_symbols - {x}
        # integer coefficients must be achievable: check coefficients (besides free constant) are integers
        poly = sp.Poly(Ps, x)
        diff = sp.simplify(Ps.subs(x, x1) - Ps.subs(x, x0))
        assert not (diff.free_symbols), diff
        # independent numeric check with a sample integer for free symbols
        Pn = Ps.subs({f: 7 for f in free})
        assert abs(sp.N(Pn.subs(x, a) - Pn.subs(x, b), 50)) < 1e-40
        return n, Ps, diff
    return None

print("original:", solve(3, 2, 10, 0))
o = solve(3, 2, 10, 0)
assert o[2] == 890, o
print("variant:", solve(5, 3, 6, 1))
