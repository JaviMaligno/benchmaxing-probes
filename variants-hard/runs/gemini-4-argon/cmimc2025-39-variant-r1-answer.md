Para hallar el área del triángulo $L_1L_2L_3$, podemos utilizar geometría vectorial o números complejos.

### 1. Representación vectorial de los vértices
Supongamos que el triángulo $ABC$ está orientado en sentido antihorario en el plano y sea $J$ la rotación de $90^\circ$ en sentido antihorario (de modo que $-J$ representa la rotación de $90^\circ$ en sentido horario, apuntando hacia el exterior del triángulo).

En cada cuadrado construido hacia el exterior de $\triangle ABC$:
- En el cuadrado $ABXY$ (sobre el lado $AB$), $X$ es adyacente a $B$ e $Y$ es adyacente a $A$:
  $$Y = A - J(B - A), \qquad X = B - J(B - A)$$
- En el cuadrado $BCPQ$ (sobre el lado $BC$), $P$ es adyacente a $C$ y $Q$ es adyacente a $B$:
  $$Q = B - J(C - B), \qquad P = C - J(C - B)$$
- En el cuadrado $ACMN$ (sobre el lado $AC$, con orden cíclico $A\to C\to M\to N$ hacia el exterior), $M$ es adyacente a $C$ y $N$ es adyacente a $A$:
  $$M = C - J(A - C), \qquad N = A - J(A - C)$$

Calculamos los puntos medios $L_1, L_2, L_3$:
$$L_1 = \frac{M + P}{2} = C - \frac{1}{2}J(A - B)$$
$$L_2 = \frac{Q + X}{2} = B - \frac{1}{2}J(C - A)$$
$$L_3 = \frac{N + Y}{2} = A - \frac{1}{2}J(B - C)$$

### 2. Fórmula para el área de $\triangle L_1L_2L_3$
Sean $\vec{x} = B - A$ y $\vec{y} = C - A$, con longitudes $|\vec{x}| = c$ y $|\vec{y}| = b$, y $|\vec{y} - \vec{x}| = a$. Tomando $A$ como origen:
$$L_1 - A = \vec{y} + \frac{1}{2}J\vec{x}, \qquad L_2 - A = \vec{x} - \frac{1}{2}J\vec{y}, \qquad L_3 - A = -\frac{1}{2}J(\vec{x} - \vec{y})$$

Restando $L_3$ obtenemos dos vectores que generan $\triangle L_1L_2L_3$:
$$\vec{p} = L_2 - L_3 = \vec{x} + \frac{1}{2}J\vec{x} - J\vec{y}$$
$$\vec{q} = L_1 - L_3 = J\vec{x} + \vec{y} - \frac{1}{2}J\vec{y}$$

Usando el producto vectorial bidimensional ($\vec{u} \times \vec{v} = u_1v_2 - u_2v_1$) y las identidades $\vec{u} \times J\vec{v} = \vec{u}\cdot\vec{v}$, $J\vec{u} \times \vec{v} = -\vec{u}\cdot\vec{v}$ y $J\vec{u} \times J\vec{v} = \vec{u} \times \vec{v}$:
$$\begin{aligned}
\vec{p} \times \vec{q} &= \left(\vec{x} + \frac{1}{2}J\vec{x} - J\vec{y}\right) \times \left(J\vec{x} + \vec{y} - \frac{1}{2}J\vec{y}\right) \\
&= \left(|\vec{x}|^2 + \vec{x}\times\vec{y} - \frac{1}{2}\vec{x}\cdot\vec{y}\right) + \left(-\frac{1}{2}\vec{x}\cdot\vec{y} - \frac{1}{4}\vec{x}\times\vec{y}\right) + \left(\vec{x}\times\vec{y} + |\vec{y}|^2\right) \\
&= |\vec{x}|^2 + |\vec{y}|^2 - \vec{x}\cdot\vec{y} + \frac{7}{4}(\vec{x}\times\vec{y})
\end{aligned}$$

Por la ley de los cosenos, $2\vec{x}\cdot\vec{y} = b^2 + c^2 - a^2$, por lo que:
$$|\vec{x}|^2 + |\vec{y}|^2 - \vec{x}\cdot\vec{y} = c^2 + b^2 - \frac{b^2 + c^2 - a^2}{2} = \frac{a^2 + b^2 + c^2}{2}$$

Además, $\vec{x}\times\vec{y} = 2[ABC]$. Por tanto, el área de $\triangle L_1L_2L_3$ es:
$$[L_1L_2L_3] = \frac{1}{2}(\vec{p} \times \vec{q}) = \frac{a^2 + b^2 + c^2}{4} + \frac{7}{4}[ABC]$$

### 3. Cálculo numérico
Con $a = BC = 26$, $b = AC = 102$ y $c = AB = 80$:
1. **Suma de cuadrados:**
   $$\frac{a^2 + b^2 + c^2}{4} = \frac{26^2 + 102^2 + 80^2}{4} = \frac{676 + 10404 + 6400}{4} = \frac{17480}{4} = 4370$$

2. **Área de $\triangle ABC$ mediante la fórmula de Herón:**
   El semiperímetro es $s = \frac{26 + 102 + 80}{2} = 104$.
   $$[ABC] = \sqrt{104(104 - 26)(104 - 102)(104 - 80)} = \sqrt{104 \cdot 78 \cdot 2 \cdot 24} = \sqrt{2^8 \cdot 3^2 \cdot 13^2} = 16 \cdot 3 \cdot 13 = 624$$

3. **Área de $\triangle L_1L_2L_3$:**
   $$[L_1L_2L_3] = 4370 + \frac{7}{4}(624) = 4370 + 1092 = 5462$$

\boxed{5462}