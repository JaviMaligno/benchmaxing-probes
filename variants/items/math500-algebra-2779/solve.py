import sympy as sp
def coeffs(p, q, n):
    e = sp.expand((sp.sqrt(p)+sp.sqrt(q))**n)
    a, b, c = sp.symbols('a b c')
    basis = [sp.sqrt(p), sp.sqrt(q), sp.sqrt(p*q)]
    # solve e == a*sqrt(p)+b*sqrt(q)+c*sqrt(pq) via exact coefficient extraction
    sol = [sp.nsimplify(e.coeff(x)) for x in basis]
    rest = sp.simplify(e - sum(s*x for s, x in zip(sol, basis)))
    assert rest == 0, rest
    # independent numeric check
    assert abs(float(e) - float(sum(s*x for s, x in zip(sol, basis)))) < 1e-9
    return sol
o = coeffs(2, 3, 3); print("original a,b,c =", o, "sum =", sum(o)); assert sum(o) == 20
v = coeffs(2, 5, 3); print("variant a,b,c =", v, "sum =", sum(v))
