from itertools import product

def edges(R, C):
    E = []
    for r in range(R + 1):
        for c in range(C):
            E.append(('h', r, c))  # horizontal segment at row-line r, column c
    for r in range(R):
        for c in range(C + 1):
            E.append(('v', r, c))
    return E

def count(R, C, k):
    """Colorings of the unit segments of an R x C grid so every unit square has exactly k red sides."""
    E = edges(R, C)
    idx = {e: i for i, e in enumerate(E)}
    sq = [[idx[('h', r, c)], idx[('h', r + 1, c)], idx[('v', r, c)], idx[('v', r, c + 1)]]
          for r in range(R) for c in range(C)]
    tot = 0
    for col in product((0, 1), repeat=len(E)):
        if all(sum(col[i] for i in s) == k for s in sq):
            tot += 1
    return tot

orig = count(2, 2, 2)
print("original (2x2 grid, 2 red sides each):", orig)
assert orig == 82
variant = count(2, 2, 1)
print("variant (2x2 grid, exactly 1 red side each):", variant)

# independent check: casework on the 4 interior segments; each square has 2 interior
# and 2 boundary sides, needs 1 - m boundary reds where m = its interior reds
from math import comb
chk = 0
for inner in product((0, 1), repeat=4):  # a=top-mid v, b=bottom-mid v, c=left-mid h, d=right-mid h
    a, b, c, d = inner
    ways = 1
    for m in (a + c, a + d, b + c, b + d):  # TL, TR, BL, BR
        ways *= comb(2, 1 - m) if m <= 1 else 0
    chk += ways
print("casework check:", chk)
assert chk == variant
print("ANSWER:", variant)
