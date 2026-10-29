```bash
python3 -I -c "
from sympy import n_order, factorint
def vp(n,p):
    s=0;q=p
    while q<=n: s+=n//q; q*=p
    return s
bad=[]
for n in range(60,121):
    m=2*n+3
    d=n_order(2,m)
    ok=all(vp(n,q)>=e for q,e in factorint(d).items())
    if not ok: bad.append((n,m,d))
print(bad, sum(x[0] for x in bad))
"
```