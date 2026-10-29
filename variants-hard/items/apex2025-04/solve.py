"""apex2025-04 variant check.
Original solution's result: S(p) = p! (smallest n divisible by p admitting an n x n
divisoral table). We (1) brute-force small cases (S(2)=2; no 3x3 table; a 6x6 table
exists, so S(3)=6) by backtracking over numbers built from small primes,
(2) reproduce the original answer from S(p)=p!, (3) compute the variant answer."""
from itertools import combinations
from math import factorial, lcm

def divisors(x): return [d for d in range(1, x + 1) if x % d == 0]
def primerange(a, b): return [q for q in range(max(a, 2), b) if all(q % d for d in range(2, int(q**.5) + 1))]

def nd(x): return len(divisors(x))

def table_exists(n, cands):
    for rows in combinations(cands, n):
        rem = [set(divisors(r)) for r in rows]
        def bt(col):
            if col == n: return True
            def pick(i, chosen, L):
                if i == n:
                    if set(divisors(L)) == set(chosen):
                        for k, x in enumerate(chosen): rem[k].discard(x)
                        if bt(col + 1): return True
                        for k, x in enumerate(chosen): rem[k].add(x)
                    return False
                for x in sorted(rem[i]):
                    if x in chosen: continue
                    L2 = lcm(L, x)
                    if nd(L2) > n: continue
                    if pick(i + 1, chosen + [x], L2): return True
                return False
            return pick(0, [], 1)
        if bt(0): return True
    return False

P = [2, 3, 5, 7, 11]
assert table_exists(2, [p for p in P])                       # 2x2 exists
assert not table_exists(3, [p*p for p in P])                 # no 3x3 (rows are q^2)
c6 = sorted({q*q*r for q in P[:4] for r in P[:4] if q != r} | {q**5 for q in P[:3]})
assert table_exists(6, c6)                                   # 6x6 exists
print("brute force: S(2)=2, S(3)=6, consistent with S(p)=p!")

S = factorial
orig = sum(S(p) for p in primerange(2, 14))
print("original (primes p <= 13):", orig, "OK" if orig == 6266942768 else "MISMATCH")
var = sum(S(p) for p in primerange(5, 18))
print("variant (primes 5 <= p <= 17):", var)
