**Paso 1:** La suma de los coeficientes de un polinomio $p(x)$ es igual a $p(1)$, porque al evaluar en $x=1$ cada término queda multiplicado por $1$.

**Paso 2:** Como $g(x) = f(x-1)$, evaluamos en $x=1$:
$$g(1) = f(1-1) = f(0)$$

**Paso 3:** Calculamos $f(0)$:
$$f(0) = 3(0)^4 + 5(0)^2 - 9(0) - 2 = -2$$

**Verificación (expansión directa):** Expandimos $g(x)$:
- $3(x-1)^4 = 3x^4 - 12x^3 + 18x^2 - 12x + 3$
- $5(x-1)^2 = 5x^2 - 10x + 5$
- $-9(x-1) = -9x + 9$
- Constante: $-2$

Sumando: $g(x) = 3x^4 - 12x^3 + 23x^2 - 31x + 15$.

Suma de coeficientes: $3 - 12 + 23 - 31 + 15 = -2$. ✓

\boxed{-2}