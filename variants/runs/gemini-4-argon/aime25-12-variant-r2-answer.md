Para encontrar el área de la región finita, primero reescribimos el sistema de desigualdades factorizando cada parte.

La primera desigualdad es:
$$x - yz < y - zx \iff x - y + zx - yz < 0 \iff (x - y)(z + 1) < 0$$

La segunda desigualdad es:
$$y - zx < z - xy \iff y - z + xy - zx < 0 \iff (y - z)(x + 1) < 0$$

Analizamos los posibles signos de los factores en el plano $x + y + z = 87$:

1. **Caso 1:** $x - y > 0$, $z + 1 < 0$ y $y - z > 0$, $x + 1 < 0$.
   Esto implica $z < y < x < -1$. Entonces $x + y + z < -3$, lo cual contradice que $x + y + z = 87$. No hay puntos en este caso.

2. **Caso 2:** $x - y > 0$, $z + 1 < 0$ y $y - z < 0$, $x + 1 > 0$.
   Esto equivale a $y < z < -1$ y $x > -1$ (con $x > y$, que se cumple automáticamente). Como $y$ y $z$ pueden tomar valores negativos arbitrariamente grandes en magnitud (con $x = 87 - y - z$), esta región no está acotada.

3. **Caso 3:** $x - y < 0$, $z + 1 > 0$ y $y - z > 0$, $x + 1 < 0$.
   Esto equivale a $x < -1$, $z > -1$ y $y > \max(x, z)$. Como $x$ puede ser arbitrariamente negativo, esta región tampoco está acotada.

4. **Caso 4:** $x - y < 0$, $z + 1 > 0$ y $y - z < 0$, $x + 1 > 0$.
   Esto equivale a:
   $$-1 < x < y < z$$
   Como $x + y + z = 87$ y las tres coordenadas son mayores que $-1$, todas están acotadas superiormente por $89$. Por lo tanto, esta es la única región convexa de área finita.

Hallamos los vértices del triángulo definido por $-1 \le x \le y \le z$ en el plano $x + y + z = 87$:
- Intersección de $x = -1$ y $x = y$: $V_1 = (-1, -1, 89)$.
- Intersección de $x = -1$ y $y = z$: $-1 + 2y = 87 \implies y = 44$, por lo que $V_2 = (-1, 44, 44)$.
- Intersección de $x = y$ y $y = z$: $3x = 87 \implies x = 29$, por lo que $V_3 = (29, 29, 29)$.

Calculamos los vectores de dos lados del triángulo a partir de $V_1$:
$$\vec{u} = V_2 - V_1 = (0, 45, -45)$$
$$\vec{v} = V_3 - V_1 = (30, 30, -60)$$

El área del triángulo es $\frac{1}{2} \|\vec{u} \times \vec{v}\|$:
$$\vec{u} \times \vec{v} = (45 \cdot 30) \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 1 & -1 \\ 1 & 1 & -2 \end{vmatrix} = 1350(-1, -1, -1)$$

Por lo tanto, el área es:
$$\text{Área} = \frac{1}{2} \|(-1350, -1350, -1350)\| = \frac{1}{2} \cdot 1350\sqrt{1^2 + 1^2 + 1^2} = 675\sqrt{3}$$

Identificando $a = 675$ y $b = 3$, obtenemos $a + b = 675 + 3 = 678$.

\boxed{678}