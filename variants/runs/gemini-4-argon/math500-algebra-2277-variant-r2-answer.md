Para calcular $g^{-1}(0) + g^{-1}(12)$, debemos encontrar los valores de $x$ tales que $g(x) = 0$ y $g(x) = 12$ respectivamente, verificando que cumplan con las condiciones de dominio de cada tramo de la función.

**Paso 1: Calcular $g^{-1}(0)$**

Buscamos $x$ tal que $g(x) = 0$. Analizamos ambos casos de la función definida a trozos:

* **Caso 1 ($x \leq 4$):**
  $$4 - x = 0 \implies x = 4$$
  Como $4 \leq 4$, esta solución es válida.

* **Caso 2 ($x > 4$):**
  $$-x^3 + 3x^2 + 4x = 0$$
  Factorizando:
  $$-x(x^2 - 3x - 4) = 0 \implies -x(x - 4)(x + 1) = 0$$
  Las soluciones son $x = 0$, $x = 4$ y $x = -1$. Ninguna de ellas cumple la condición $x > 4$, por lo que se descartan.

Por lo tanto, $g^{-1}(0) = 4$.

---

**Paso 2: Calcular $g^{-1}(12)$**

Buscamos $x$ tal que $g(x) = 12$. Analizamos nuevamente ambos casos:

* **Caso 1 ($x \leq 4$):**
  $$4 - x = 12 \implies x = -8$$
  Como $-8 \leq 4$, esta solución es válida.

* **Caso 2 ($x > 4$):**
  $$-x^3 + 3x^2 + 4x = 12 \implies x^3 - 3x^2 - 4x + 12 = 0$$
  Factorizando por agrupación:
  $$x^2(x - 3) - 4(x - 3) = 0 \implies (x^2 - 4)(x - 3) = 0 \implies (x - 2)(x + 2)(x - 3) = 0$$
  Las soluciones son $x = 2$, $x = -2$ y $x = 3$. Ninguna de ellas cumple la condición $x > 4$, por lo que también se descartan.

Por lo tanto, $g^{-1}(12) = -8$.

---

**Paso 3: Sumar ambos resultados**

$$g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4$$

\boxed{-4}