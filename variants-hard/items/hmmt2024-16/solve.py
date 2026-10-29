# Brute force: each cell gets diagonal 0 ('\') or 1 ('/'); build region adjacency graph
# of the 2*R*C triangles and test bipartiteness. Count good configurations exactly.
from fractions import Fraction
from itertools import product

def tri(d, side):
    # returns which of the cell's two triangles (0/1) touches the given side
    # d=0 '\': tri0 = {top,right}, tri1 = {left,bottom}
    # d=1 '/': tri0 = {top,left},  tri1 = {bottom,right}
    if d == 0:
        return 0 if side in ('T', 'R') else 1
    return 0 if side in ('T', 'L') else 1

def bipartite(R, C, conf):
    n = 2 * R * C
    adj = [[] for _ in range(n)]
    idx = lambda r, c, t: 2 * (r * C + c) + t
    for r in range(R):
        for c in range(C):
            d = conf[r * C + c]
            a, b = idx(r, c, 0), idx(r, c, 1)
            adj[a].append(b); adj[b].append(a)
            if c + 1 < C:
                u = idx(r, c, tri(d, 'R')); v = idx(r, c + 1, tri(conf[r * C + c + 1], 'L'))
                adj[u].append(v); adj[v].append(u)
            if r + 1 < R:
                u = idx(r, c, tri(d, 'B')); v = idx(r + 1, c, tri(conf[(r + 1) * C + c], 'T'))
                adj[u].append(v); adj[v].append(u)
    col = [-1] * n
    for s in range(n):
        if col[s] >= 0: continue
        col[s] = 0; st = [s]
        while st:
            x = st.pop()
            for y in adj[x]:
                if col[y] < 0:
                    col[y] = col[x] ^ 1; st.append(y)
                elif col[y] == col[x]:
                    return False
    return True

def prob(R, C):
    good = sum(bipartite(R, C, conf) for conf in product((0, 1), repeat=R * C))
    return Fraction(good, 2 ** (R * C))

orig = prob(4, 4)
print("original 4x4:", orig, "matches 1/512:", orig == Fraction(1, 512))
var = prob(4, 5)
print("variant 4x5:", var)
