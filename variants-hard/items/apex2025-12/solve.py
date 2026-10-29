"""apex2025-12 variant check.
Problem: n x n grid, disjoint grid-aligned rectangles, each row and column has exactly
one uncovered cell (holes form a permutation). Minimise number of tiles.
Known answer f(n) = n + ceil(2*sqrt(n)) - 3  (n = k^2 -> n + 2k - 3).
Checks:
 (1) exact brute force over ALL permutations, exact min rectangle partition (ILP; small n cross-checked by branch-and-bound), n = 1..6
 (2) exact ILP (scipy HiGHS) min partition for the standard k^2 construction, n = 4, 9, 16, 25
     -> confirms the bound is attained for perfect squares
 (3) original n=2025 -> 2112 ; variant n=2116 -> ?
"""
import itertools, math
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

def f(n):
    return n + math.isqrt(4*n - 1) + 1 - 3 if n > 0 else 0  # ceil(2 sqrt n) = isqrt(4n-1)+1

def min_partition_bb(n, holes):
    grid = [[False]*n for _ in range(n)]
    for r, c in holes: grid[r][c] = True   # True = blocked/covered
    free = n*n - n
    best = [free]
    def rec(count, left):
        if count >= best[0]: return
        if left == 0: best[0] = count; return
        # first free cell row-major
        for r in range(n):
            row = grid[r]
            for c in range(n):
                if not row[c]: break
            else: continue
            break
        # width options
        maxw = 0
        while c+maxw < n and not grid[r][c+maxw]: maxw += 1
        for w in range(maxw, 0, -1):
            h = 0
            while r+h < n and all(not grid[r+h][c+x] for x in range(w)): h += 1
            for hh in range(h, 0, -1):
                for y in range(hh):
                    for x in range(w): grid[r+y][c+x] = True
                rec(count+1, left - w*hh)
                for y in range(hh):
                    for x in range(w): grid[r+y][c+x] = False
    rec(0, free)
    return best[0]

def brute(n):
    return min(min_partition_ilp(n, [(i, p[i]) for i in range(n)]) for p in itertools.permutations(range(n)))

def min_partition_ilp(n, holes):
    H = set(holes)
    pre = np.zeros((n+1, n+1), int)
    for r, c in holes: pre[r+1][c+1] = 1
    pre = pre.cumsum(0).cumsum(1)
    rects = []
    for r1 in range(n):
        for r2 in range(r1, n):
            for c1 in range(n):
                for c2 in range(c1, n):
                    s = pre[r2+1][c2+1]-pre[r1][c2+1]-pre[r2+1][c1]+pre[r1][c1]
                    if s: break
                    rects.append((r1, r2, c1, c2))
    cells = [(r, c) for r in range(n) for c in range(n) if (r, c) not in H]
    if not cells: return 0
    idx = {cell: i for i, cell in enumerate(cells)}
    A = lil_matrix((len(cells), len(rects)))
    for j, (r1, r2, c1, c2) in enumerate(rects):
        for r in range(r1, r2+1):
            for c in range(c1, c2+1): A[idx[(r, c)], j] = 1
    res = milp(np.ones(len(rects)), constraints=LinearConstraint(A.tocsr(), 1, 1),
               integrality=np.ones(len(rects)), bounds=Bounds(0, 1))
    return round(res.fun)

def construction(k):
    n = k*k
    return [(a*k + b, b*k + (k-1-a)) for a in range(k) for b in range(k)]

print("(1) brute force over all permutations:")
for n in range(1, 7):
    b = brute(n); print(f"  n={n}: min={b}, formula={f(n)}", "OK" if b == f(n) else "MISMATCH")
for n in range(1, 5):
    assert all(min_partition_bb(n, [(i, p[i]) for i in range(n)]) == min_partition_ilp(n, [(i, p[i]) for i in range(n)]) for p in itertools.permutations(range(n)))
print("  branch-and-bound == ILP on every permutation for n<=4")
print("(2) ILP on k^2 construction:")
for k in range(2, 6):
    holes = construction(k)
    assert sorted(c for _, c in holes) == list(range(k*k))
    v = min_partition_ilp(k*k, holes); print(f"  n={k*k}: tiles={v}, formula={f(k*k)}", "OK" if v == f(k*k) else "MISMATCH")
print("(3) original n=2025:", f(2025), "(expected 2112)", "OK" if f(2025) == 2112 else "FAIL")
print("    variant  n=2116:", f(2116))
