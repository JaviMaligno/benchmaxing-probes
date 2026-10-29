```bash
python3 -I -c "
from itertools import product
rows,cols=4,5
def ok_col(c):
    return all(not(c>>i&1 and c>>(i+1)&1) for i in range(rows-1))
cs=[c for c in range(16) if ok_col(c)]
cnt=0
for g in product(cs,repeat=cols):
    if any(g[j]&g[j+1] for j in range(cols-1)): continue
    bad=False
    for j in range(cols-1):
        for i in range(rows-1):
            m=(1<<i)|(1<<(i+1))
            if not((g[j]|g[j+1])&m): bad=True;break
        if bad: break
    if not bad: cnt+=1
print(cnt)
"
```