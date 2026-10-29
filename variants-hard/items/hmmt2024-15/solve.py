# Count labelled 3-regular graphs on n vertices in which every pair of distinct
# vertices has exactly 0 or 2 common neighbours. Exhaustive backtracking
# (each labelled graph generated exactly once: vertex v picks its remaining
# neighbours among higher-indexed vertices).
from itertools import combinations
from math import comb, factorial

def count(n, d=3, fix0=False):
    adj = [0]*n
    if fix0:
        # by symmetry, count graphs with N(0) = {1,2,3}; total = this * C(n-1,3)
        for u in (1, 2, 3):
            adj[0] |= 1 << u; adj[u] |= 1

    pc = lambda x: bin(x).count("1")
    total = 0
    def rec(v):
        nonlocal total
        if v == n:
            total += 1
            return
        need = d - pc(adj[v])
        if need < 0:
            return
        cands = [u for u in range(v+1, n) if pc(adj[u]) < d]
        for S in combinations(cands, need):
            for u in S:
                adj[v] |= 1 << u; adj[u] |= 1 << v
            good = True
            # v is now complete; pairs (a, v), a < v, are final -> must be 0 or 2
            for a in range(v):
                if pc(adj[a] & adj[v]) not in (0, 2):
                    good = False; break
            # partial pruning: no pair may exceed 2 common neighbours
            if good:
                touched = (v,) + S
                for x in touched:
                    for y in range(n):
                        if y != x and pc(adj[x] & adj[y]) > 2:
                            good = False; break
                    if not good: break
            if good:
                rec(v+1)
            for u in S:
                adj[v] &= ~(1 << u); adj[u] &= ~(1 << v)
    rec(0)
    return total

orig = count(8)
assert count(8, fix0=True) * comb(7, 3) == orig
print("original n=8 brute force:", orig, "(expected 875)")
assert orig == 875
formula12 = factorial(12)//(factorial(3)*24**3) + comb(12, 4)*840
print("variant n=12 closed form (3 K4's + K4 & cube):", formula12)
var = count(12, fix0=True) * comb(11, 3)
print("variant n=12 brute force:", var)
assert var == formula12
print("ANSWER:", var)
