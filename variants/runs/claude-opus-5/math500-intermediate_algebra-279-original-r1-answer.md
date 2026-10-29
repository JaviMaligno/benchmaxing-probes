## Factorización

**Paso 1.** Tratando la expresión como cuadrática en $x^4$:
$$x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1).$$

**Paso 2.** El segundo factor:
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1).$$

**Paso 3.** El primero, por identidad de Sophie Germain ($x^4+4 = (x^2+2)^2 - (2x)^2$):
$$x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2).$$

Ambos son irreducibles sobre $\mathbb{Z}$ (discriminante negativo), igual que $x^2+1$.

**Paso 4.** Evaluación en $x=1$:

| $p_i(x)$ | $p_i(1)$ |
|---|---|
| $x-1$ | $0$ |
| $x+1$ | $2$ |
| $x^2+1$ | $2$ |
| $x^2-2x+2$ | $1$ |
| $x^2+2x+2$ | $5$ |

Suma: $0 + 2 + 2 + 1 + 5 = 10$.

\boxed{10}