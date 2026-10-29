Para hallar el valor mínimo posible de $a+b+c+d$, primero recordemos la fórmula para el área de un paralelogramo acotado por dos pares de rectas paralelas:
$$y = m_1x + c_1, \quad y = m_1x + c_2$$
$$y = m_2x + d_1, \quad y = m_2x + d_2$$

Mediante el cambio de variables $u = y - m_1x$ y $v = y - m_2x$, el determinante jacobiano de la transformación es $|m_1 - m_2|$. Por lo tanto, el área del paralelogramo en el plano $(x,y)$ está dada por:
$$\text{Área} = \frac{|c_1 - c_2| \cdot |d_1 - d_2|}{|m_1 - m_2|}$$

**Paso 1: Plantear las ecuaciones de área para ambos paralelogramos**

Para el primer paralelogramo, acotado por $y=ax+c$, $y=ax+d$, $y=bx+c$ y $y=bx+d$, tenemos:
$$\text{Área}_1 = \frac{|c - d| \cdot |c - d|}{|a - b|} = \frac{(c - d)^2}{|a - b|} = 18$$

Para el segundo paralelogramo, acotado por $y=ax+c$, $y=ax-d$, $y=bx+c$ y $y=bx-d$, tenemos:
$$\text{Área}_2 = \frac{|c - (-d)| \cdot |c - (-d)|}{|a - b|} = \frac{(c + d)^2}{|a - b|} = 72$$

**Paso 2: Relacionar $c$ y $d$**

Dividiendo la segunda ecuación entre la primera, obtenemos:
$$\frac{(c + d)^2}{(c - d)^2} = \frac{72}{18} = 4$$

Dado que $c$ y $d$ son enteros positivos, tomamos la raíz cuadrada en ambos lados:
$$\frac{c + d}{|c - d|} = 2 \implies c + d = 2|c - d|$$

Sin pérdida de generalidad (por simetría en la suma $c+d$), supongamos que $c > d$:
$$c + d = 2(c - d) \implies c + d = 2c - 2d \implies c = 3d$$

**Paso 3: Minimizar los valores de $a, b, c, d$**

Sustituyendo $c = 3d$ en la ecuación del primer paralelogramo:
$$\frac{(3d - d)^2}{|a - b|} = 18 \implies \frac{4d^2}{|a - b|} = 18 \implies 2d^2 = 9|a - b|$$

Como $9$ y $2$ son coprimos, $d^2$ debe ser múltiplo de $9$, lo que implica que $d$ debe ser múltiplo de $3$. Para minimizar la suma total, elegimos el menor entero positivo posible para $d$:
$$d = 3$$

Con $d = 3$, obtenemos inmediatamente:
$$c = 3(3) = 9$$

Sustituyendo $d = 3$ para hallar $|a - b|$:
$$2(3)^2 = 9|a - b| \implies 18 = 9|a - b| \implies |a - b| = 2$$

Para minimizar $a + b$ sabiendo que $a$ y $b$ son enteros positivos con diferencia $2$, tomamos el menor entero positivo para uno de ellos, es decir, $1$, por lo que el otro debe ser $3$:
$$\{a, b\} = \{1, 3\}$$

**Paso 4: Calcular la suma mínima**

Sumando los valores mínimos obtenidos:
$$a + b + c + d = 1 + 3 + 9 + 3 = 16$$

\boxed{16}