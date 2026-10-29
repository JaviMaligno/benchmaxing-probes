from fractions import Fraction
from functools import lru_cache
from sympy.utilities.iterables import multiset_permutations
from math import factorial

def dp(nvals, copies):
    @lru_cache(None)
    def E(counts, last):
        tot = sum(counts)
        if tot == 0: return Fraction(0)
        r = Fraction(0)
        for v, c in enumerate(counts):
            if c == 0: continue
            nc = list(counts); nc[v] -= 1; nc = tuple(nc)
            if last == v: r += Fraction(c, tot) * (1 + E(nc, -1))
            else: r += Fraction(c, tot) * E(nc, v)
        return r
    return E(tuple([copies]*nvals), -1)

def brute(nvals, copies):
    deck = [v for v in range(nvals) for _ in range(copies)]
    total = 0; cnt = 0
    for p in multiset_permutations(deck):
        n = 0; last = -1
        for x in p:
            if x == last: n += 1; last = -1
            else: last = x
        total += n; cnt += 1
    return Fraction(total, cnt)

orig = dp(3, 4); print("original DP:", orig, "brute:", brute(3, 4))
assert orig == Fraction(138, 55)
var = dp(4, 3); print("variant DP:", var, "brute:", brute(4, 3))
