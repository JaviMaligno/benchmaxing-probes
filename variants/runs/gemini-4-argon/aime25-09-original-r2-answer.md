Para encontrar el punto de intersección en el cuarto cuadrante entre la parábola original y su imagen rotada, podemos aprovechar la simetría de la parábola y las propiedades de las rotaciones.

### Paso 1: Plantear las ecuaciones de los puntos de intersección
Sea $C$ la parábola original dada por la ecuación:
$$y = x^2 - 4 \implies x^2 = y + 4$$

Un punto $(x, y)$ pertenece a la parábola rotada $60^\circ$ en sentido antihorario alrededor del origen si y solo si, al rotar $(x, y)$ un ángulo de $60^\circ$ en sentido horario alrededor del origen, el punto resultante $(x_0, y_0)$ pertenece a la parábola original $C$.

Las coordenadas de $(x_0, y_0)$ vienen dadas por:
$$x_0 = x \cos(60^\circ) + y \sin(60^\circ) = \frac{1}{2}x + \frac{\sqrt{3}}{2}y$$
$$y_0 = -x \sin(60^\circ) + y \cos(60^\circ) = -\frac{\sqrt{3}}{2}x + \frac{1}{2}y$$

Como tanto $(x, y)$ como $(x_0, y_0)$ están en la parábola $C$, se cumple que:
$$x^2 = y + 4 \quad \text{y} \quad x_0^2 = y_0 + 4$$

Restando ambas ecuaciones, obtenemos:
$$x_0^2 - x^2 = y_0 - y$$

### Paso 2: Usar la invarianza de la distancia al origen
Dado que $(x_0, y_0)$ se obtiene rotando $(x, y)$ alrededor del origen, ambos puntos están a la misma distancia del origen:
$$x_0^2 + y_0^2 = x^2 + y^2 \implies x_0^2 - x^2 = -(y_0^2 - y^2) = -(y_0 - y)(y_0 + y)$$

Igualando las dos expresiones para $x_0^2 - x^2$:
$$y_0 - y = -(y_0 - y)(y_0 + y) \implies (y_0 - y)(y_0 + y + 1) = 0$$

Esto nos da dos casos posibles: $y_0 = y$ o $y_0 + y = -1$.

### Paso 3: Identificar el punto en el cuarto cuadrante
En el cuarto cuadrante tenemos $x > 0$ e $y < 0$. Analicemos el primer caso:
- **Caso 1 ($y_0 = y$):**
  Sustituyendo la expresión de $y_0$:
  $$-\frac{\sqrt{3}}{2}x + \frac{1}{2}y = y \implies y = -\sqrt{3}x$$
  (Geométricamente, como la parábola original es simétrica respecto al eje $y$, reflejar respecto al eje $y$ y luego rotar $60^\circ$ equivale a reflejar respecto a la recta $y = -\sqrt{3}x$, la cual pasa por el segundo y cuarto cuadrante).

  Sustituyendo $x = -\frac{y}{\sqrt{3}}$ (o $y = -\sqrt{3}x$) en la ecuación de la parábola $y = x^2 - 4$:
  $$x^2 + \sqrt{3}x - 4 = 0$$
  Como buscamos el punto en el cuarto cuadrante ($x > 0$ e $y < 0$), tomamos la raíz positiva para $x$:
  $$x = \frac{-\sqrt{3} + \sqrt{(\sqrt{3})^2 - 4(1)(-4)}}{2} = \frac{\sqrt{19} - \sqrt{3}}{2} > 0$$

  A partir de $y = -\sqrt{3}x$, calculamos la coordenada $y$:
  $$y = -\sqrt{3}\left(\frac{\sqrt{19} - \sqrt{3}}{2}\right) = \frac{3 - \sqrt{57}}{2} < 0$$

*(Nota: En el Caso 2, $y_0 + y = -1$ conduce a $\sqrt{3}x = 3y + 2$; si $y < 0$, la raíz negativa de $9y^2 + 9y - 8 = 0$ cumple $y < -1$, lo que implica $\sqrt{3}x = 3y + 2 < 0$, ubicando dicho punto en el tercer cuadrante y el otro en el primero).*

### Paso 4: Calcular $a + b + c$
Comparando $y = \frac{3 - \sqrt{57}}{2}$ con la forma $\frac{a - \sqrt{b}}{c}$, identificamos:
- $a = 3$
- $b = 57$
- $c = 2$

Aquí $a$, $b$ y $c$ son enteros positivos, y $\operatorname{mcd}(3, 2) = 1$. Por lo tanto:
$$a + b + c = 3 + 57 + 2 = 62$$

\boxed{62}