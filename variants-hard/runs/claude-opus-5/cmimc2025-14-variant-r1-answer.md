
<invoke name="Bash">
<parameter name="command">cd /tmp && cat > hk.py << 'EOF'
from itertools import combinations
def comps(n,k):
    par={i:i for i in range(1<<n)}
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    masks=[sum(1<<i for i in c) for c in combinations(range(n),k)]
    for v in range(1<<n):
        for m in masks:
            a,b=f(v),f(v^m)
            if a!=b: par[a]=b
    return len({f(v) for v in range(1<<n)})
tot=0
for n in range(1,13):
    for k in range(1,n+1):
        d=comps(n,k); tot+=d
        if n<=5: print(n,k,d)
print("TOTAL",tot)
EOF
python3 -I hk.py</parameter>
</invoke>