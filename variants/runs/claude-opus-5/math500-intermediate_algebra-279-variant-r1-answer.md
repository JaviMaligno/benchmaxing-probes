## Factorización

**Paso 1.** Es cuadrática en $x^4$:
$$x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64).$$

**Paso 2.** Factorizamos $x^4 - 1$:
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1),$$
donde $x^2+1$ es irreducible sobre $\mathbb{Z}$.

**Paso 3.** Factorizamos $x^4 + 64$ completando cuadrado (identidad de Sophie Germain):
$$x^4 + 64 = (x^2+8)^2 - 16x^2 = (x^2 - 4x + 8)(x^2 + 4x + 8).$$
Ambos factores tienen discriminante $16 - 32 = -16 < 0$, así que son irreducibles sobre $\mathbb{Z}$.

**Paso 4.** Evaluamos en $x = 1$:

| Factor | Valor en $1$ |
|---|---|
| $x-1$ | $0$ |
| $x+1$ | $2$ |
| $x^2+1$ | $2$ |
| $x^2-4x+8$ | $5$ |
| $x^2+4x+8$ | $13$ |

Suma: $0 + 2 + 2 + 5 + 13 = 22$.

(Verificación: el producto $0\cdot 2\cdot 2\cdot 5\cdot 13 = 0$ coincide con $1 + 63 - 64 = 0$.)

\boxed{22}