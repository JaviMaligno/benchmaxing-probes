Para hallar el área de la región finita, primero factorizamos las desigualdades dadas.

La primera desigualdad es:
$$x - yz < y - zx \iff x - y + zx - yz < 0 \iff (x - y)(z + 1) < 0$$

La segunda desigualdad es:
$$y - zx < z - xy \iff y - z + xy - zx < 0 \iff (y - z)(x + 1) < 0$$

Por lo tanto, los puntos de la región deben satisfacer el sistema:
1. $(x - y)(z + 1) < 0$
2. $(y - z)(x + 1) < 0$
3. $x + y + z = 75$

Cada una de las dos desigualdades se cumple cuando sus factores tienen signos opuestos, lo que da lugar a $2 \times 2 = 4$ casos posibles:

- **Caso 1:** $z + 1 > 0 \implies x < y$, y $x + 1 > 0 \implies y < z$.
  Esto nos da la cadena de desigualdades $-1 < x < y < z$. Como $x + y + z = 75$, todas las variables están acotadas (por ejemplo, $-1 < x < 25$ y $25 < z < 77$). Por lo tanto, esta región es **finita**.

- **Caso 2:** $z + 1 < 0 \implies x > y$, y $x + 1 > 0 \implies y < z$.
  Aquí $y < z < -1$ y $x > -1$. Como $x + y + z = 75$, podemos hacer que $y, z \to -\infty$ mientras $x \to +\infty$, por lo que la región es no acotada.

- **Caso 3:** $z + 1 > 0 \implies x < y$, y $x + 1 < 0 \implies y > z$.
  Aquí $x < -1 < z < y$. Podemos hacer que $x \to -\infty$ mientras $y \to +\infty$, por lo que también es no acotada.

- **Caso 4:** $z + 1 < 0 \implies x > y$, y $x + 1 < 0 \implies y > z$.
  Esto implica $z < y < x < -1$, por lo que $x + y + z < -3$, lo cual es imposible en el plano $x + y + z = 75$ (conjunto vacío).

La única región de área finita corresponde al **Caso 1**, que es el interior de un triángulo en el plano $x + y + z = 75$ delimitado por los planos $x = -1$, $x = y$ e $y = z$.

Hallamos los vértices de este triángulo intersectando los planos dos a dos junto con $x + y + z = 75$:

1. Intersección de $x = -1$ y $x = y$:
   $$x = -1, \quad y = -1 \implies z = 75 - (-1) - (-1) = 77 \implies A = (-1, -1, 77)$$

2. Intersección de $x = -1$ e $y = z$:
   $$x = -1, \quad 2y = 76 \implies y = 38, \quad z = 38 \implies B = (-1, 38, 38)$$

3. Intersección de $x = y$ e $y = z$:
   $$x = y = z \implies 3x = 75 \implies x = 25 \implies C = (25, 25, 25)$$

Calculamos los vectores de dos lados del triángulo a partir del vértice $A$:
$$\overrightarrow{AB} = B - A = (0, 39, -39) = 39(0, 1, -1)$$
$$\overrightarrow{AC} = C - A = (26, 26, -52) = 26(1, 1, -2)$$

El área del triángulo $ABC$ viene dada por $\frac{1}{2} \left\| \overrightarrow{AB} \times \overrightarrow{AC} \right\|$:
$$\overrightarrow{AB} \times \overrightarrow{AC} = (39 \cdot 26) \big((0, 1, -1) \times (1, 1, -2)\big) = 1014(-1, -1, -1)$$

Calculamos el área:
$$\text{Área} = \frac{1}{2} \cdot 1014 \left\|(-1, -1, -1)\right\| = 507\sqrt{(-1)^2 + (-1)^2 + (-1)^2} = 507\sqrt{3}$$

De la expresión $a\sqrt{b}$ tenemos que $a = 507$ y $b = 3$. Por lo tanto, $a + b = 507 + 3 = 510$.

\boxed{510}