Para encontrar el número de cuatro dígitos $\underline{abcd}$, podemos expresar su valor posicional en función del primer dígito $a$ y del número formado por los últimos tres dígitos, al que llamaremos $x = \underline{bcd}$ (donde $0 \le x \le 999$ y $a \in \{1, 2, \dots, 9\}$).

De este modo, tenemos que:
$$\underline{abcd} = 1000a + x$$

Según el enunciado, las dos expresiones son iguales:
$$\sqrt{1000a + x} = a\sqrt{x}$$

Elevando ambos lados de la ecuación al cuadrado, obtenemos:
$$1000a + x = a^2x$$

Reorganizando los términos para despejar $x$:
$$1000a = (a^2 - 1)x$$
$$x = \frac{1000a}{a^2 - 1}$$

Dado que $x$ debe ser un número entero y que $\text{mcd}(a, a^2 - 1) = 1$, el término $a^2 - 1$ debe ser un divisor de $1000$. Evaluamos los posibles valores para el dígito $a \in \{1, 2, \dots, 9\}$:

- Si $a = 1$: $a^2 - 1 = 0$ (división no definida).
- Si $a = 2$: $a^2 - 1 = 3$ (no divide a $1000$).
- Si $a = 3$: $a^2 - 1 = 8$ (divide a $1000$, ya que $1000 / 8 = 125$).
- Si $a = 4$: $a^2 - 1 = 15$ (no divide a $1000$).
- Si $a = 5$: $a^2 - 1 = 24$ (no divide a $1000$).
- Si $a = 6$: $a^2 - 1 = 35$ (no divide a $1000$).
- Si $a = 7$: $a^2 - 1 = 48$ (no divide a $1000$).
- Si $a = 8$: $a^2 - 1 = 63$ (no divide a $1000$).
- Si $a = 9$: $a^2 - 1 = 80$ (no divide a $1000$).

El único valor válido es $a = 3$. Sustituyendo $a = 3$ en la ecuación para $x$:
$$x = \frac{1000 \cdot 3}{8} = 125 \cdot 3 = 375$$

Por lo tanto, $\underline{bcd} = 375$ y el número de cuatro dígitos $\underline{abcd}$ es $3375$.

\boxed{3375}