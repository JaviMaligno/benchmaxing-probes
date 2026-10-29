# Resolución

**Paso 1: Reducir la cuártica con la sustitución palindrómica.**

El polinomio es recíproco (palindrómico). Como $x=0$ nunca es raíz (el término constante es 1), dividimos entre $x^2$:

$$x^2 + \frac{1}{x^2} + 2p\left(x + \frac{1}{x}\right) - q = 0.$$

Sea $t = x + \frac{1}{x}$. Entonces $x^2 + \frac{1}{x^2} = t^2 - 2$, y la ecuación se convierte en:

$$t^2 + 2pt - (q + 2) = 0.$$

**Paso 2: Condición sobre $t$.**

Para $x$ real (con $x \neq 0$), $t = x + \frac{1}{x}$ recorre exactamente $|t| \ge 2$. Recíprocamente, todo $t$ con $|t|\ge 2$ proviene de alguna $x$ real. Por lo tanto, la cuártica tiene raíz real si y solo si la ecuación cuadrática en $t$ tiene una raíz con $|t| \ge 2$.

Su discriminante es $4(p^2 + q + 2) > 0$ siempre (con $q \ge 0$), así que las raíces son reales:

$$t = -p \pm \sqrt{p^2 + q + 2}.$$

**Paso 3: Analizar cada raíz (con $p, q \ge 0$).**

- Raíz $t_1 = -p + \sqrt{p^2+q+2} \ge 2$ exigiría $\sqrt{p^2+q+2} \ge p+2$, es decir $q \ge 4p+2 \ge 2$; imposible pues $q \le 1$.
- Raíz $t_2 = -p - \sqrt{p^2+q+2} \le -2$ exige $p + \sqrt{p^2+q+2} \ge 2$. Si $p \ge 2$ es automático; si $p < 2$, al elevar al cuadrado:

$$p^2 + q + 2 \ge (2-p)^2 \iff q \ge 2 - 4p.$$

**Paso 4: Describir la región $T$ en el cuadrado $[0,1]^2$.**

- Si $p \ge \frac{1}{2}$: entonces $2 - 4p \le 0$, así que **todo** $q \in [0,1]$ sirve.
- Si $0 \le p < \frac{1}{2}$: se necesita $q \ge 2 - 4p$, y además $q \le 1$ exige $p \ge \frac{1}{4}$.

**Paso 5: Calcular el área.**

$$\text{Área} = \underbrace{\int_{1/2}^{1} 1\, dp}_{=\,1/2} \;+\; \int_{1/4}^{1/2} \bigl(1 - (2-4p)\bigr)\, dp = \frac{1}{2} + \int_{1/4}^{1/2} (4p-1)\,dp.$$

$$\int_{1/4}^{1/2} (4p-1)\,dp = \left[2p^2 - p\right]_{1/4}^{1/2} = \left(\frac{1}{2} - \frac{1}{2}\right) - \left(\frac{1}{8} - \frac{1}{4}\right) = \frac{1}{8}.$$

$$\text{Área} = \frac{1}{2} + \frac{1}{8} = \frac{5}{8}.$$

\boxed{\dfrac{5}{8}}