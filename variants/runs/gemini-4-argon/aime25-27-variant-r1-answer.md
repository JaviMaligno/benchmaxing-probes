Para hallar el valor de $B_1 B_2 + B_1 B_{11}$, denotemos las distancias desde el vértice $B_1$ a los demás vértices como $r_i = B_1 B_i$ para cada $2 \le i \le 11$, y sea $\theta = \angle B_i B_1 B_{i+1}$ para $2 \le i \le 10$.

**Paso 1: Relación entre los radios $r_i$**
Sabemos que para cada $2 \le i \le 10$, $\cos\theta = \frac{4}{5}$. Como $0 < \theta < \pi$, tenemos que:
$$\sin\theta = \sqrt{1 - \cos^2\theta} = \frac{3}{5}$$

El área de cada triángulo $B_i B_1 B_{i+1}$ es $1$, por lo que:
$$\frac{1}{2} r_i r_{i+1} \sin\theta = 1 \implies \frac{3}{10} r_i r_{i+1} = 1 \implies r_i r_{i+1} = \frac{10}{3}$$

De esta relación para todo $2 \le i \le 10$, se deduce que $r_{i+2} = r_i$, es decir:
$$r_2 = r_4 = r_6 = r_8 = r_{10} = x$$
$$r_3 = r_5 = r_7 = r_9 = r_{11} = y$$
donde $xy = \frac{10}{3}$. Nuestro objetivo es encontrar $S = B_1 B_2 + B_1 B_{11} = r_2 + r_{11} = x + y$.

**Paso 2: Longitud de los lados $B_i B_{i+1}$**
Dado que el polígono es simple y $r_{i-1} = r_{i+1}$, los rayos $B_1 B_i$ no pueden doblarse sobre sí mismos (de lo contrario, $B_{i+1}$ coincidiría con $B_{i-1}$), sino que giran siempre en el mismo sentido alrededor de $B_1$ (cubriendo un ángulo total de $9\theta \approx 331.8^\circ < 360^\circ$).

Aplicando la ley de los cosenos en el triángulo $B_i B_1 B_{i+1}$ para $2 \le i \le 10$:
$$B_i B_{i+1}^2 = r_i^2 + r_{i+1}^2 - 2 r_i r_{i+1} \cos\theta = x^2 + y^2 - 2\left(\frac{10}{3}\right)\left(\frac{4}{5}\right) = x^2 + y^2 - \frac{16}{3}$$

Como $x^2 + y^2 = (x+y)^2 - 2xy = S^2 - \frac{20}{3}$, sustituimos en la expresión anterior:
$$B_i B_{i+1}^2 = S^2 - \frac{20}{3} - \frac{16}{3} = S^2 - 12 \implies B_i B_{i+1} = \sqrt{S^2 - 12}$$

**Paso 3: Ecuación del perímetro**
El perímetro del polígono de $11$ lados es igual a $20$:
$$(B_1 B_2 + B_1 B_{11}) + \sum_{i=2}^{10} B_i B_{i+1} = 20$$
$$S + 9\sqrt{S^2 - 12} = 20 \implies 9\sqrt{S^2 - 12} = 20 - S$$

Elevando ambos lados al cuadrado:
$$81(S^2 - 12) = (20 - S)^2$$
$$81S^2 - 972 = S^2 - 40S + 400$$
$$80S^2 + 40S - 1372 = 0$$

Dividiendo entre $4$:
$$20S^2 + 10S - 343 = 0$$

Resolviendo la ecuación cuadrática para $S > 0$:
$$S = \frac{-10 + \sqrt{10^2 - 4(20)(-343)}}{40} = \frac{-10 + \sqrt{27540}}{40} = \frac{18\sqrt{85} - 10}{40} = \frac{9\sqrt{85} - 5}{20}$$

Identificando los términos con $\frac{m\sqrt{n} - p}{q}$, obtenemos $m = 9$, $n = 85$, $p = 5$ y $q = 20$. Por lo tanto:
$$m + n + p + q = 9 + 85 + 5 + 20 = 119$$

\boxed{119}