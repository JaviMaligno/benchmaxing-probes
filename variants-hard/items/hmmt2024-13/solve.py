from itertools import combinations, product

def faces(p, n):
    f = set()
    for ax, c in enumerate(p):
        if c == 0: f.add((ax, 0))
        if c == n - 1: f.add((ax, 1))
    return f

def count(n, red, k):
    cells = list(product(range(n), repeat=3))
    tot = 0
    for S in combinations(cells, red):
        u = set()
        for p in S: u |= faces(p, n)
        if len(u) == k: tot += 1
    return tot

orig = count(3, 2, 4)
print("original (3x3x3, 2 red, exactly 4 faces):", orig)
assert orig == 114
for k in range(7):
    print("2 red, exactly", k, "faces:", count(3, 2, k))
var = count(3, 2, 3)
print("VARIANT (3x3x3, 2 red, exactly 3 faces):", var)
