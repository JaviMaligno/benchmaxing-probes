Para hallar el área del triángulo $L_1 L_2 L_3$, podemos utilizar geometría vectorial en el plano.

### 1. Representación vectorial de los vértices
Supongamos que el triángulo $ABC$ está orientado en sentido antihorario y sea $J$ el operador de rotación de $90^\circ$ en sentido antihorario. Dado que los cuadrados se construyen hacia el exterior del triángulo, los vectores perpendiculares hacia afuera de los lados $\overrightarrow{AB}$, $\overrightarrow{BC}$ y $\overrightarrow{CA}$ se obtienen aplicando la rotación horaria $-J$:

- Para el cuadrado $ABXY$:
  $$X = B - J(B - A), \quad Y = A - J(B - A)$$
- Para el cuadrado $BCPQ$:
  $$P = C - J(C - B), \quad Q = B - J(C - B)$$
- Para el cuadrado $ACMN$ (orientado hacia afuera sobre el lado $CA$):
  $$M = C - J(A - C), \quad N = A - J(A - C)$$

Calculamos los puntos medios $L_1, L_2, L_3$:
$$L_1 = \frac{M + P}{2} = C - \frac{1}{2}J(A - B) = C + \frac{1}{2}J(B - A)$$
$$L_2 = \frac{Q + X}{2} = B - \frac{1}{2}J(C - A) = B + \frac{1}{2}J(A - C)$$
$$L_3 = \frac{N + Y}{2} = A - \frac{1}{2}J(B - C) = A + \frac{1}{2}J(C - B)$$

---

### 2. Fórmula para el área de $\triangle L_1 L_2 L_3$
Fijando el origen en $A = \vec{0}$ y definiendo $\vec{u} = B - A$ y $\vec{v} = C - A$, tenemos:
$$L_1 - L_3 = \vec{v} + J\vec{u} - \frac{1}{2}J\vec{v}$$
$$L_2 - L_3 = \vec{u} + \frac{1}{2}J\vec{u} - J\vec{v}$$

El área orientada del triángulo $L_1 L_2 L_3$ viene dada por $\frac{1}{2} | [L_1 - L_3, L_2 - L_3] |$, donde $[\vec{x}, \vec{y}]$ denota el producto cruz en 2D. Usando las propiedades $[\vec{u}, \vec{v}] = 2S$ (donde $S$ es el área de $\triangle ABC$), $[J\vec{x}, J\vec{y}] = [\vec{x}, \vec{y}]$ y $[\vec{x}, J\vec{y}] = \vec{x} \cdot \vec{y}$, desarrollamos el producto:

$$\begin{aligned}
[L_1 - L_3, L_2 - L_3] &= [\vec{v}, \vec{u}] + \frac{1}{2}[\vec{v}, J\vec{u}] - [\vec{v}, J\vec{v}] + [J\vec{u}, \vec{u}] - [J\vec{u}, J\vec{v}] - \frac{1}{2}[J\vec{v}, \vec{u}] - \frac{1}{4}[J\vec{v}, J\vec{u}] \\
&= -2S + \frac{1}{2}(\vec{u} \cdot \vec{v}) - |\vec{v}|^2 - |\vec{u}|^2 - 2S + \frac{1}{2}(\vec{u} \cdot \vec{v}) + \frac{1}{2}S \\
&= -\frac{7}{2}S + \vec{u} \cdot \vec{v} - \left(|\vec{u}|^2 + |\vec{v}|^2\right)
\end{aligned}$$

Por la ley de los cosenos, $\vec{u} \cdot \vec{v} = \frac{b^2 + c^2 - a^2}{2}$, con $a = BC$, $b = AC$ y $c = AB$. Sustituyendo esto:
$$\vec{u} \cdot \vec{v} - (b^2 + c^2) = -\frac{a^2 + b^2 + c^2}{2}$$

Por lo tanto, el área de $\triangle L_1 L_2 L_3$ es:
$$\text{Área}(L_1 L_2 L_3) = \frac{7}{4}S + \frac{a^2 + b^2 + c^2}{4}$$

---

### 3. Cálculo numérico
Los lados del triángulo son $a = 50$, $b = 112$ y $c = 78$.

1. **Área $S$ de $\triangle ABC$ (Fórmula de Herón):**
   El semiperímetro es:
   $$s = \frac{50 + 112 + 78}{2} = 120$$
   $$S = \sqrt{120(120 - 50)(120 - 112)(120 - 78)} = \sqrt{120 \cdot 70 \cdot 8 \cdot 42} = 1680$$
   De aquí obtenemos:
   $$\frac{7}{4}S = \frac{7}{4}(1680) = 2940$$

2. **Suma de cuadrados de los lados:**
   $$\frac{a^2 + b^2 + c^2}{4} = \left(\frac{50}{2}\right)^2 + \left(\frac{112}{2}\right)^2 + \left(\frac{78}{2}\right)^2 = 25^2 + 56^2 + 39^2 = 625 + 3136 + 1521 = 5282$$

3. **Área total:**
   $$\text{Área}(L_1 L_2 L_3) = 2940 + 5282 = 8222$$

\boxed{8222}