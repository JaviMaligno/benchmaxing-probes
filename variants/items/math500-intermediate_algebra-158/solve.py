from fractions import Fraction
from sympy import symbols, Rational, solve, diff, log, simplify
import random

def amgm_max(exps, S):
    # AM-GM: max of prod x_i^{e_i} with sum x_i = S is at x_i = e_i*S/sum(e)
    E = sum(exps)
    xs = [Fraction(e * S, E) for e in exps]
    val = Fraction(1)
    for x, e in zip(xs, exps):
        val *= x ** e
    return xs, val

def numeric_check(exps, S, trials=200000):
    best = 0.0
    for _ in range(trials):
        w = [random.random() for _ in exps]
        t = sum(w)
        xs = [S * wi / t for wi in w]
        v = 1.0
        for x, e in zip(xs, exps):
            v *= x ** e
        best = max(best, v)
    return best

random.seed(0)
# Original: a+b+c+d=10, max a b^2 c^3 d^4
xs, v = amgm_max([1, 2, 3, 4], 10)
print("original:", xs, v, "numeric best", numeric_check([1, 2, 3, 4], 10))
assert v == 27648

# Variant: p+q+r+s=16, max p q^2 r^2 s^3
xs, v = amgm_max([1, 2, 2, 3], 16)
print("variant:", xs, v, "numeric best", numeric_check([1, 2, 2, 3], 16))
# Lagrange check via sympy
p, q, r, s = symbols('p q r s', positive=True)
f = log(p) + 2*log(q) + 2*log(r) + 3*log(s)
lam = symbols('lam')
sol = solve([diff(f, x) - lam for x in (p, q, r, s)] + [p+q+r+s-16], [p, q, r, s, lam], dict=True)
print("lagrange:", sol, [ (d[p]*d[q]**2*d[r]**2*d[s]**3) for d in sol])
print("ANSWER", v)
