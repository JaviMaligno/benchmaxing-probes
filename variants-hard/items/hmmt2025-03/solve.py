# a=log2 x, b=log2 y, c=log2 z, k=log2 3. System: a(b+c)=A1+B1 k, b(c+a)=A2+B2 k, c(a+b)=A3+B3 k.
# Solve all real solutions symbolically (sympy), take min of a+b+c, return xyz = 2^(a+b+c) exactly.
import sympy as sp
from fractions import Fraction
import itertools, math

def solve(e):
    k = sp.log(3, 2)
    a, b, c = sp.symbols('a b c', real=True)
    eqs = [a*(b+c) - (e[0][0] + e[0][1]*k),
           b*(c+a) - (e[1][0] + e[1][1]*k),
           c*(a+b) - (e[2][0] + e[2][1]*k)]
    sols = sp.solve(eqs, [a, b, c], dict=True)
    vals = []
    for s in sols:
        if all(sp.im(sp.N(s[v])) == 0 for v in (a, b, c)):
            vals.append(sp.simplify(sp.expand_log(2**(s[a]+s[b]+s[c]), force=True)))
    vals = [sp.nsimplify(sp.simplify(v)) for v in vals]
    return min(vals, key=lambda v: float(v)), vals

def numeric_check(e):
    # independent check: Newton-free; solve via products ab, bc, ca
    k = math.log2(3)
    r = [p + q*k for p, q in e]
    P = sum(r)/2
    ab, bc, ca = P - r[2], P - r[0], P - r[1]
    abc = math.sqrt(ab*bc*ca)
    out = []
    for sgn in (1, -1):
        t = sgn*abc
        A, B, C = t/bc, t/ca, t/ab
        assert abs(A*(B+C)-r[0]) < 1e-9 and abs(B*(C+A)-r[1]) < 1e-9 and abs(C*(A+B)-r[2]) < 1e-9
        out.append(2**(A+B+C))
    return min(out)

orig = [(8, 4), (9, 6), (5, 10)]
var  = [(12, 4), (6, 1), (10, 5)]
mo, allo = solve(orig)
print("original:", mo, "all:", allo, "numeric:", numeric_check(orig), "1/576 =", 1/576)
assert sp.simplify(mo - sp.Rational(1, 576)) == 0
mv, allv = solve(var)
print("variant:", mv, "all:", allv, "numeric:", numeric_check(var), "1/384 =", 1/384)
