"""Lame king longest simple path from the top-left corner of an R x C grid.
Moves: to any of the 8 neighbours except the two in the same column,
so every move changes the column by exactly +-1.
Method:
  * exact brute force (exhaustive DFS) on small grids;
  * on the target grids: parity upper bound (columns alternate parity, so the
    path alternates between start-parity columns A and the other class B:
    length <= 2|B|+1 when |A|>|B|), plus a DFS that finds a path attaining it.
"""
import sys
sys.setrecursionlimit(10000)

def nbrs(R, C):
    N = {}
    for r in range(R):
        for c in range(C):
            N[(r, c)] = [(r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 1)
                         if 0 <= r + dr < R and 0 <= c + dc < C]
    return N

def exact_bruteforce(R, C):
    N = nbrs(R, C); seen = {(0, 0)}; best = [1]
    def dfs(v, L):
        if L > best[0]: best[0] = L
        for w in N[v]:
            if w not in seen:
                seen.add(w); dfs(w, L + 1); seen.remove(w)
    dfs((0, 0), 1)
    return best[0]

def bound(R, C):
    A = sum(R for c in range(C) if c % 2 == 0)   # start column parity
    B = R * C - A
    return 2 * B + 1 if A > B else 2 * A if B > A else R * C

def find_path(R, C, target):
    N = nbrs(R, C); seen = {(0, 0)}; path = [(0, 0)]
    def free_deg(w): return sum(1 for x in N[w] if x not in seen)
    def dfs(v):
        if len(path) == target: return True
        cand = sorted((w for w in N[v] if w not in seen), key=lambda w: (free_deg(w), w))
        for w in cand:
            seen.add(w); path.append(w)
            if dfs(w): return True
            seen.remove(w); path.pop()
        return False
    assert dfs((0, 0))
    # validate path
    assert len(set(path)) == target and path[0] == (0, 0)
    for a, b in zip(path, path[1:]):
        assert abs(a[1] - b[1]) == 1 and abs(a[0] - b[0]) <= 1
    return path

# cross-check the bound against exhaustive search on small grids
for R, C in [(3, 3), (3, 4), (4, 3), (4, 5), (5, 5), (5, 4), (3, 5)]:
    ex = exact_bruteforce(R, C)
    assert ex == bound(R, C), (R, C, ex, bound(R, C))
print("small-grid brute force agrees with bound")

for name, (R, C) in [("original 7x7", (7, 7)), ("variant 9x9", (9, 9))]:
    b = bound(R, C); p = find_path(R, C, b)
    print(name, "bound", b, "attained by path of length", len(p))
