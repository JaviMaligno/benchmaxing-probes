from fractions import Fraction
from math import lcm
from sympy import divisors

def brute(N):
    A = divisors(N)
    k = len(A)
    good = 0
    for mask in range(1, 1 << k):
        l = 1
        for i in range(k):
            if mask >> i & 1:
                l = lcm(l, A[i])
        if l == N:
            good += 1
    p = Fraction(good, 1 << k)
    return p, p.numerator + p.denominator

def incl_excl(N):
    from sympy import factorint
    exps = list(factorint(N).values())
    k = 1
    for e in exps: k *= e + 1
    tot = 0
    for mask in range(1 << len(exps)):
        size = 1; sign = 1
        for i, e in enumerate(exps):
            if mask >> i & 1:
                size *= e; sign = -sign
            else:
                size *= e + 1
        tot += sign * 2**size
    p = Fraction(tot, 2**k)
    return p, p.numerator + p.denominator

for label, N in [("original", 2025), ("variant", 675)]:
    pb, ab = brute(N); pi, ai = incl_excl(N)
    print(label, N, "brute:", pb, ab, "incl-excl:", pi, ai)
assert brute(2025)[1] == 237
