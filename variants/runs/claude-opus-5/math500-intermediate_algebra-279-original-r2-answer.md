## Factorización

Tratando la expresión como cuadrática en $x^4$:
$$x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$$

**Factor $x^4 - 1$:**
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$$

**Factor $x^4 + 4$** (identidad de Sophie Germain):
$$x^4 + 4 = (x^2+2)^2 - 4x^2 = (x^2 - 2x + 2)(x^2 + 2x + 2)$$

Todos los factores cuadráticos son irreducibles sobre $\mathbb{Z}$ (discriminantes $-4$, $-4$, $-4$), así que la factorización completa es:
$$(x-1)(x+1)(x^2+1)(x^2-2x+2)(x^2+2x+2)$$

## Evaluación en $x = 1$

| $p_i(x)$ | $p_i(1)$ |
|---|---|
| $x-1$ | $0$ |
| $x+1$ | $2$ |
| $x^2+1$ | $2$ |
| $x^2-2x+2$ | $1$ |
| $x^2+2x+2$ | $5$ |

Suma: $0 + 2 + 2 + 1 + 5 = 10$

\boxed{10}