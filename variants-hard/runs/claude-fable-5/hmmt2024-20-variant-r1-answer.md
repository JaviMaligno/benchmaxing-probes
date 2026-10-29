Voy a calcular esto con un script rápido de Python por fuerza bruta sobre las permutaciones de 1–9.

▶ **Bash**: _Contar pandigitales 1-9 cuyo doble también es pandigital 1-9_
```
python3 -I -c "
from itertools import permutations
target = set('123456789')
count = 0
for p in permutations('123456789'):
    m = int(''.join(p))
    n = 2*m
    s = str(n)
    if len(s) == 9 and set(s) == target:
        count += 1
print(count)
"
```

✱ Running…