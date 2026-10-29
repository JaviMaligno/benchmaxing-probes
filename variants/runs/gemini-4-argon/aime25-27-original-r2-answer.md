Para hallar el valor de $A_1 A_2 + A_1 A_{11}$, analicemos las propiedades geométricas del polígono $A_1 A_2 A_3 \ldots A_{11}$.

**Paso 1: Relación entre las distancias desde $A_1$**
Sea $x_i = A_1 A_i$ para cada $2 \le i \le 11$, y sea $\theta_i = \angle A_i A_1 A_{i+1}$ para $2 \le i \le 10$. 
Se nos da que $\cos(\theta_i) = \frac{12}{13}$ para todo $2 \le i \le 10$. Como $\theta_i \in (0, \pi)$, tenemos que:
$$\sin(\theta_i) = \sqrt{1 - \cos^2(\theta_i)} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13}$$

El área de cada triángulo $\triangle A_i A_1 A_{i+1}$ es igual a $1$, por lo que:
$$\text{Área}(\triangle A_i A_1 A_{i+1}) = \frac{1}{2} x_i x_{i+1} \sin(\theta_i) = 1 \implies \frac{1}{2} x_i x_{i+1} \left(\frac{5}{13}\right) = 1 \implies x_i x_{i+1} = \frac{26}{5}$$

Como $x_i x_{i+1} = \frac{26}{5}$ se cumple para todo $2 \le i \le 10$, deducimos que $x_{i+2} = x_i$. Es decir, las longitudes se alternan:
$$x_2 = x_4 = x_6 = x_8 = x_{10} = a$$
$$x_3 = x_5 = x_7 = x_9 = x_{11} = b$$
con $ab = \frac{26}{5}$. Además, como el polígono es simple (sus vértices no pueden coincidir), los rayos $A_1 A_2, A_1 A_3, \ldots, A_1 A_{11}$ avanzan en el mismo sentido angular alrededor de $A_1$.

Buscamos el valor de:
$$S = A_1 A_2 + A_1 A_{11} = x_2 + x_{11} = a + b$$

---

**Paso 2: Cálculo de los lados $A_i A_{i+1}$ mediante la Ley de Cosenos**
En cada uno de los $9$ triángulos $\triangle A_i A_1 A_{i+1}$ ($2 \le i \le 10$), los lados adyacentes al vértice $A_1$ miden $a$ y $b$, y el ángulo comprendido tiene coseno igual a $\frac{12}{13}$. Por la Ley de Cosenos, todos los segmentos $A_i A_{i+1}$ tienen la misma longitud $c$:
$$c^2 = a^2 + b^2 - 2ab \cos(\theta_i) = (a + b)^2 - 2ab\big(1 + \cos(\theta_i)\big)$$

Sustituyendo $a + b = S$, $ab = \frac{26}{5}$ y $\cos(\theta_i) = \frac{12}{13}$:
$$2ab\big(1 + \cos(\theta_i)\big) = 2 \left(\frac{26}{5}\right) \left(1 + \frac{12}{13}\right) = \frac{52}{5} \cdot \frac{25}{13} = 20$$
Por lo tanto:
$$c^2 = S^2 - 20$$

---

**Paso 3: Uso del perímetro del polígono**
El perímetro del polígono de $11$ lados es la suma de los lados $A_1 A_2$, $A_{11} A_1$ y los $9$ lados $A_i A_{i+1}$ ($2 \le i \le 10$):
$$\text{Perímetro} = A_1 A_2 + A_{11} A_1 + \sum_{i=2}^{10} A_i A_{i+1} = (a + b) + 9c = S + 9c = 20$$

Despejando $9c$ y elevando al cuadrado ambos miembros (con $S < 20$):
$$9c = 20 - S \implies 81c^2 = (20 - S)^2$$

Sustituimos $c^2 = S^2 - 20$:
$$81(S^2 - 20) = 400 - 40S + S^2$$
$$80S^2 + 40S - 2020 = 0$$

Dividiendo toda la ecuación entre $20$:
$$4S^2 + 2S - 101 = 0$$

Aplicando la fórmula general para ecuaciones de segundo grado y tomando la raíz positiva (ya que $S > 0$):
$$S = \frac{-2 + \sqrt{2^2 - 4(4)(-101)}}{2(4)} = \frac{-2 + \sqrt{1620}}{8} = \frac{-2 + 18\sqrt{5}}{8} = \frac{9\sqrt{5} - 1}{4}$$

---

**Paso 4: Suma final**
Comparando $A_1 A_2 + A_1 A_{11} = \frac{9\sqrt{5} - 1}{4}$ con la forma $\frac{m\sqrt{n} - p}{q}$, identificamos:
$$m = 9, \quad n = 5, \quad p = 1, \quad q = 4$$

Finalmente, calculamos $m + n + p + q$:
$$m + n + p + q = 9 + 5 + 1 + 4 = 19$$

\boxed{19}