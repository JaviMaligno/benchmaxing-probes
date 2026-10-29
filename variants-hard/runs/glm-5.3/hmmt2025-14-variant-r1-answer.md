```python
import sys
sys.setrecursionlimit(10000)
start=(0,0); goal=(4,2)
moves=[(1,0),(0,1),(-1,1),(1,-1)]
def nxt(p):
    x,y=p
    for dx,dy in moves:
        q=(x+dx,y+dy)
        if 0<=q[0]<=4 and 0<=q[1]<=2:
            yield q
count=0
def dfs(p,visited):
    global count
    if p==goal:
        count+=1
        return
    for q in nxt(p):
        if q not in visited:
            dfs(q,visited|{q})
dfs(start,{start})
print(count)
```
El contador devuelve `131`.