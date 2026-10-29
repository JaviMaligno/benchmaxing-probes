# Brute force: unordered pairs of grid rectangles in an m x n grid of squares whose
# closed regions are disjoint (no shared interior, edge, or vertex).
from itertools import combinations
from math import comb

def rects(m, n):
    # rectangle = (x1, x2, y1, y2) with 0<=x1<x2<=n, 0<=y1<y2<=m (grid-line coords)
    return [(x1, x2, y1, y2) for x1 in range(n+1) for x2 in range(x1+1, n+1)
            for y1 in range(m+1) for y2 in range(y1+1, m+1)]

def disjoint(a, b):
    # closed rectangles disjoint iff separated strictly along some axis
    return a[1] < b[0] or b[1] < a[0] or a[3] < b[2] or b[3] < a[2]

def count(m, n):
    R = rects(m, n)
    return sum(1 for a, b in combinations(R, 2) if disjoint(a, b))

def formula(m, n):
    # independent check: inclusion-exclusion on separation axes
    # pairs of disjoint closed intervals on a line with k+1 points: C(k+1,4)
    sx, sy = comb(n+1, 4), comb(m+1, 4)
    tx, ty = comb(n+1, 2), comb(m+1, 2)
    # separated in x: ordered-unordered pair of x-intervals disjoint (sx), any y for each (ty^2)
    both = 2 * sx * sy  # separated in both axes: two diagonal orientations
    return sx * ty * ty + sy * tx * tx - both

orig = count(5, 5)
print("original 5x5:", orig, "formula:", formula(5, 5), "expected 6300 ->", orig == 6300)
var = count(6, 6)
print("variant 6x6:", var, "formula:", formula(6, 6))
