## Factorización

Con la sustitución $u = x^4$:

$$x^8 + 3x^4 - 4 = u^2 + 3u - 4 = (u-1)(u+4) = (x^4 - 1)(x^4 + 4).$$

**Factorizamos cada parte:**

- $x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x-1)(x+1)(x^2+1)$
- $x^4 + 4$: identidad de Sophie Germain ($a^4 + 4b^4$):
$$x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2).$$

(Chequeo: los términos cruzados se cancelan y queda $x^4 + 2x^2 \cdot 2 - 4x^2 + 4 = x^4 + 4$.) ✓

**Irreducibilidad sobre $\mathbb{Z}$:**
- $x-1$ y $x+1$: lineales, irreducibles.
- $x^2 + 1$: raíces $\pm i$, no racionales.
- $x^2 \pm 2x + 2$: discriminante $4 - 8 = -4 < 0$, sin raíces racionales.

Como $\mathbb{Z}[x]$ es un UFD (lema de Gauss) y todos los factores son mónicos, la factorización es única:

$$x^8 + 3x^4 - 4 = (x-1)(x+1)(x^2+1)(x^2-2x+2)(x^2+2x+2).$$

(Producto de términos independientes: $(-1)(1)(1)(2)(2) = -4$.) ✓

## Evaluación en $x = 1$

| Factor | $p_i(1)$ |
|---|---|
| $x - 1$ | $0$ |
| $x + 1$ | $2$ |
| $x^2 + 1$ | $2$ |
| $x^2 - 2x + 2$ | $1$ |
| $x^2 + 2x + 2$ | $5$ |

$$0 + 2 + 2 + 1 + 5 = \boxed{10}$$