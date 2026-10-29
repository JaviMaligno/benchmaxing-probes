Voy a analizar la estructura del problema y verificarla con cálculo.

**Análisis:** cada jarra tiene 4 canicas, y cada canica necesita un vecino en su jarra. Por tanto, los *tramos* (bloques maximales de consecutivos) dentro de una jarra tienen longitud ≥ 2: una jarra es un tramo de 4 consecutivos, o dos pares de consecutivos no adyacentes.

Si marco los "cortes" entre $i$ e $i+1$ cuando están en jarras distintas, obtengo una composición de 20 en partes de tamaño 2 y 4. Cada parte 4 es una jarra; las partes 2 se emparejan, y dos partes 2 **contiguas** en la composición no pueden ir juntas (si no, no habría corte entre ellas). Lo calculo:


---
description: Contar la respuesta con enumeración estructural y verificar con fuerza bruta
command: mkdir -p /tmp/marbles && cat > /tmp/marbles/count.py << 'EOF'
from itertools import combinations
from functools import lru_cache

def comps(n):
    if n == 0: yield ()
    for p in (2,4):
        if n >= p:
            for rest in comps(n-p):
                yield (p,)+rest

def matchings_avoiding(m, forbidden):
    # perfect matchings on range(m) avoiding forbidden edges
    def rec(rem):
        if not rem: return 1
        a = rem[0]; tot = 0
        for b in rem[1:]:
            if (a,b) not in forbidden:
                tot += rec(tuple(x for x in rem[1:] if x != b))
        return tot
    return rec(tuple(range(m)))

def structural(n):
    total = 0
    for c in comps(n):
        twos = [i for i,p in enumerate(c) if p == 2]
        idx = {pos:j for j,pos in enumerate(twos)}
        forb = set()
        for a,b in zip(twos, twos[1:]):
            if b == a+1:  # contiguas en la composicion
                forb.add((idx[a], idx[b])); forb.add((idx[b], idx[a]))
        if len(twos) % 2: continue
        total += matchings_avoiding(len(twos), forb)
    return total

def ok(jar):
    s = set(jar)
    return all((x-1 in s) or (x+1 in s) for x in jar)

def brute(n):
    marbles = list(range(1, n+1))
    def rec(rem):
        if not rem: return 1
        first = rem[0]; tot = 0
        for rest in combinations(rem[1:], 3):
            jar = (first,)+rest
            if ok(jar):
                tot += rec(tuple(x for x in rem[1:] if x not in rest))
        return tot
    return rec(tuple(marbles))

for n in (4,8,12,16):
    print(n, "estructural:", structural(n), "fuerza bruta:", brute(n))
print("n=20 estructural:", structural(20))
EOF
python3 -I /tmp/marbles/count.py
description: Count partitions
---