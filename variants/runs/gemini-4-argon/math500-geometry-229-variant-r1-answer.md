Para hallar el valor mínimo posible de $p+q+r+s$, calculemos primero el área de un paralelogramo definido por dos pares de rectas paralelas en función de sus pendientes y ordenadas en el origen.

Consideremos el paralelogramo delimitado por las rectas:
$$y - px = c_1, \quad y - px = c_2, \quad y - qx = d_1, \quad y - qx = d_2$$

Realizando el cambio de variables $u = y - px$ y $v = y - qx$, el determinante jacobiano de la transformación es:
$$\left|\frac{\partial(u,v)}{\partial(x,y)}\right| = \left|\det \begin{pmatrix} -p & 1 \\ -q & 1 \end{pmatrix}\right| = |q - p| = |p - q|$$

Por lo tanto, el área del paralelogramo en el plano $(x,y)$ viene dada por:
$$\text{Área} = \frac{|c_1 - c_2| \cdot |d_1 - d_2|}{|p - q|}$$

**1. Primer paralelogramo:**
Las rectas son $y = px + r$, $y = px + s$, $y = qx + r$ y $y = qx + s$. Aplicando la fórmula del área con $c_1 = d_1 = r$ y $c_2 = d_2 = s$, obtenemos:
$$\frac{(r - s)^2}{|p - q|} = 8 \implies (r - s)^2 = 8|p - q|$$

**2. Segundo paralelogramo:**
Las rectas son $y = px + r$, $y = px - s$, $y = qx + r$ y $y = qx - s$. Aplicando la fórmula con $c_1 = d_1 = r$ y $c_2 = d_2 = -s$, tenemos:
$$\frac{(r + s)^2}{|p - q|} = 50 \implies (r + s)^2 = 50|p - q|$$

**3. Minimización de las variables:**
Sea $k = |p - q|$. Como $p$ y $q$ son enteros positivos y el área es finita, $k$ debe ser un entero positivo. De la primera ecuación, $8k = (r - s)^2$ debe ser un cuadrado perfecto. Dado que $8k = 2^3 k$, el valor de $k$ debe ser de la forma $k = 2m^2$ para algún entero positivo $m$.

Sustituyendo $k = 2m^2$ en ambas ecuaciones:
$$|r - s| = \sqrt{16m^2} = 4m$$
$$r + s = \sqrt{100m^2} = 10m$$

Resolviendo para $r$ y $s$, obtenemos que $\{r, s\} = \{7m, 3m\}$, los cuales son enteros positivos para cualquier entero $m \ge 1$.

Para minimizar la suma $p + q + r + s$:
- Elegimos el menor entero positivo posible para $m$, que es $m = 1$.
- Con $m = 1$, tenemos $r + s = 10(1) = 10$ (donde $\{r, s\} = \{7, 3\}$) y $|p - q| = 2(1)^2 = 2$.
- Para minimizar $p + q$ sabiendo que $p, q \ge 1$ y $|p - q| = 2$, tomamos $\{p, q\} = \{1, 3\}$, lo que nos da $p + q = 1 + 3 = 4$.

Finalmente, sumamos los valores mínimos obtenidos:
$$p + q + r + s = 4 + 10 = 14$$

\boxed{14}