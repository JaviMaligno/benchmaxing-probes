"""apex2025-02 variant check.

Original: largest k with a1 + a2 > k*a3 for every simple grid polygon -> 1/2.
Variant : largest k with 2*a1 + 3*a2 > k*a3                          -> 3/2.

Method (same for both): count boundary edges and turns.
  2L = a1 + 2a2 + 3a3 + 4a4   (each boundary edge borders two unit squares)
  T  = a2adj + 2a3 + 4a4      (each turn sits in the right angle of exactly one square)
  T <= L                      (L vertices on the boundary)
  => a1 + 2a2 >= a3 + 4a4 + 2a2adj,  hence  c1*a1 + c2*a2 >= (c2/2)*a3  if c1 >= c2/2,
     strict because a1 >= 1 (square above a topmost edge).
Tightness: a family with a1/a3 -> 0, a2/a3 -> 1/2 (needed for the original answer 1/2).
Then inf (c1 a1 + c2 a2)/a3 = c2/2.

The script (1) enumerates every hole-free, simple-boundary polyomino up to N cells and
checks the identities/lemma exactly, (2) builds an explicit recursive family and shows
both ratios approach c2/2 from above, reproducing 1/2 (original) and 3/2 (variant).
"""
from fractions import Fraction as F
import sys

def boundary_edges(cells):
    E = set()
    for (x, y) in cells:
        for (dx, dy, e) in ((0, -1, ('h', x, y)), (0, 1, ('h', x, y + 1)),
                            (-1, 0, ('v', x, y)), (1, 0, ('v', x + 1, y))):
            if (x + dx, y + dy) not in cells:
                E.add(e)
    return E

def sq_edges(x, y):
    return [('h', x, y), ('h', x, y + 1), ('v', x, y), ('v', x + 1, y)]

def is_simple(cells, E):
    # every boundary vertex has degree 2 and boundary is one cycle
    from collections import defaultdict
    adj = defaultdict(list)
    for e in E:
        if e[0] == 'h':
            a, b = (e[1], e[2]), (e[1] + 1, e[2])
        else:
            a, b = (e[1], e[2]), (e[1], e[2] + 1)
        adj[a].append(b); adj[b].append(a)
    if any(len(v) != 2 for v in adj.values()):
        return False, None
    start = next(iter(adj)); prev = None; cur = start; n = 0
    while True:
        nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
        prev, cur = cur, nxt; n += 1
        if cur == start:
            break
    if n != len(E):
        return False, None
    turns = sum(1 for v, (p, q) in adj.items()
                if not (p[0] == q[0] or p[1] == q[1]))
    return True, turns

def stats(cells):
    cells = set(cells)
    E = boundary_edges(cells)
    ok, T = is_simple(cells, E)
    if not ok:
        return None
    xs = [x for x, _ in cells]; ys = [y for _, y in cells]
    a = [0] * 5; a2adj = 0
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            s = [e in E for e in sq_edges(x, y)]
            k = sum(s); a[k] += 1
            if k == 2 and not ((s[0] and s[1]) or (s[2] and s[3])):
                a2adj += 1
    return dict(a=a, a2adj=a2adj, L=len(E), T=T)

def enumerate_polyominoes(N):
    # Redelmeier enumeration of fixed polyominoes
    out = []
    def nbrs(c):
        x, y = c
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    def ok(c):
        return c[1] > 0 or (c[1] == 0 and c[0] >= 0)
    def rec(poly, untried, seen):
        out.append(frozenset(poly))
        if len(poly) == N:
            return
        untried = list(untried)
        while untried:
            c = untried.pop()
            new = [n for n in nbrs(c) if ok(n) and n not in seen]
            seen2 = seen | set(new)
            rec(poly | {c}, untried + new, seen2)
    rec(frozenset(), [(0, 0)], {(0, 0)})
    return [p for p in out if p]

def check_lemma(N):
    cnt = 0; best = {}
    for P in enumerate_polyominoes(N):
        s = stats(P)
        if s is None:
            continue
        cnt += 1
        a1, a2, a3, a4 = s['a'][1], s['a'][2], s['a'][3], s['a'][4]
        assert 2 * s['L'] == a1 + 2 * a2 + 3 * a3 + 4 * a4
        assert s['T'] == s['a2adj'] + 2 * a3 + 4 * a4
        assert s['T'] <= s['L']
        assert a1 + 2 * a2 >= a3 + 4 * a4 + 2 * s['a2adj']
        assert a1 >= 1
        for c in ((1, 1), (2, 3)):
            if a3:
                r = F(c[0] * a1 + c[1] * a2, a3)
                assert r > F(c[1], 2)
                best[c] = min(best.get(c, r), r)
    return cnt, best

# ---------- explicit tight family ----------
# m horizontal "double combs" (spine row with unit teeth above and below at every even
# column), stacked with period 4 so that tips face tips across a one-cell outside corridor,
# all joined by a vertical bar at x = -1.  Bulk per 2 columns per comb: a3 = 4, a2 = 2, a1 = 0.
def comb_stack(m, n):
    cells = set()
    for j in range(m):
        y0 = 4 * j
        for x in range(n):
            cells.add((x, y0 + 1))
            if x % 2 == 0:
                cells.add((x, y0)); cells.add((x, y0 + 2))
    for y in range(0, 4 * m - 1):
        cells.add((-1, y))
    return cells

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    cnt, best = check_lemma(N)
    print(f"exhaustive: {cnt} simple polyominoes up to {N} cells; lemma a1+2a2 >= a3+4a4+2a2adj holds")
    print("min ratios found exhaustively:", {k: str(v) for k, v in best.items()})
    for c, name in (((1, 1), "ORIGINAL a1+a2"), ((2, 3), "VARIANT 2a1+3a2")):
        print(f"{name}: lower bound c2/2 = {F(c[1], 2)}; family ratios:")
        for m in (2, 5, 10, 20, 40):
            P = comb_stack(m, 2 * m + 1)
            s = stats(P); a = s['a']
            r = F(c[0] * a[1] + c[1] * a[2], a[3])
            assert r > F(c[1], 2)
            print(f"  m={m:3d} a1={a[1]} a2={a[2]} a3={a[3]} ratio={r} ~ {float(r):.5f}")
    print("ANSWER original k = 1/2 ; ANSWER variant k = 3/2")
