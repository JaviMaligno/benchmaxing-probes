Para calcular $f^{-1}(0) + f^{-1}(6)$, debemos encontrar los valores de $x$ tales que $f(x) = 0$ y $f(x) = 6$, asegurándonos de que cada solución cumpla con la condición del intervalo correspondiente en la función definida a trozos.

**Paso 1: Calcular $f^{-1}(0)$**
Buscamos $x$ tal que $f(x) = 0$. Analizamos ambos casos:
1. Si $x \leq 3$:
   $$3 - x = 0 \implies x = 3$$
   Como $3 \leq 3$, esta solución es válida.

2. Si $x > 3$:
   $$-x^3 + 2x^2 + 3x = 0 \implies -x(x^2 - 2x - 3) = 0 \implies -x(x - 3)(x + 1) = 0$$
   Las soluciones son $x = 0$, $x = 3$ y $x = -1$. Ninguna de ellas cumple con $x > 3$.

Por lo tanto, $f^{-1}(0) = 3$.

---

**Paso 2: Calcular $f^{-1}(6)$**
Buscamos $x$ tal que $f(x) = 6$. Analizamos ambos casos:
1. Si $x \leq 3$:
   $$3 - x = 6 \implies x = -3$$
   Como $-3 \leq 3$, esta solución es válida.

2. Si $x > 3$:
   $$-x^3 + 2x^2 + 3x = 6 \implies x^3 - 2x^2 - 3x + 6 = 0$$
   Factorizando por agrupación:
   $$x^2(x - 2) - 3(x - 2) = 0 \implies (x^2 - 3)(x - 2) = 0$$
   Las soluciones son $x = 2$, $x = \sqrt{3}$ y $x = -\sqrt{3}$. Ninguna de ellas es mayor que $3$.

Por lo tanto, $f^{-1}(6) = -3$.

---

**Paso 3: Sumar ambos resultados**
$$f^{-1}(0) + f^{-1}(6) = 3 + (-3) = 0$$

\boxed{0}