```bash
cd /tmp && cat > ham.py <<'EOF'
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)

def count(n):
    pts=[(i,j) for i in range(1,4) for j in range(1,n+1)]
    idx={p:k for k,p in enumerate(pts)}
    N=len(pts)
    adj=[[] for _ in range(N)]
    for (i,j) in pts:
        for (di,dj) in ((1,0),(-1,0),(0,1),(0,-1)):
            q=(i+di,j+dj)
            if q in idx: adj[idx[(i,j)]].append(idx[q])
    start=idx[(2,1)]
    visited=[False]*N
    total=0
    def connected_ok(cur):
        # remaining unvisited must be connected and reachable from cur
        rem=[k for k in range(N) if not visited[k]]
        if not rem: return True
        # BFS from a neighbor of cur that is unvisited
        seen=set()
        stack=[rem[0]]
        seen.add(rem[0])
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if not visited[w] and w not in seen:
                    seen.add(w); stack.append(w)
        if len(seen)!=len(rem): return False
        # cur must touch the component
        if not any((not visited[w]) for w in adj[cur]): return False
        # degree-1 count check
        deg1=0
        for v in rem:
            d=sum(1 for w in adj[v] if not visited[w])
            d2=d+(1 if cur in adj[v] else 0)
            if d2==0: return False
            if d2==1: deg1+=1
        if deg1>2: return False
        return True
    def dfs(cur,cnt):
        nonlocal total
        if cnt==N:
            total+=1
            return
        if not connected_ok(cur): return
        for w in adj[cur]:
            if not visited[w]:
                visited[w]=True
                dfs(w,cnt+1)
                visited[w]=False
    visited[start]=True
    dfs(start,1)
    return total

for n in range(1,13):
    print(n, count(n))
EOF
python3 -I ham.py
```