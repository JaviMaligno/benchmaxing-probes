from itertools import combinations

def count(rows, cols, start, home, k):
    cells = [(r, c) for r in range(rows) for c in range(cols)]
    others = [p for p in cells if p not in (start, home)]
    total = 0
    for rem in combinations(others, k):
        alive = set(cells) - set(rem)
        seen = {start}; stack = [start]
        while stack:
            r, c = stack.pop()
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                q = (r+d[0], c+d[1])
                if q in alive and q not in seen:
                    seen.add(q); stack.append(q)
        if home not in seen:
            total += 1
    return total

# rows indexed from bottom (row 0 = bottom), cols from left
orig = count(3, 3, (0, 0), (2, 2), 4)
print("original (3x3, BL->TR, remove 4):", orig)
assert orig == 29
# independent check: complement count (removals where home IS reachable)
from math import comb
def reach(rows, cols, start, home, k):
    return comb(rows*cols-2, k) - count(rows, cols, start, home, k)
assert reach(3,3,(0,0),(2,2),4) + orig == comb(7,4)

variant = count(3, 3, (0, 0), (2, 1), 4)
print("variant (3x3, BL->top-middle, remove 4):", variant)
