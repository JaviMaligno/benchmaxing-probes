## Planteamiento

Numeremos los vértices $0,1,\dots,23$. Dos vértices $i,j$ determinan un segmento cuya longitud depende solo del "paso" $k=|i-j| \bmod 24$, con $1\le k\le 12$. Como los 12 segmentos deben tener la misma longitud, todos usan el mismo $k$, y debemos contar los emparejamientos perfectos del grafo circulante $C_{24}(k)$, donde $i \sim i+k$.

## Estructura del grafo

Si $d=\gcd(k,24)$, el grafo se descompone en $d$ ciclos disjuntos de longitud $24/d$ cada uno.

- Un ciclo de longitud par $m\ge 4$ tiene exactamente $2$ emparejamientos perfectos.
- Un ciclo de longitud impar tiene $0$.
- El caso $k=12$ es especial: cada componente es una sola arista, con $1$ emparejamiento.

Por tanto, para $k\ne 12$ el total es $2^d$ si $24/d$ es par, y $0$ si es impar.

## Conteo por cada $k$

| $k$ | $d=\gcd(k,24)$ | $24/d$ | emparejamientos |
|---|---|---|---|
| 1 | 1 | 24 | $2$ |
| 2 | 2 | 12 | $4$ |
| 3 | 3 | 8 | $8$ |
| 4 | 4 | 6 | $16$ |
| 5 | 1 | 24 | $2$ |
| 6 | 6 | 4 | $64$ |
| 7 | 1 | 24 | $2$ |
| 8 | 8 | 3 (impar) | $0$ |
| 9 | 3 | 8 | $8$ |
| 10 | 2 | 12 | $4$ |
| 11 | 1 | 24 | $2$ |
| 12 | 12 | 2 | $1$ |

## Suma

$$2+4+8+16+2+64+2+0+8+4+2+1 = 113$$

\boxed{113}