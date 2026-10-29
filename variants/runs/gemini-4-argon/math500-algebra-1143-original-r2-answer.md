Para encontrar la menor distancia $a$ entre el origen $(0,0)$ y un punto $(x, y)$ en la gráfica de $y = \frac{1}{2}x^2 - 9$, podemos minimizar el cuadrado de la distancia, $d^2 = x^2 + y^2$.

1. Despejamos $x^2$ de la ecuación de la parábola:
   $$y = \frac{1}{2}x^2 - 9 \implies x^2 = 2y + 18$$
   Dado que $x^2 \ge 0$, se debe cumplir que $y \ge -9$.

2. Sustituimos $x^2$ en la fórmula de la distancia al cuadrado:
   $$d^2 = (2y + 18) + y^2 = y^2 + 2y + 18$$

3. Completamos el cuadrado para hallar el valor mínimo de esta expresión cuadrática:
   $$d^2 = (y + 1)^2 - 1 + 18 = (y + 1)^2 + 17$$

4. Como $(y + 1)^2 \ge 0$ para todo número real $y$, el valor mínimo de $d^2$ se alcanza cuando $y = -1$. Verificamos que $y = -1$ cumple la condición $y \ge -9$ (en este punto, $x^2 = 2(-1) + 18 = 16$, por lo que $x = \pm 4$).

Por lo tanto, el valor mínimo del cuadrado de la distancia es $a^2 = 17$.

\boxed{17}