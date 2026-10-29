# Brute-force: count all squares (any orientation) with vertices in a 3 x n lattice of points.
from itertools import combinations

def count_squares(rows, cols):
    pts = {(x, y) for x in range(cols) for y in range(rows)}
    seen = set()
    for (x1, y1), (x2, y2) in combinations(sorted(pts), 2):
        dx, dy = x2 - x1, y2 - y1
        for s in (1, -1):  # rotate edge vector both ways
            p3 = (x2 - s*dy, y2 + s*dx)
            p4 = (x1 - s*dy, y1 + s*dx)
            if p3 in pts and p4 in pts:
                seen.add(frozenset([(x1, y1), (x2, y2), p3, p4]))
    sizes = {(lambda q: min((a[0]-b[0])**2 + (a[1]-b[1])**2 for a, b in combinations(q, 2)))(q) for q in seen}
    return len(seen), sizes

def solve(total):
    sols = [n for n in range(2, 200) if count_squares(3, n)[0] == total]
    assert len(sols) == 1, sols
    n = sols[0]
    return n, count_squares(3, n)[1]

n0, s0 = solve(70)
print("original: n =", n0, "squared side lengths:", sorted(s0))
assert n0 == 19 and len(s0) == 3
n1, s1 = solve(86)
print("variant: n =", n1, "squared side lengths:", sorted(s1))
assert len(s1) == 3
