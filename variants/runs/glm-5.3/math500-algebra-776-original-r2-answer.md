# Solución

**Paso 1: Comprender la relación entre g y f**

Dado que $g(x) = f(x-1)$, podemos evaluar $g$ en cualquier punto usando $f$. En particular:
$$g(x) = f(x-1)$$

**Paso 2: La suma de coeficientes es $g(1)$**

Un hecho clave: la suma de los coeficientes de cualquier polinomio $g(x)$ es igual a $g(1)$, porque al sustituir $x=1$, todas las potencias valen $1$ y solo quedan los coeficientes.

**Paso 3: Evaluar**

$$g(1) = f(1-1) = f(0)$$

Ahora calculamos $f(0)$:
$$f(0) = 3(0)^4 + 5(0)^2 - 9(0) - 2 = -2$$

**Verificación por expansión directa:**

Expandiendo $f(x-1) = 3(x-1)^4 + 5(x-1)^2 - 9(x-1) - 2$:
- $3(x-1)^4 = 3x^4 - 12x^3 + 18x^2 - 12x + 3$
- $5(x-1)^2 = 5x^2 - 10x + 5$
- $-9(x-1) = -9x + 9$
- $-2$

Sumando coeficientes por grado:
- Grado 4: $3$
- Grado 3: $-12$
- Grado 2: $18 + 5 = 23$
- Grado 1: $-12 - 10 - 9 = -31$
- Grado 0: $3 + 5 + 9 - 2 = 15$

Total: $3 - 12 + 23 - 31 + 15 = -2$ ✓

La suma de los coeficientes de $g$ es $\boxed{-2}$.