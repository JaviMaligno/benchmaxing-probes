## Planteamiento

Numeremos los vértices $0,1,\dots,23$. Dos vértices a distancia angular $d$ (con $1\le d\le 12$) determinan segmentos de la misma longitud, y longitudes distintas para $d$ distintos. Por tanto hay que contar, para cada $d$, los emparejamientos perfectos del grafo circulante $G_d$ donde $i \sim i+d \pmod{24}$.

## Estructura de $G_d$

Si $g=\gcd(d,24)$, el grafo $G_d$ se descompone en $g$ ciclos disjuntos de longitud $24/g$ (para $d=12$ los "ciclos" degeneran en 12 aristas simples).

- Un ciclo de longitud par $2k\ (k\ge 2)$ tiene exactamente **2** emparejamientos perfectos.
- Un ciclo de longitud impar tiene **0**.
- Una arista simple ($d=12$) aporta **1**.

## Conteo por $d$

| $d$ | $g$ | long. ciclo | nº ciclos | emparejamientos |
|---|---|---|---|---|
| 1 | 1 | 24 | 1 | $2^1=2$ |
| 2 | 2 | 12 | 2 | $2^2=4$ |
| 3 | 3 | 8 | 3 | $2^3=8$ |
| 4 | 4 | 6 | 4 | $2^4=16$ |
| 5 | 1 | 24 | 1 | $2$ |
| 6 | 6 | 4 | 6 | $2^6=64$ |
| 7 | 1 | 24 | 1 | $2$ |
| 8 | 8 | 3 (impar) | 8 | $0$ |
| 9 | 3 | 8 | 3 | $8$ |
| 10 | 2 | 12 | 2 | $4$ |
| 11 | 1 | 24 | 1 | $2$ |
| 12 | 12 | 2 | 12 | $1$ |

## Suma

$$2+4+8+16+2+64+2+0+8+4+2+1 = 113$$

\boxed{113}