## Planteamiento

Etiquetamos los vértices $0, 1, \dots, 23$. Dos vértices determinan una cuerda cuya longitud depende solo de la "separación" $k = $ diferencia módulo 24, con $k \in \{1, 2, \dots, 12\}$. Como los 12 segmentos deben tener la misma longitud, fijamos un $k$ y contamos los emparejamientos perfectos usando solo cuerdas de separación $k$; luego sumamos sobre $k$.

## Estructura para cada $k$

Para $k$ fijo, el grafo con aristas $\{i, i+k \bmod 24\}$ se descompone en $d = \gcd(24, k)$ ciclos disjuntos, cada uno de longitud $24/d$.

- Un ciclo de longitud **par** tiene exactamente $2$ emparejamientos perfectos, así que el total es $2^d$.
- Un ciclo de longitud **impar** no tiene ninguno.
- Caso especial $k = 12$: cada vértice se une a su diametralmente opuesto, formando 12 aristas fijas; hay exactamente $1$ manera.

## Cálculo por cada $k$

| $k$ | $d=\gcd(24,k)$ | longitud del ciclo | conteo |
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
| 12 | — | diámetros | $1$ |

## Suma total

$$2 + 4 + 8 + 16 + 2 + 64 + 2 + 0 + 8 + 4 + 2 + 1 = 113$$

$$\boxed{113}$$