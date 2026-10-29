```bash
cat > /tmp/solve_triples.py <<'EOF'
from itertools import permutations

def comp(a,b):  # (a o b)(x) = a(b(x))
    return tuple(a[b[i]] for i in range(6))

def inv(a):
    r=[0]*6
    for i,v in enumerate(a): r[v]=i
    return tuple(r)

perms=list(permutations(range(6)))
count=0
sols=[]
for p in perms:
    pi=inv(p)
    for q in perms:
        qi=inv(q)
        # pqr=q  =>  r = q^{-1} p^{-1} q
        r=comp(qi,comp(pi,q))
        if (comp(p,comp(q,r))==q and comp(r,comp(q,p))==q and
            comp(q,comp(r,p))==r and comp(p,comp(r,q))==r and
            comp(r,comp(p,q))==p and comp(q,comp(p,r))==p):
            count+=1
            sols.append((p,q,r))
print(count)
EOF
python3 -I /tmp/solve_triples.py
```