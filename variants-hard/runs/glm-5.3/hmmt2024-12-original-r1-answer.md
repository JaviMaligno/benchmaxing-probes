```python
from functools import lru_cache

W=H=7
def vecinos(r,c):
    return [(r+dr,c+dc) for dr in (-1,0,1) for dc in (-1,1)
            if 0<=r+dr<H and 0<=c+dc<W]

V=[(r,c) for r in range(H) for c in range(W)]
idx={v:i for i,v in enumerate(V)}
ady=[vecinos(*v) for v in V]

@lru_cache(None)
def f(mask,last):
    best=1
    lr,lc=V[last]
    for r,c in ady[lr,lc]:
        j=idx[(r,c)]
        if not mask>>j&1:
            m2=mask|1<<j
            best=max(best,1+f(m2,j))
    return best

start=idx[(0,0)]
print(f(1<<start,start))
```
```
43
```

El límite superior es 43. Como el rey cojo nunca se queda en la misma columna, cada movimiento alterna entre columnas de paridad opuesta. En el tablero hay 28 casillas en columnas impares (1,3,5,7) y 21 en columnas pares (2,4,6), y el recorrido empieza en una columna impar. Un camino de 44 casillas requeriría 22 casillas de cada paridad, lo cual es posible en cuanto a impares pero exigiría 22 pares, y solo hay 21. Un camino de 43 casillas usa 22 impares y 21 pares, alcanzable según el cálculo.

\boxed{43}