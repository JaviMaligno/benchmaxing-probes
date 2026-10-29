## Planteamiento

Numeramos los vértices $0,1,\dots,27$. Dos vértices determinan un segmento cuya longitud depende solo del "paso" $k=1,\dots,14$ (distancia mínima a lo largo del polígono). Pasos distintos dan longitudes distintas, así que basta contar, para cada $k$, los emparejamientos perfectos del grafo circulante $G_k$ con aristas $\{i,\ i+k \bmod 28\}$, y sumar.

## Estructura de $G_k$

Para $k<14$, con $d=\gcd(k,28)$, el grafo $G_k$ se descompone en $d$ ciclos disjuntos, cada uno de longitud $L=28/d$.

- Si $L$ es impar, un ciclo no admite emparejamiento perfecto → 0 configuraciones.
- Si $L$ es par, cada ciclo admite exactamente 2 emparejamientos → $2^{d}$ en total.

Para $k=14$ las aristas $\{i,i+14\}$ ya son 14 segmentos disjuntos: exactamente **1** configuración.

## Conteo por $k$

| $k$ | $d=\gcd(k,28)$ | $L=28/d$ | conteo |
|---|---|---|---|
| 1,3,5,9,11,13 | 1 | 28 (par) | $2$ cada uno |
| 2,6,10 | 2 | 14 (par) | $4$ cada uno |
| 4,8,12 | 4 | 7 (impar) | $0$ |
| 7 | 7 | 4 (par) | $2^7=128$ |
| 14 | — | — | $1$ |

## Suma

$$6\cdot 2 \;+\; 3\cdot 4 \;+\; 3\cdot 0 \;+\; 128 \;+\; 1 \;=\; 12+12+0+128+1 = 153$$

\boxed{153}