Queremos maximizar $\dfrac{x-y}{x^4+y^4+6}$.

**Paso 1: Acotar el denominador.** Por la desigualdad AM–GM aplicada a cuatro términos:
$$x^4 + 1 + 1 + 1 \ge 4\sqrt[4]{x^4} = 4|x|,$$
es decir, $x^4 + 3 \ge 4|x|$, y análogamente $y^4 + 3 \ge 4|y|$.

**Paso 2: Sumar ambas desigualdades.**
$$x^4 + y^4 + 6 \ge 4|x| + 4|y| \ge 4(x - y),$$
ya que $x - y \le |x| + |y|$.

**Paso 3: Concluir.** Para que la fracción sea máxima nos interesa $x - y > 0$, y en ese caso:
$$\frac{x-y}{x^4+y^4+6} \le \frac{x-y}{4(x-y)} = \frac{1}{4}.$$

**Paso 4: Verificar que se alcanza la igualdad.** Necesitamos $x^4 = 1$, $y^4 = 1$, y que $x \ge 0$, $y \le 0$ (para que $|x|+|y| = x - y$). Tomando $x = 1$, $y = -1$:
$$\frac{1 - (-1)}{1 + 1 + 6} = \frac{2}{8} = \frac{1}{4}. \checkmark$$

$$\boxed{\dfrac{1}{4}}$$