# Solución paso a paso

**Condición de triángulo.** Tres longitudes $2, a, b$ forman un triángulo (no degenerado) si y solo si se cumplen las tres desigualdades triangulares:

$$a + b > 2, \qquad a + 2 > b, \qquad b + 2 > a.$$

Las últimas dos se resumen como $|a - b| < 2$.

**Modelo geométrico.** El par $(a,b)$ se distribuye uniformemente en el cuadrado $(0,4)\times(0,4)$, de área $16$. Buscamos el área de la región:

$$a + b > 2 \quad \text{y} \quad |a-b| < 2.$$

**Cálculo por complemento.** La región de fallo es: $a+b \le 2$ **o** $|a-b| \ge 2$.

- **Región $a+b \le 2$:** triángulo rectángulo con vértices $(0,0)$, $(2,0)$, $(0,2)$; su área es $\tfrac12 \cdot 2 \cdot 2 = 2$.
- **Región $b \le a-2$:** triángulo con vértices $(2,0)$, $(4,0)$, $(4,2)$; área $= 2$. Por simetría, $a \le b-2$ también tiene área $2$. Total: $4$.

**¿Se solapan?** Si $a+b \le 2$, entonces $|a-b| \le a+b \le 2$, con igualdad solo en un conjunto de medida cero. Por lo tanto, las regiones de fallo son esencialmente disjuntas.

Área de fallo $= 2 + 4 = 6$, así que el área de éxito es:

$$16 - 6 = 10.$$

**Probabilidad:**

$$\frac{10}{16} = \frac{5}{8}.$$

$\boxed{\dfrac{5}{8}}$