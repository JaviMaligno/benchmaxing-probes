from fractions import Fraction
from math import isqrt

def smallest_a(first, ratio_num, limit=10000):
    # series first + first*(r/a) + ...; converges iff r/a < 1
    for a in range(1, limit):
        r = Fraction(ratio_num, a)
        if not (abs(r) < 1):
            continue
        s = Fraction(first) / (1 - r)
        if s.denominator == 1 and s.numerator >= 0 and isqrt(s.numerator) ** 2 == s.numerator:
            # independent numeric check of partial sums
            partial = sum(float(first) * float(r) ** k for k in range(2000))
            assert abs(partial - float(s)) < 1e-6
            return a, s
    return None

orig = smallest_a(4, 3)   # 4 + 12/a + 36/a^2 + ...
print("original:", orig)
assert orig[0] == 4
var = smallest_a(3, 5)    # 3 + 15/a + 75/a^2 + ...
print("variant:", var)
