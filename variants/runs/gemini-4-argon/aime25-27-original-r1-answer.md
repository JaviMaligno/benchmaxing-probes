Para hallar el valor de $A_1 A_2 + A_1 A_{11}$, analicemos las propiedades geométricas de los triángulos que conforman el polígono.

**Paso 1: Relación entre las distancias desde $A_1$**
Sea $x_i = A_1 A_i$ para cada $2 \le i \le 11$, y sea $\theta_i = \angle A_i A_1 A_{i+1}$ para $2 \le i \le 10$.
Sabemos que $\cos(\theta_i) = \frac{12}{13}$. Como $\theta_i \in (0, \pi)$, tenemos que:
$$\sin(\theta_i) = \sqrt{1 - \cos^2(\theta_i)} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13}$$

El área de cada triángulo $\triangle A_i A_1 A_{i+1}$ es igual a $1$, por lo que para todo $2 \le i \le 10$:
$$\text{Área}(\triangle A_i A_1 A_{i+1}) = \frac{1}{2} x_i x_{i+1} \sin(\theta_i) = 1 \implies \frac{1}{2} x_i x_{i+1} \left(\frac{5}{13}\right) = 1 \implies x_i x_{i+1} = \frac{26}{5}$$

Dado que $x_i x_{i+1} = \frac{26}{5}$ para todo $2 \le i \le 10$, se deduce que $x_{i+2} = x_i$. Por lo tanto, las longitudes se alternan:
$$x_2 = x_4 = x_6 = x_8 = x_{10} = a$$
$$x_3 = x_5 = x_7 = x_9 = x_{11} = b$$
donde $ab = \frac{26}{5}$. En particular, la suma que buscamos es:
$$A_1 A_2 + A_1 A_{11} = x_2 + x_{11} = a + b$$

**Paso 2: Cálculo de los lados $A_i A_{i+1}$ mediante la Ley de Cosenos**
Aplicando la Ley de Cosenos en el triángulo $\triangle A_i A_1 A_{i+1}$ para $2 \le i \le 10$, la longitud $s = A_i A_{i+1}$ cumple:
$$s^2 = x_i^2 + x_{i+1}^2 - 2 x_i x_{i+1} \cos(\theta_i) = a^2 + b^2 - 2ab\left(\frac{12}{13}\right)$$

Reescribiendo $a^2 + b^2 = (a+b)^2 - 2ab$ y sustituyendo $ab = \frac{26}{5}$:
$$s^2 = (a+b)^2 - 2ab\left(1 + \frac{12}{13}\right) = (a+b)^2 - 2\left(\frac{26}{5}\right)\left(\frac{25}{13}\right) = (a+b)^2 - 20$$
De modo que $s = \sqrt{(a+b)^2 - 20}$ para cada uno de los $9$ lados $A_2 A_3, A_3 A_4, \dots, A_{10} A_{11}$.

**Paso 3: Uso del perímetro del polígono**
El perímetro del polígono de $11$ lados es igual a $20$:
$$A_1 A_2 + \sum_{i=2}^{10} A_i A_{i+1} + A_{11} A_1 = a + 9s + b = 20$$

Sea $u = a + b$. Sustituyendo $s = \sqrt{u^2 - 20}$ en la ecuación del perímetro:
$$u + 9\sqrt{u^2 - 20} = 20 \implies 9\sqrt{u^2 - 20} = 20 - u$$

Elevando ambos lados al cuadrado (con $u \le 20$):
$$81(u^2 - 20) = (20 - u)^2$$
$$81u^2 - 1620 = u^2 - 40u + 400$$
$$80u^2 + 40u - 2020 = 0$$

Dividiendo toda la ecuación entre $20$:
$$4u^2 + 2u - 101 = 0$$

Aplicando la fórmula general para ecuaciones cuadráticas y tomando la raíz positiva:
$$u = \frac{-2 + \sqrt{2^2 - 4(4)(-101)}}{2(4)} = \frac{-2 + \sqrt{1620}}{8} = \frac{-1 + \sqrt{405}}{4} = \frac{9\sqrt{5} - 1}{4}$$

(Notemos que $u^2 \approx 22.86 > 4ab = 20.8$, lo que garantiza soluciones reales y distintas para $a$ y $b$, formando un polígono simple no convexo).

**Paso 4: Suma final**
Comparando $A_1 A_2 + A_1 A_{11} = \frac{9\sqrt{5} - 1}{4}$ con la forma $\frac{m\sqrt{n} - p}{q}$, identificamos:
- $m = 9$
- $n = 5$
- $p = 1$
- $q = 4$

Por lo tanto, $m + n + p + q = 9 + 5 + 1 + 4 = 19$.

\boxed{19}