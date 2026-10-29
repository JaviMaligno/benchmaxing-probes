Para encontrar el área de la región finita, primero reescribimos la cadena de desigualdades dada:
$$x - yz < y - zx < z - xy$$

Analizamos la primera desigualdad:
$$x - yz < y - zx \iff x - y + zx - yz < 0 \iff (x - y)(z + 1) < 0$$

Analizamos la segunda desigualdad:
$$y - zx < z - xy \iff y - z + xy - zx < 0 \iff (y - z)(x + 1) < 0$$

Por lo tanto, el sistema de desigualdades equivale a:
1. $(x - y)(z + 1) < 0$
2. $(y - z)(x + 1) < 0$

Cada desigualdad se cumple en dos casos posibles según los signos de sus factores:
- De (1), tenemos:
  - Caso A: $x < y$ y $z > -1$
  - Caso B: $x > y$ y $z < -1$
- De (2), tenemos:
  - Caso C: $y < z$ y $x > -1$
  - Caso D: $y > z$ y $x < -1$

Al combinar estos casos en el plano $x + y + z = 87$, obtenemos cuatro combinaciones:
1. **A y C:** $x < y$, $z > -1$, $y < z$ y $x > -1$. Esto se resume en $-1 < x < y < z$. Como $x + y + z = 87$, todas las coordenadas están acotadas inferior y superiormente, por lo que esta región es un triángulo acotado (de área finita).
2. **A y D:** $x < -1$ y $y > z > -1$. Aquí $x$ puede tomar valores arbitrariamente negativos mientras $y$ crece indefinidamente, dando una región no acotada.
3. **B y C:** $x > -1$ y $y < z < -1$. Aquí $y, z$ pueden ser arbitrariamente negativos mientras $x$ crece indefinidamente, dando otra región no acotada.
4. **B y D:** $-1 > x > y > z$, lo cual implica $x + y + z < -3$, imposible en el plano $x + y + z = 87$ (conjunto vacío).

La única región de área finita está definida en el plano $x + y + z = 87$ por las desigualdades:
$$-1 < x < y < z$$

Sus vértices se obtienen al intersecar las rectas frontera $x = -1$, $x = y$ y $y = z$ en el plano $x + y + z = 87$:
- **Vértice $V_1$ ($x = -1$ y $x = y$):** $x = -1, y = -1 \implies z = 87 - (-1) - (-1) = 89$.
  $$V_1 = (-1, -1, 89)$$
- **Vértice $V_2$ ($x = -1$ y $y = z$):** $x = -1, 2y = 88 \implies y = 44, z = 44$.
  $$V_2 = (-1, 44, 44)$$
- **Vértice $V_3$ ($x = y$ y $y = z$):** $3x = 87 \implies x = y = z = 29$.
  $$V_3 = (29, 29, 29)$$

Calculamos los vectores que forman dos lados del triángulo desde $V_1$:
$$\vec{u} = V_2 - V_1 = (0, 45, -45) = 45(0, 1, -1)$$
$$\vec{v} = V_3 - V_1 = (30, 30, -60) = 30(1, 1, -2)$$

El área del triángulo viene dada por $\frac{1}{2} \|\vec{u} \times \vec{v}\|$:
$$\vec{u} \times \vec{v} = 45 \cdot 30 \cdot \big((0, 1, -1) \times (1, 1, -2)\big) = 1350(-1, -1, -1)$$

Por lo tanto, el área es:
$$\text{Área} = \frac{1}{2} \cdot 1350 \sqrt{(-1)^2 + (-1)^2 + (-1)^2} = 675\sqrt{3}$$

Identificando con la forma $a\sqrt{b}$, tenemos $a = 675$ y $b = 3$, por lo que $a + b = 675 + 3 = 678$.

\boxed{678}