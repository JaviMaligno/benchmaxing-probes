Para encontrar el valor de $k$, analicemos los puntos de intersección entre la recta horizontal $y = k$ y la familia de parábolas dadas.

**Paso 1: Contar el número de parábolas**
Las ecuaciones de las parábolas tienen la forma:
$$y = (x - 5n)^2$$
donde $5n$ toma los valores $0, 5, 10, \ldots, 45$. Esto corresponde a $n = 0, 1, 2, \ldots, 9$, por lo que hay un total de $10$ parábolas.

**Paso 2: Analizar las intersecciones con $y = k$**
- Si $k < 0$, la recta no interseca ninguna parábola ($0$ puntos).
- Si $k = 0$, la recta interseca cada parábola únicamente en su vértice, dando $10$ puntos distintos.
- Si $k > 0$, la recta $y = k$ corta a cada una de las $10$ parábolas en dos puntos:
  $$(x - 5n)^2 = k \implies x = 5n \pm \sqrt{k}$$

En principio, con $10$ parábolas y $2$ soluciones por parábola, hay un máximo de $2 \times 10 = 20$ puntos de intersección.

**Paso 3: Condición para tener exactamente $19$ puntos distintos**
Para que haya exactamente $19$ puntos distintos de intersección, exactamente dos de los $20$ puntos deben coincidir (es decir, una única superposición).

Todas las soluciones de la rama derecha ($x_n^+ = 5n + \sqrt{k}$) son distintas entre sí, y todas las de la rama izquierda ($x_m^- = 5m - \sqrt{k}$) también son distintas entre sí. Por lo tanto, una coincidencia solo puede darse cuando la rama derecha de la parábola $n$ coincide con la rama izquierda de la parábola $m$ (con $m > n$):
$$5n + \sqrt{k} = 5m - \sqrt{k}$$
$$2\sqrt{k} = 5(m - n) \implies \sqrt{k} = \frac{5(m - n)}{2}$$

Sea $d = m - n$ la diferencia entre los índices, donde $d \in \{1, 2, \ldots, 9\}$. El número de pares $(n, m)$ en $\{0, 1, \ldots, 9\}$ que cumplen $m - n = d$ es $10 - d$.

Para que ocurra **exactamente una** coincidencia, necesitamos que haya un solo par $(n, m)$, lo cual requiere:
$$10 - d = 1 \implies d = 9$$
(Esto corresponde únicamente al par $n = 0$ y $m = 9$, es decir, las parábolas $y = x^2$ y $y = (x - 45)^2$ intersecándose en su punto medio $x = 22.5$).

**Paso 4: Calcular $k$**
Sustituyendo $d = 9$ en la ecuación para $\sqrt{k}$:
$$\sqrt{k} = \frac{5 \times 9}{2} = \frac{45}{2}$$

Elevando al cuadrado ambos lados:
$$k = \left(\frac{45}{2}\right)^2 = \frac{2025}{4} = 506.25$$

\boxed{\frac{2025}{4}}