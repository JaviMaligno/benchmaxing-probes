Este es un problema de optimización que puedo resolver directamente con desigualdades.

**Cota superior con AM-GM.** Para cualquier real $x$, aplicando la desigualdad de medias a los cuatro términos $x^4, 1, 1, 1$:

$$x^4 + 3 \ge 4\sqrt[4]{x^4} = 4|x|,$$

y análogamente $y^4 + 3 \ge 4|y|$. Sumando:

$$x^4 + y^4 + 6 \ge 4|x| + 4|y| \ge 4(x - y),$$

donde la última desigualdad vale porque $x - y \le |x| + |y|$.

Si $x - y \le 0$, la fracción es $\le 0$, que no puede ser el máximo. Si $x - y > 0$, el denominador siempre es positivo, así que:

$$\frac{x - y}{x^4 + y^4 + 6} \le \frac{x - y}{4(x - y)} = \frac{1}{4}.$$

**La cota se alcanza.** La igualdad en AM-GM requiere $x^4 = 1$ y $y^4 = 1$, y la igualdad $|x| + |y| = x - y$ requiere $x \ge 0$ y $y \le 0$. Con $x = 1$, $y = -1$:

$$\frac{1 - (-1)}{1 + 1 + 6} = \frac{2}{8} = \frac{1}{4}.$$

$$\boxed{\dfrac{1}{4}}$$