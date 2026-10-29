Para hallar el área de un paralelogramo limitado por las rectas $y = ax + c_1$, $y = ax + c_2$, $y = bx + d_1$ y $y = bx + d_2$, podemos realizar el cambio de variables $u = y - ax$ y $v = y - bx$. 

El jacobiano de esta transformación con respecto a $(x, y)$ es:
$$\left|\det \begin{pmatrix} -a & 1 \\ -b & 1 \end{pmatrix}\right| = |b - a| = |a - b|$$

Por lo tanto, el área del paralelogramo en el plano $(x, y)$ viene dada por:
$$\text{Área} = \frac{|c_1 - c_2| \cdot |d_1 - d_2|}{|a - b|}$$

**Paso 1: Plantear las ecuaciones de las áreas**

Para el primer paralelogramo, limitado por $y=ax+c$, $y=ax+d$, $y=bx+c$ y $y=bx+d$, el área es $18$:
$$\frac{|c - d| \cdot |c - d|}{|a - b|} = \frac{(c - d)^2}{|a - b|} = 18$$

Para el segundo paralelogramo, limitado por $y=ax+c$, $y=ax-d$, $y=bx+c$ y $y=bx-d$, el área es $72$:
$$\frac{|c - (-d)| \cdot |c - (-d)|}{|a - b|} = \frac{(c + d)^2}{|a - b|} = 72$$

**Paso 2: Relacionar $c$ y $d$**

Dividiendo la segunda ecuación entre la primera, obtenemos:
$$\frac{(c + d)^2}{(c - d)^2} = \frac{72}{18} = 4$$

Tomando la raíz cuadrada en ambos lados (dado que $c$ y $d$ son enteros positivos, $c + d > 0$):
$$\frac{c + d}{|c - d|} = 2 \implies c + d = 2|c - d|$$

Por simetría en la suma $c + d$ y en las ecuaciones de área, podemos suponer sin pérdida de generalidad que $c > d$ (si fuera $d > c$, los valores simplemente se intercambiarían):
$$c + d = 2(c - d) \implies c + d = 2c - 2d \implies c = 3d$$

**Paso 3: Minimizar $a + b + c + d$**

Sustituyendo $c = 3d$ en la primera ecuación del área:
$$\frac{(3d - d)^2}{|a - b|} = 18 \implies \frac{4d^2}{|a - b|} = 18 \implies 2d^2 = 9|a - b|$$

Como $a, b, c, d$ son enteros positivos, $2d^2$ debe ser múltiplo de $9$, lo que implica que $d$ debe ser múltiplo de $3$. Para minimizar la suma total, tomamos el menor entero positivo posible para $d$:
- $d = 3$
- $c = 3(3) = 9$

Sustituyendo $d = 3$ para hallar $|a - b|$:
$$2(3)^2 = 9|a - b| \implies 18 = 9|a - b| \implies |a - b| = 2$$

Para minimizar $a + b$ sabiendo que $a$ y $b$ son enteros positivos con diferencia $2$, elegimos los menores enteros positivos posibles: $1$ y $3$. Así, $\{a, b\} = \{1, 3\}$.

Finalmente, calculamos el valor mínimo de $a + b + c + d$:
$$a + b + c + d = 1 + 3 + 9 + 3 = 16$$

\boxed{16}