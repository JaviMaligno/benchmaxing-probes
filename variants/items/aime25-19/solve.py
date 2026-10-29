from fractions import Fraction
from math import gcd
import mpmath as mp
mp.mp.dps = 50

def exact(a, b, base_k_target):
    # prod_{k=a}^{b} log_k(B^{k^2-1}) / log_{k+1}(B^{k^2-4})
    # = prod (k^2-1)/(k^2-4) * prod ln(k+1)/ln(k) = prod(...) * log_a(b+1)
    r = Fraction(1)
    for k in range(a, b + 1):
        r *= Fraction(k*k - 1, k*k - 4)
    # log_a(b+1) must be an integer e with a^e == b+1
    e = 0; v = 1
    while v < b + 1:
        v *= a; e += 1
    assert v == b + 1
    return r * e

def numeric(a, b, B):
    p = mp.mpf(1)
    for k in range(a, b + 1):
        p *= (mp.log(mp.mpf(B)**0 * 1) + (k*k - 1) * mp.log(B) / mp.log(k)) / ((k*k - 4) * mp.log(B) / mp.log(k + 1))
    return p

for name, a, b, B, expect in [("original", 4, 63, 5, 106), ("variant", 3, 80, 7, None)]:
    r = exact(a, b, None)
    n = numeric(a, b, B)
    assert abs(n - mp.mpf(r.numerator) / r.denominator) < mp.mpf(10)**-30
    print(name, r, "m+n =", r.numerator + r.denominator, "numeric", mp.nstr(n, 20))
    if expect is not None:
        assert r.numerator + r.denominator == expect
