from fractions import Fraction as F
from sympy import sqrt, Rational, nsimplify

def val(a, b, c):
    a, b, c = F(a), F(b), F(c)
    r = a*a - b*b
    s = sqrt(Rational(r.numerator, r.denominator))
    exact = nsimplify(s / Rational((c - a).numerator, (c - a).denominator))
    num = ((float(a)**2 - float(b)**2) ** 0.5) / (float(c) - float(a))  # independent float check
    assert abs(float(exact) - num) < 1e-9
    return exact

orig = val("2.5", "0.7", "2.7")
print("original:", orig)
assert orig == 12
var = val("3.7", "1.2", "4.2")
print("variant:", var)
