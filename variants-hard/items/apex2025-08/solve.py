# Brute force: enumerate all L-triomino tilings of an R x C rectangle, build the
# neighbor graph (pieces sharing a unit edge), count proper k-colorings.
import itertools, sys

def L_shapes():
    out = set()
    for miss in range(4):
        sq = [(0,0),(0,1),(1,0),(1,1)]
        cells = [c for i,c in enumerate(sq) if i != miss]
        out.add(tuple(sorted(cells)))
    return list(out)

def tilings(R, C):
    shapes = L_shapes()
    grid = [[-1]*C for _ in range(R)]
    res = []
    def first_empty():
        for r in range(R):
            for c in range(C):
                if grid[r][c] < 0: return r, c
        return None
    def rec(k):
        fe = first_empty()
        if fe is None:
            res.append([row[:] for row in grid]); return
        r0, c0 = fe
        for sh in shapes:
            anchor = min(sh)  # first cell in row-major order
            dr, dc = r0-anchor[0], c0-anchor[1]
            cells = [(a+dr, b+dc) for a,b in sh]
            if all(0<=a<R and 0<=b<C and grid[a][b] < 0 for a,b in cells):
                for a,b in cells: grid[a][b] = k
                rec(k+1)
                for a,b in cells: grid[a][b] = -1
    rec(0)
    return res

def colorings(g, k):
    n = max(max(row) for row in g) + 1
    R, C = len(g), len(g[0])
    adj = [set() for _ in range(n)]
    for r in range(R):
        for c in range(C):
            for a,b in ((r+1,c),(r,c+1)):
                if a<R and b<C and g[a][b] != g[r][c]:
                    adj[g[r][c]].add(g[a][b]); adj[g[a][b]].add(g[r][c])
    col = [-1]*n
    def rec(i):
        if i == n: return 1
        t = 0
        for x in range(k):
            if all(col[j] != x for j in adj[i]):
                col[i] = x; t += rec(i+1); col[i] = -1
        return t
    return rec(0)

def count(R, C, k=3):
    T = tilings(R, C)
    return len(T), sum(colorings(g, k) for g in T)

if __name__ == "__main__":
    nt, tot = count(4, 6)
    print("ORIGINAL 4x6: tilings =", nt, "colored count =", tot, "| expected 1164 ->", tot == 1164)
    nt, tot = count(5, 6)
    print("VARIANT 5x6: tilings =", nt, "colored count =", tot)
    nt2, tot2 = count(6, 5)
    print("VARIANT check transposed 6x5:", nt2, tot2, "| consistent ->", tot2 == tot)
