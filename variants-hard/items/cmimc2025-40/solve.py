# Maximal simple colorings of an m x n grid.
# Method: rows/columns = vertices of K_{m,n}, black squares = edges; the ant can
# return iff the black edges contain a cycle. Maximal simple = spanning tree of K_{m,n}.
# 1) brute-force ant simulation on small grids to validate the bijection,
# 2) matrix-tree theorem (exact) for the target sizes.
import itertools, sympy as sp

DIRS=[(0,1),(1,0),(0,-1),(-1,0)]
def simple(m,n,black):
    for s in black:
        seen=set(); stack=[(s,d) for d in range(4)]
        while stack:
            (r,c),d=stack.pop()
            if ((r,c),d) in seen: continue
            seen.add(((r,c),d))
            nr,nc=r+DIRS[d][0],c+DIRS[d][1]
            if not(0<=nr<m and 0<=nc<n): continue
            if (nr,nc)==s: return False
            opts=[d]+([(d+1)%4,(d+3)%4] if (nr,nc) in black else [])
            for e in opts: stack.append(((nr,nc),e))
    return True

def brute(m,n):
    cells=[(r,c) for r in range(m) for c in range(n)]
    S=set()
    for mask in range(1<<len(cells)):
        b=frozenset(cells[i] for i in range(len(cells)) if mask>>i&1)
        if simple(m,n,b): S.add(b)
    return sum(1 for b in S if all((b|{x}) not in S for x in cells if x not in b))

def trees(m,n):  # spanning trees of K_{m,n} via matrix-tree theorem
    N=m+n; L=sp.zeros(N,N)
    for i in range(m):
        for j in range(n):
            a,b=i,m+j; L[a,a]+=1; L[b,b]+=1; L[a,b]-=1; L[b,a]-=1
    return L[1:,1:].det()

for (m,n) in [(1,1),(1,3),(2,2),(2,3),(3,3),(3,4),(4,4)]:
    bf=brute(m,n); t=trees(m,n)
    print(f"{m}x{n}: brute={bf} trees={t} formula={m**(n-1)*n**(m-1)}")
    assert bf==t==m**(n-1)*n**(m-1)

# original check: 2024x2024 -> 2024^(2*2024-2)
orig=2024**4046
assert 2024**(2024-1)*2024**(2024-1)==orig
assert trees(6,6)==6**10  # square-case sanity of the same formula
print("original 2024x2024 = 2024^4046 reproduced:", 2024**(2023)*2024**(2023)==orig)

# variant: 6 x 8 grid
v=trees(6,8)
assert v==6**7*8**5
print("variant 6x8 answer =", v, "= 6^7 * 8^5")
