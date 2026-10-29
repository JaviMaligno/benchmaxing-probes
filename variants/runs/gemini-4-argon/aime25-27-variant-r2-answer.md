Para hallar el valor de $B_1 B_2 + B_1 B_{11}$, definimos $r_i = B_1 B_i$ para cada $2 \le i \le 11$ y $\theta = \angle B_i B_1 B_{i+1}$ para $2 \le i \le 10$.

**Paso 1: Relación entre las distancias desde $B_1$**
Sabemos que $\cos(\theta) = \frac{4}{5}$. Como $\theta \in (0, \pi)$, tenemos que:
$$\sin(\theta) = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \frac{3}{5}$$

El área de cada triángulo $B_i B_1 B_{i+1}$ (para $2 \le i \le 10$) es igual a $1$:
$$\text{Área} = \frac{1}{2} r_i r_{i+1} \sin(\theta) = \frac{3}{10} r_i r_{i+1} = 1 \implies r_i r_{i+1} = \frac{10}{3}$$

De esta relación se deduce que $r_i = r_{i+2}$ para todo $2 \le i \le 9$. Por lo tanto, las longitudes se alternan:
$$r_2 = r_4 = r_6 = r_8 = r_{10} = x$$
$$r_3 = r_5 = r_7 = r_9 = r_{11} = y$$
con $xy = \frac{10}{3}$. Observamos que la suma buscada es $S = B_1 B_2 + B_1 B_{11} = r_2 + r_{11} = x + y$.

**Paso 2: Cálculo de los demás lados del polígono**
Aplicando la ley de los cosenos en el triángulo $B_i B_1 B_{i+1}$ para $2 \le i \le 10$:
$$B_i B_{i+1}^2 = r_i^2 + r_{i+1}^2 - 2 r_i r_{i+1} \cos(\theta) = x^2 + y^2 - 2\left(\frac{10}{3}\right)\left(\frac{4}{5}\right) = x^2 + y^2 - \frac{16}{3}$$

Esto implica que los $9$ lados $B_2 B_3, B_3 B_4, \dots, B_{10} B_{11}$ tienen la misma longitud, que llamaremos $s$. Expresando $s^2$ en función de $S = x + y$:
$$s^2 = (x + y)^2 - 2xy - \frac{16}{3} = S^2 - \frac{20}{3} - \frac{16}{3} = S^2 - 12$$

**Paso 3: Uso del perímetro**
El perímetro del polígono de $11$ lados es $20$:
$$B_1 B_2 + B_{11} B_1 + \sum_{i=2}^{10} B_i B_{i+1} = x + y + 9s = S + 9s = 20$$

Despejamos $9s = 20 - S$ y elevamos al cuadrado ambos lados:
$$81s^2 = (20 - S)^2$$
Sustituyendo $s^2 = S^2 - 12$:
$$81(S^2 - 12) = 400 - 40S + S^2$$
$$81S^2 - 972 = S^2 - 40S + 400$$
$$80S^2 + 40S - 1372 = 0$$
Dividiendo toda la ecuación entre $4$:
$$20S^2 + 10S - 343 = 0$$

**Paso 4: Resolución de la ecuación cuadrática**
Usando la fórmula general para $S > 0$:
$$S = \frac{-10 + \sqrt{10^2 - 4(20)(-343)}}{2(20)} = \frac{-10 + \sqrt{100 + 27440}}{40} = \frac{\sqrt{27540} - 10}{40}$$

Simplificamos el radical sabiendo que $27540 = 324 \times 85 = 18^2 \times 85$:
$$S = \frac{18\sqrt{85} - 10}{40} = \frac{9\sqrt{85} - 5}{20}$$

Comparando con la forma $\frac{m\sqrt{n} - p}{q}$, identificamos $m = 9$, $n = 85$, $p = 5$ y $q = 20$ (donde $85 = 5 \times 17$ es libre de cuadrados y $\gcd(9, 5, 20) = 1$).

Finalmente, calculamos la suma pedida:
$$m + n + p + q = 9 + 85 + 5 + 20 = 119$$

\boxed{119}