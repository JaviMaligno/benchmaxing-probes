## Planteamiento

Numeremos los vértices $0,1,\dots,27$ en $\mathbb{Z}_{28}$. Dos vértices determinan un segmento cuya longitud depende solo de la "diferencia" $k$, con $1\le k\le 14$. Hay exactamente 14 longitudes distintas.

Fijada una longitud $k$, los segmentos disponibles forman el grafo con aristas $\{i,\,i+k\}$. Este grafo se descompone en $d=\gcd(28,k)$ ciclos de longitud $L=28/d$ (para $k=14$ cada "ciclo" degenera en una sola arista).

Un ciclo de longitud par $L$ tiene exactamente 2 emparejamientos perfectos; si $L$ es impar, no tiene ninguno.

## Conteo por longitud

| $k$ | $d=\gcd(28,k)$ | $L=28/d$ | emparejamientos |
|---|---|---|---|
| 1,3,5,9,11,13 | 1 | 28 (par) | $2$ cada uno |
| 2,6,10 | 2 | 14 (par) | $2^2=4$ cada uno |
| 4,8,12 | 4 | 7 (impar) | $0$ |
| 7 | 7 | 4 (par) | $2^7=128$ |
| 14 | 14 | 2 (diámetros) | $1$ |

## Suma

$$6\cdot 2 \;+\; 3\cdot 4 \;+\; 0 \;+\; 128 \;+\; 1 \;=\; 12+12+128+1 = 153$$

Como longitudes distintas dan configuraciones distintas, no hay repeticiones.

\boxed{153}