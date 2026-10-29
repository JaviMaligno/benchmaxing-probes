## Factorización

**Paso 1.** Buscamos dos factores cuyo producto dé los coeficientes $63$ y $-64$:
$$x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64)$$
Verificación: $x^8 + 64x^4 - x^4 - 64 = x^8 + 63x^4 - 64$. ✓

**Paso 2.** Factorizamos $x^4 - 1$:
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$$
donde $x^2+1$ es irreducible sobre $\mathbb{Z}$.

**Paso 3.** Factorizamos $x^4 + 64$ completando cuadrado (identidad de Sophie Germain):
$$x^4 + 64 = (x^2+8)^2 - 16x^2 = (x^2 - 4x + 8)(x^2 + 4x + 8)$$
Ambos factores tienen discriminante $16 - 32 = -16 < 0$, luego no tienen raíces reales y son irreducibles sobre $\mathbb{Z}$.

**Factorización completa:**
$$x^8 + 63x^4 - 64 = (x-1)(x+1)(x^2+1)(x^2-4x+8)(x^2+4x+8)$$

**Paso 4.** Evaluamos en $x = 1$:

| $q_i(x)$ | $q_i(1)$ |
|---|---|
| $x-1$ | $0$ |
| $x+1$ | $2$ |
| $x^2+1$ | $2$ |
| $x^2-4x+8$ | $5$ |
| $x^2+4x+8$ | $13$ |

Suma: $0 + 2 + 2 + 5 + 13 = 22$.

(Comprobación del producto: $0 \cdot 2 \cdot 2 \cdot 5 \cdot 13 = 0 = 1 + 63 - 64$. ✓)

\boxed{22}