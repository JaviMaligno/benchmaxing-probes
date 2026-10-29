from itertools import product

def count(R, C):
    """Brute force: subsets of an R x C grid with no two orthogonally adjacent
    coins and every 2x2 block containing at least one coin."""
    n = R * C
    total = 0
    for mask in range(1 << n):
        g = [[(mask >> (r * C + c)) & 1 for c in range(C)] for r in range(R)]
        ok = True
        for r in range(R):
            for c in range(C):
                if g[r][c] and ((c + 1 < C and g[r][c+1]) or (r + 1 < R and g[r+1][c])):
                    ok = False; break
            if not ok: break
        if not ok: continue
        for r in range(R - 1):
            for c in range(C - 1):
                if not (g[r][c] or g[r][c+1] or g[r+1][c] or g[r+1][c+1]):
                    ok = False; break
            if not ok: break
        if ok: total += 1
    return total

def count_tm(R, C):
    """Independent check: row-by-row transfer matrix."""
    rows = [m for m in range(1 << C) if not (m & (m >> 1))]
    def good(a, b):
        if a & b: return False
        for c in range(C - 1):
            if not (((a | b) >> c) & 3): return False
        return True
    dp = {m: 1 for m in rows}
    for _ in range(R - 1):
        nd = {m: 0 for m in rows}
        for a, v in dp.items():
            for b in rows:
                if good(a, b): nd[b] += v
        dp = nd
    return sum(dp.values())

orig = count(4, 4)
print("original 4x4:", orig, count_tm(4, 4))
assert orig == 256 == count_tm(4, 4)
var = count(4, 5)
print("variant 4x5:", var, count_tm(4, 5))
assert var == count_tm(4, 5)
