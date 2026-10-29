## Planteamiento

Numeramos los vértices $0,1,\dots,27$ en el círculo. La longitud de un segmento entre dos vértices depende solo de la distancia cíclica $k$ entre ellos, con $k \in \{1,2,\dots,14\}$ (donde $k=14$ corresponde a los diámetros). Como los 14 segmentos deben tener la misma longitud, fijamos $k$ y contamos los emparejamientos perfectos del grafo con aristas $\{i,\, i+k \pmod{28}\}$.

**Estructura:** Sea $d = \gcd(k,28)$. La permutación $i \mapsto i+k$ sobre $\mathbb{Z}_{28}$ tiene $d$ ciclos, cada uno de longitud $L = 28/d$, y las aristas de cada ciclo forman un grafo ciclo $C_L$. El número total de emparejamientos es el producto sobre los $d$ ciclos:
- $L$ impar $\Rightarrow$ $0$ emparejamientos,
- $L = 2$ $\Rightarrow$ $1$ emparejamiento (la arista misma),
- $L$ par, $L \ge 4$ $\Rightarrow$ exactamente $2$ emparejamientos por ciclo.

## Cálculo para cada $k$

| $k$ | $d=\gcd(k,28)$ | $L=28/d$ | Ciclos | Formas |
|---|---|---|---|---|
| 1, 3, 5, 9, 11, 13 | 1 | 28 | 1 | $2$ cada uno → $6\cdot 2 = 12$ |
| 2, 6, 10 | 2 | 14 | 2 | $2^2 = 4$ cada uno → $3\cdot 4 = 12$ |
| 4, 8, 12 | 4 | 7 (impar) | — | $0$ |
| 7 | 7 | 4 | 7 | $2^7 = 128$ |
| 14 | 14 | 2 | 14 | $1$ (los diámetros) |

## Suma total

$$12 + 12 + 128 + 1 = 153$$

(Verificación rápida: los casos $k=1,3,5,9,11,13$ dan $2$; $k=2,6,10$ dan $4$; $k=7$ da $128$; $k=14$ da $1$; los $k$ múltiplos de 4 dan $0$ por ciclos impares.)

$$\boxed{153}$$