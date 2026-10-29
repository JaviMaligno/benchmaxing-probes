import sympy as sp
x = sp.symbols('x')

def solve(coef, k_terms=4):
    lhs = sum(sp.Rational(k)/(x**2 - k) for k in range(1, k_terms+1))
    rhs = coef*x - k_terms
    num, den = sp.fraction(sp.together(lhs - rhs))
    P = sp.Poly(sp.expand(num), x)
    # no root of P may be a pole
    D = sp.Poly(sp.expand(den), x)
    assert sp.gcd(P, D).degree() == 0
    # exact Vieta sum
    c = P.all_coeffs()
    vieta = -sp.Rational(c[1], c[0])
    # independent numeric check: sum numeric roots
    roots = sp.Poly(P, x).nroots(n=30, maxsteps=200)
    numsum = sum(roots)
    assert abs(sp.N(numsum) - sp.N(vieta)) < 1e-15, (numsum, vieta)
    # distinct roots (no multiplicity issues)
    assert sp.gcd(P, P.diff(x)).degree() == 0
    return vieta, P.degree()

orig, d0 = solve(2010)
print("original:", orig, "degree", d0)
assert orig == sp.Rational(2, 1005)
var, d1 = solve(2022)
print("variant:", var, "degree", d1, "=", float(var))
