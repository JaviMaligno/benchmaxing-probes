## Planteamiento

Un número de 8 cifras usando 1–8 exactamente una vez es divisible por 22 = 2 · 11 si y solo si es divisible por 2 y por 11.

**Divisibilidad por 2:** la última cifra (posición 8) debe ser par: 2, 4, 6 u 8.

**Divisibilidad por 11:** la suma alternada de las cifras debe ser múltiplo de 11. Sea $S$ la suma de las cifras en las posiciones impares (1, 3, 5, 7). Como la suma total es $1+2+\cdots+8 = 36$, la diferencia es:
$$S - (36 - S) = 2S - 36 \equiv 0 \pmod{11}.$$
Como $10 \le S \le 26$, se tiene $-16 \le 2S-36 \le 16$, y siendo $2S-36$ par, el único múltiplo de 11 posible es $0$. Entonces $S = 18$.

## Conteo de subconjuntos con suma 18

Necesito elegir 4 cifras (para las posiciones impares) que sumen 18. Enumerando $\{a<b<c<d\}$:

- $a=1$: $\{1,2,7,8\},\ \{1,3,6,8\},\ \{1,4,5,8\},\ \{1,4,6,7\}$
- $a=2$: $\{2,3,5,8\},\ \{2,3,6,7\},\ \{2,4,5,7\}$
- $a=3$: $\{3,4,5,6\}$

Son **8 subconjuntos**.

## Conteo de arreglos por subconjunto

Para cada subconjunto $A$ en las posiciones impares hay $4! = 24$ arreglos. El complemento $B$ ocupa las posiciones pares (2, 4, 6, 8), y la posición 8 debe ser par. Verificando cada caso:

| $A$ (impares) | $B$ (pares) | cifras pares en $B$ |
|---|---|---|
| {1,2,7,8} | {3,4,5,6} | 2 |
| {1,3,6,8} | {2,4,5,7} | 2 |
| {1,4,5,8} | {2,3,6,7} | 2 |
| {1,4,6,7} | {2,3,5,8} | 2 |
| {2,3,5,8} | {1,4,6,7} | 2 |
| {2,3,6,7} | {1,4,5,8} | 2 |
| {2,4,5,7} | {1,3,6,8} | 2 |
| {3,4,5,6} | {1,2,7,8} | 2 |

En todos los casos $B$ contiene exactamente 2 cifras pares, así que los arreglos de $B$ con la posición 8 par son $2 \cdot 3! = 12$.

## Resultado

$$N = 8 \cdot 24 \cdot 12 = 2304,$$

y la diferencia pedida es:
$$N - 2025 = 2304 - 2025 = 279.$$

$$\boxed{279}$$