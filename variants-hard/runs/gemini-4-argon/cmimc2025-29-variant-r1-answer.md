Para encontrar la menor razón posible entre el eje mayor y el eje menor de una elipse que pasa por los cuatro vértices del trapecio $PQRS$, podemos utilizar geometría analítica.

### Paso 1: Sistema de coordenadas
Dado que $\angle PSR = 90^\circ$ y $PQ \parallel SR$, también se cumple que $\angle SPQ = 90^\circ$. Situamos el vértice $S$ en el origen de coordenadas $(0, 0)$, el lado $SR$ sobre el semieje positivo $x$ y el lado $PS$ sobre el semieje positivo $y$.

Con las longitudes $SR = 110$, $PS = 28$ y $PQ = 20$, las coordenadas de los cuatro vértices son:
- $S = (0, 0)$
- $R = (110, 0)$
- $P = (0, 28)$
- $Q = (20, 28)$

### Paso 2: Haz de cónicas que pasan por $P, Q, R, S$
Hallamos las ecuaciones de las rectas que contienen los lados del trapecio:
- Recta $SR$: $y = 0$
- Recta $PQ$: $y - 28 = 0$
- Recta $PS$: $x = 0$
- Recta $QR$: pasa por $(20, 28)$ y $(110, 0)$. Su pendiente es $m = \frac{0 - 28}{110 - 20} = -\frac{28}{90} = -\frac{14}{45}$, por lo que su ecuación es:
  $$14x + 45y - 1540 = 0$$

Cualquier cónica que pase por los cuatro vértices (salvo el par de rectas paralelas $y(y - 28) = 0$) pertenece al haz generado por los dos pares de rectas opuestas:
$$x(14x + 45y - 1540) + C y(y - 28) = 0$$
Desarrollando los términos cuadráticos, obtenemos:
$$14x^2 + 45xy + Cy^2 - 1540x - 28Cy = 0$$
donde $A = 14$, $B = 45$ y $C$ es un parámetro real.

Para que esta cónica sea una elipse, la forma cuadrática asociada debe ser definida positiva, lo cual ocurre si y solo si $4AC - B^2 > 0$, es decir, $C > \frac{45^2}{4 \cdot 14} = \frac{2025}{56}$. Como la curva pasa por cuatro puntos reales distintos, cualquier valor de $C$ en este rango produce una elipse real no degenerada.

### Paso 3: Minimización de la razón de los ejes
Sea $r = \frac{a}{b} \ge 1$ la razón entre la longitud del eje mayor y la del eje menor de la elipse. Si $\mu_1$ y $\mu_2$ son los autovalores de la matriz de la forma cuadrática
$$M = \begin{pmatrix} A & B/2 \\ B/2 & C \end{pmatrix},$$
entonces las longitudes de los ejes son inversamente proporcionales a $\sqrt{\mu_1}$ y $\sqrt{\mu_2}$, de modo que $r = \sqrt{\frac{\mu_{\max}}{\mu_{\min}}}$.

Por las propiedades de la traza y el determinante de $M$, tenemos:
$$\mu_1 + \mu_2 = A + C, \qquad \mu_1 \mu_2 = AC - \frac{B^2}{4}$$

Por tanto:
$$\left(r + \frac{1}{r}\right)^2 = \frac{(\mu_1 + \mu_2)^2}{\mu_1 \mu_2} = \frac{(A + C)^2}{AC - B^2/4}$$

Como la función $r \mapsto \left(r + \frac{1}{r}\right)^2$ es estrictamente creciente para $r \ge 1$, minimizar $r$ equivale a minimizar la expresión anterior respecto a $C$. Sea $k = \frac{B^2}{4A}$ y hagamos el cambio de variable $u = C - k > 0$:
$$\frac{(A + C)^2}{AC - B^2/4} = \frac{(A + k + u)^2}{Au} = \frac{1}{A}\left(\frac{(A + k)^2}{u} + u + 2(A + k)\right)$$

Por la desigualdad entre las medias aritmética y geométrica (MA-MG), se cumple que $\frac{(A + k)^2}{u} + u \ge 2(A + k)$, alcanzándose la igualdad cuando $u = A + k$. El valor mínimo es:
$$\left(r + \frac{1}{r}\right)^2_{\min} = \frac{4(A + k)}{A} = 4 + \frac{4k}{A} = 4 + \frac{B^2}{A^2}$$

Restando $4$ en ambos miembros, obtenemos:
$$\left(r - \frac{1}{r}\right)^2 = \left(r + \frac{1}{r}\right)^2 - 4 = \frac{B^2}{A^2} \implies r - \frac{1}{r} = \frac{B}{A}$$

### Paso 4: Cálculo de $r$
Sustituyendo $A = 14$ y $B = 45$:
$$r - \frac{1}{r} = \frac{45}{14} \implies 14r^2 - 45r - 14 = 0$$

Resolvemos la ecuación cuadrática para $r \ge 1$:
$$r = \frac{45 + \sqrt{45^2 - 4(14)(-14)}}{2 \cdot 14} = \frac{45 + \sqrt{2025 + 784}}{28} = \frac{45 + \sqrt{2809}}{28} = \frac{45 + 53}{28} = \frac{98}{28} = \frac{7}{2}$$

\boxed{\frac{7}{2}}