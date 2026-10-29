## Razonamiento

Como se reparten las 48 cartas completas, debe cumplirse $xy = 48$, es decir, $x$ es un divisor de 48.

**Divisores de 48:** 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.

**Condiciones:**
- $x \geq 3$
- $y \geq 4 \Rightarrow \dfrac{48}{x} \geq 4 \Rightarrow x \leq 12$

Por tanto hay que contar los divisores de 48 en el intervalo $3 \leq x \leq 12$:

| $x$ | $y = 48/x$ |
|---|---|
| 3 | 16 |
| 4 | 12 |
| 6 | 8 |
| 8 | 6 |
| 12 | 4 |

Son 5 valores (se descartan 1 y 2 por ser menores que 3; y 16, 24, 48 porque darían $y < 4$).

\boxed{5}