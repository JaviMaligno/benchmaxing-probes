# Range of f(x) = floor(c * b^x), b negative rational with |b|<1, x>=0.
# b^x is real only for integer x (same convention as the original solution).
from fractions import Fraction as F
import math

def range_size(c, b, N=200):
    vals = set()
    for n in range(N):
        vals.add(math.floor(c * b**n))
    # beyond N terms |c*b^n| < 1 tiny: floor is 0 (positive) or -1 (negative); both already seen
    assert abs(c * b**N) < F(1, 10**6)
    return vals

orig = range_size(F(1), F(-5, 8))
print("original values:", sorted(orig), "count:", len(orig))
assert len(orig) == 3

var = range_size(F(2), F(-3, 5))
print("variant values:", sorted(var), "count:", len(var))
