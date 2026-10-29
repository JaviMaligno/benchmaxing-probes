"""apex2025-05 variant: staircase cut of a W x H rectangle reassembled into a new rectangle.
Formula: shifting a k-step staircase by one step turns W x H into
W*k/(k+1) x H*(k+1)/k, needing (k+1)|W and k|H (or roles of W,H swapped).
Count distinct unordered results not congruent to the original.
Validated against an exhaustive brute force (all monotone cuts, all placements) on small rectangles."""
from itertools import product
from functools import lru_cache

def formula(W, H):
    res = set()
    for A, B in ((W, H), (H, W)):
        for k in range(1, B + 1):
            if B % k == 0 and A % (k + 1) == 0:
                r = tuple(sorted((A * k // (k + 1), B * (k + 1) // k)))
                res.add(r)
    res.discard(tuple(sorted((W, H))))
    return len(res), sorted(res)

def norm(cells):
    mx = min(x for x, y in cells); my = min(y for x, y in cells)
    return frozenset((x - mx, y - my) for x, y in cells)

def orients(cells):
    out = set()
    for sx, sy, sw in product((1, -1), (1, -1), (0, 1)):
        c = [((y if sw else x) * sx, (x if sw else y) * sy) for x, y in cells]
        out.add(norm(c))
    return out

def canon(cells):
    return min(tuple(sorted(o)) for o in orients(cells))

def brute(W, H):
    full = {(x, y) for x in range(W) for y in range(H)}
    area = W * H
    targets = [(a, area // a) for a in range(1, area + 1) if area % a == 0 and a <= area // a]
    found = set()
    def seqs(i, lo):
        if i == W:
            yield ()
            return
        for t in range(lo, H + 1):
            for rest in seqs(i + 1, t):
                yield (t,) + rest
    for t in seqs(0, 0):
        if all(v == 0 for v in t) or all(v == H for v in t):
            continue
        A = {(x, y) for x in range(W) for y in range(t[x])}
        Bc = canon(full - A)
        for (a, b) in targets:
            if (a, b) in found or (a, b) == tuple(sorted((W, H))):
                continue
            ok = False
            for o in orients(A):
                ow = max(x for x, y in o) + 1; oh = max(y for x, y in o) + 1
                for dx in range(a - ow + 1):
                    for dy in range(b - oh + 1):
                        P = {(x + dx, y + dy) for x, y in o}
                        rest = {(x, y) for x in range(a) for y in range(b)} - P
                        if canon(rest) == Bc:
                            ok = True; break
                    if ok: break
                if ok: break
            if ok:
                found.add((a, b))
    return len(found), sorted(found)

# brute-force validation on small rectangles
for W, H in [(4, 5), (5, 6), (6, 7), (6, 8), (4, 9), (3, 8), (4, 6)]:
    f, b = formula(W, H), brute(W, H)
    print(f"{W}x{H}: formula={f[0]} brute={b[0]}", "OK" if f == b else f"MISMATCH {f} {b}")

orig = formula(2024, 2025)
print("original 2024x2025:", orig[0], orig[1], "expected 6 ->", orig[0] == 6)
var = formula(1935, 1936)
print("variant 1935x1936:", var[0], var[1])
