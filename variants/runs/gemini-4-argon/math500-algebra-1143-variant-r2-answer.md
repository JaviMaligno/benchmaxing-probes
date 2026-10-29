Para encontrar la distancia más corta $b$ desde el origen $(0,0)$ hasta un punto $(x,y)$ en la parábola $y = \frac{1}{4}x^2 - 6$, expresamos el cuadrado de la distancia $d^2$ desde el origen a dicho punto:

$$d^2 = x^2 + y^2$$

De la ecuación de la parábola, podemos despejar $x^2$ en función de $y$:

$$y + 6 = \frac{1}{4}x^2 \implies x^2 = 4y + 24$$

Dado que $x^2 \ge 0$ para todo número real $x$, tenemos la restricción $4y + 24 \ge 0$, es decir, $y \ge -6$.

Sustituyendo $x^2$ en la fórmula de la distancia al cuadrado:

$$d^2(y) = (4y + 24) + y^2 = y^2 + 4y + 24$$

Completamos el cuadrado para hallar el valor mínimo de esta expresión cuadrática:

$$d^2(y) = (y + 2)^2 - 4 + 24 = (y + 2)^2 + 20$$

El valor mínimo de $(y + 2)^2 + 20$ se alcanza cuando $y = -2$. Como $y = -2$ cumple con la condición $y \ge -6$ (correspondiente a los puntos $(4, -2)$ y $(-4, -2)$ en la parábola), el valor mínimo de $d^2$ es $20$.

Por lo tanto, $b^2 = 20$.

\boxed{20}