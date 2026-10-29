# Exact computation. For P(a ever at root before target reaches root), only the
# positions of a and target matter: Markov chain on ordered pairs of distinct nodes.
# Nodes: 0 root, 1 left child, 2 right child, 3,4 children of 1, 5,6 children of 2.
# Original tree labels at nodes: (4,2,6,1,3,5,7).
from fractions import Fraction
import random

EDGES = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
INIT = (4,2,6,1,3,5,7)

def swap(p, u, v):
    return v if p == u else (u if p == v else p)

def solve_linear(A, b):
    n = len(b)
    A = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        inv = 1 / A[c][c]
        A[c] = [x * inv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] for i in range(n)]

def hit_prob(pa, pt):
    """P(label at pa reaches root before label at pt)."""
    if pa == 0: return Fraction(1)
    if pt == 0: return Fraction(0)
    states = [(x, y) for x in range(1, 7) for y in range(1, 7) if x != y]
    ix = {s: i for i, s in enumerate(states)}
    n = len(states); w = Fraction(1, len(EDGES))
    A = [[Fraction(0)] * n for _ in range(n)]; b = [Fraction(0)] * n
    for (x, y) in states:
        i = ix[(x, y)]; A[i][i] += 1
        for u, v in EDGES:
            nx, ny = swap(x, u, v), swap(y, u, v)
            if nx == 0: b[i] += w
            elif ny == 0: pass
            else: A[i][ix[(nx, ny)]] -= w
    return solve_linear(A, b)[ix[(pa, pt)]]

def total(target, others):
    pos = {lab: i for i, lab in enumerate(INIT)}
    return sum(hit_prob(pos[a], pos[target]) for a in others)

def mc(target, others, trials=200000, seed=1):
    rng = random.Random(seed); s = 0
    for _ in range(trials):
        lab = list(INIT); seen = {lab[0]}
        while lab[0] != target:
            u, v = rng.choice(EDGES); lab[u], lab[v] = lab[v], lab[u]; seen.add(lab[0])
        s += sum(1 for a in others if a in seen)
    return s / trials

orig = total(7, (1,2,3,5,6))
print("ORIGINAL (target 7):", orig, "matches 11/4:", orig == Fraction(11, 4))
var = total(6, (1,2,3,5,7))
print("VARIANT (target 6):", var, float(var))
print("Monte Carlo original:", mc(7, (1,2,3,5,6)))
print("Monte Carlo variant :", mc(6, (1,2,3,5,7)))
