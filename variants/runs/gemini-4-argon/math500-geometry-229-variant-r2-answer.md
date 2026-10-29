Para hallar el valor mínimo posible de $p+q+r+s$, primero calculamos el área de un paralelogramo general limitado por dos pares de rectas paralelas.

Considérese el paralelogramo limitado por las rectas:
$$y = px + b_1, \quad y = px + b_2, \quad y = qx + c_1, \quad y = qx + c_2$$
Mediante el cambio de variables $u = y - px$ y $v = y - qx$, el jacobiano de la transformación es:
$$\left|\frac{\partial(u,v)}{\partial(x,y)}\right| = \left|\det \begin{pmatrix} -p & 1 \\ -q & 1 \end{pmatrix}\right| = |q - p| = |p - q|$$
Por lo tanto, el área del paralelogramo en el plano $(x,y)$ viene dada por:
$$\text{Área} = \frac{|b_1 - b_2| \cdot |c_1 - c_2|}{|p - q|}$$

**1. Primer paralelogramo:**
Las rectas son $y=px+r$, $y=px+s$, $y=qx+r$ y $y=qx+s$. Aplicando la fórmula del área, tenemos:
$$\frac{|r - s| \cdot |r - s|}{|p - q|} = \frac{(r - s)^2}{|p - q|} = 8$$

**2. Segundo paralelogramo:**
Las rectas son $y=px+r$, $y=px-s$, $y=qx+r$ y $y=qx-s$. Aplicando nuevamente la fórmula, obtenemos:
$$\frac{|r - (-s)| \cdot |r - (-s)|}{|p - q|} = \frac{(r + s)^2}{|p - q|} = 50$$

**3. Relación entre $r$ y $s$:**
Dividiendo la segunda ecuación entre la primera:
$$\frac{(r + s)^2}{(r - s)^2} = \frac{50}{8} = \frac{25}{4}$$
Tomando la raíz cuadrada en ambos lados (dado que $r, s > 0$, se cumple que $r+s > 0$):
$$\frac{r + s}{|r - s|} = \frac{5}{2}$$
Sin pérdida de generalidad, supongamos que $r > s$ (el caso $s > r$ es simétrico y arroja la misma suma $r+s$). Entonces:
$$2(r + s) = 5(r - s) \implies 2r + 2s = 5r - 5s \implies 3r = 7s$$
Como $r$ y $s$ son enteros positivos, debe existir un entero positivo $k$ tal que:
$$r = 7k \quad \text{y} \quad s = 3k$$
(o viceversa).

**4. Relación entre $p$ y $q$:**
Sustituyendo $|r - s| = 4k$ en la ecuación del área del primer paralelogramo:
$$\frac{(4k)^2}{|p - q|} = 8 \implies \frac{16k^2}{|p - q|} = 8 \implies |p - q| = 2k^2$$

**5. Minimización de $p + q + r + s$:**
Queremos minimizar la suma:
$$p + q + r + s = p + q + 10k$$
Sin pérdida de generalidad, si $p > q$, entonces $p = q + 2k^2$, por lo que:
$$p + q + r + s = 2q + 2k^2 + 10k$$
Como $q$ y $k$ son enteros positivos, el valor mínimo se alcanza cuando tomamos los valores más pequeños posibles, es decir, $k = 1$ y $q = 1$:
- Para $k = 1$: $\{r, s\} = \{7, 3\}$, por lo que $r + s = 10$.
- Para $q = 1$: $p = 1 + 2(1)^2 = 3$, por lo que $p + q = 4$.

Finalmente, el valor mínimo posible de $p + q + r + s$ es:
$$3 + 1 + 7 + 3 = 14$$

\boxed{14}