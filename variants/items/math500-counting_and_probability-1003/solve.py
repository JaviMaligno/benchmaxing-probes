from fractions import Fraction as Fr
from itertools import product
import sympy as sp

def p7(face_F, pF):
    probs = {k: Fr(1,6) for k in range(1,7)}
    probs[face_F] = pF
    probs[7-face_F] = Fr(1,3) - pF
    return sum(probs[a]*probs[b] for a,b in product(range(1,7), repeat=2) if a+b==7)

def solve(target):
    x = sp.symbols('x', positive=True)
    # symbolic enumeration with F=1 (choice of F irrelevant by symmetry)
    probs = {k: sp.Rational(1,6) for k in range(1,7)}
    probs[1] = sp.Rational(1,6)+x; probs[6] = sp.Rational(1,6)-x
    expr = sum(probs[a]*probs[b] for a,b in product(range(1,7), repeat=2) if a+b==7)
    sols = [s for s in sp.solve(sp.Eq(expr, target), x) if 0 < s < sp.Rational(1,6)]
    assert len(sols) == 1
    pF = Fr(str(sp.Rational(1,6)+sols[0]))
    for F in range(1,7):  # independent exact check for every choice of F
        assert p7(F, pF) == Fr(target.p, target.q)
    return pF, pF.numerator + pF.denominator

o = solve(sp.Rational(47,288)); print("original:", o); assert o[1] == 29
v = solve(sp.Rational(71,450)); print("variant:", v)
