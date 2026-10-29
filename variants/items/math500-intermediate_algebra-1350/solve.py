# Brute force: f = a_n * prod(x - r) over a set S of distinct integer roots.
# Need a_n * (-1)^|S| * prod(S) == a_0; a_{n-1} = -a_n * sum(S). Roots must divide a_0
# (actually a_0/a_n), so enumerate all subsets of the signed divisors.
from itertools import combinations
from sympy import divisors, symbols, expand, Poly
from math import prod

def least(an, a0):
    ds = [d for d in divisors(abs(a0)) ] 
    cand = [s*d for d in ds for s in (1, -1)]
    best = None; wit = None
    for k in range(1, len(cand) + 1):
        for S in combinations(cand, k):
            if an * (-1)**k * prod(S) == a0:
                v = abs(an * sum(S))
                if best is None or v < best:
                    best, wit = v, S
    # verify witness polynomial has integer coefficients
    x = symbols('x')
    p = Poly(expand(an * prod(x - r for r in wit)), x)
    assert p.LC() == an and p.eval(0) == a0
    return best, wit, p.as_expr()

print("original (2, 66):", least(2, 66))
assert least(2, 66)[0] == 14
print("variant  (2, 78):", least(2, 78))
