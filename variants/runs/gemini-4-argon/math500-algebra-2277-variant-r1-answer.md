Para calcular $g^{-1}(0) + g^{-1}(12)$, debemos encontrar los valores de $x$ tales que $g(x) = 0$ y $g(x) = 12$ respectivamente, verificando cada tramo de la función definida a trozos.

**Paso 1: Calcular $g^{-1}(0)$**
Buscamos $x$ tal que $g(x) = 0$.

- **Caso 1 ($x \leq 4$):**
  $$4 - x = 0 \implies x = 4$$
  Como $4 \leq 4$, esta solución es válida.

- **Caso 2 ($x > 4$):**
  $$-x^3 + 3x^2 + 4x = 0 \implies -x(x^2 - 3x - 4) = 0 \implies -x(x - 4)(x + 1) = 0$$
  Las soluciones son $x = 0$, $x = 4$ y $x = -1$. Ninguna de ellas cumple la condición $x > 4$.

Por lo tanto, $g^{-1}(0) = 4$.

---

**Paso 2: Calcular $g^{-1}(12)$**
Buscamos $x$ tal que $g(x) = 12$.

- **Caso 1 ($x \leq 4$):**
  $$4 - x = 12 \implies x = -8$$
  Como $-8 \leq 4$, esta solución es válida.

- **Caso 2 ($x > 4$):**
  Para $x > 4$, podemos factorizar la expresión como $-x(x - 4)(x + 1)$. Dado que $x > 4$, los tres factores $x$, $(x - 4)$ y $(x + 1)$ son positivos, por lo que $-x(x - 4)(x + 1) < 0$. Así, nunca puede ser igual a $12$ en este intervalo.

Por lo tanto, $g^{-1}(12) = -8$.

---

**Paso 3: Sumar ambos resultados**
$$g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4$$

\boxed{-4}