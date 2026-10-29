from fractions import Fraction as F
import random

def solve(S1, S2, S3):
    S1, S2, S3 = F(S1), F(S2), F(S3)
    # Cauchy-Schwarz: S1*S3 >= S2^2, equality iff all a_i equal
    assert S1 * S3 >= S2 ** 2
    if S1 * S3 > S2 ** 2:
        raise ValueError("no equality; method does not pin n")
    a = S2 / S1           # common value
    n = S1 / a            # = S1^2 / S2
    assert n.denominator == 1 and n > 0
    n = int(n)
    # consistency of all three sums with a_i = a
    assert n * a == S1 and n * a**2 == S2 and n * a**3 == S3
    return n

# sanity: CS strict for random non-constant positive sequences
for _ in range(2000):
    k = random.randint(2, 8)
    v = [F(random.randint(1, 50), random.randint(1, 10)) for _ in range(k)]
    if len(set(v)) > 1:
        assert sum(v) * sum(x**3 for x in v) > sum(x**2 for x in v) ** 2

orig = solve(96, 144, 216)
print("original:", orig)
assert orig == 64
var = solve(108, 144, 192)
print("variant:", var)
