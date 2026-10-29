
<invoke name="Bash">
<parameter name="command">cat > /tmp/cuenta_cajas.py <<'EOF'
from itertools import combinations

def ok(box):
    s = set(box)
    return all((b-1 in s) or (b+1 in s) for b in s)

def rec(rest):
    if not rest:
        return 1
    first = rest[0]
    total = 0
    for comb in combinations(rest[1:], 3):
        box = (first,) + comb
        if ok(box):
            resto = tuple(x for x in rest if x not in box)
            total += rec(resto)
    return total

print(rec(tuple(range(1, 17))))
EOF
python3 -I /tmp/cuenta_cajas.py</parameter>
</invoke>


```
105
```