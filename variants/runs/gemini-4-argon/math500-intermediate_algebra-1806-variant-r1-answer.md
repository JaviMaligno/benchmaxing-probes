Para encontrar el valor máximo de la expresión dada, primero factorizamos el segundo término y utilizamos el hecho de que $|w| = 1.$

Sea $w = e^{i\theta}$ para algún ángulo $\theta \in [-\pi, \pi].$ 

Analizamos el primer término de la suma:
\[|1 + w| = |1 + e^{i\theta}| = |e^{i\theta/2}(e^{-i\theta/2} + e^{i\theta/2})| = |e^{i\theta/2}| \cdot |2\cos(\theta/2)| = 2|\cos(\theta/2)|.\]

Ahora analizamos el segundo término. Como $|w| = 1,$ podemos dividir por $|w|$ sin alterar el módulo:
\[|2 - 2w + 2w^2| = 2|1 - w + w^2| = 2\left|\frac{1}{w} - 1 + w\right| = 2|e^{-i\theta} - 1 + e^{i\theta}| = 2|2\cos\theta - 1|.\]

Usando la identidad del ángulo doble $\cos\theta = 2\cos^2(\theta/2) - 1,$ podemos reescribir $2\cos\theta - 1$ en función de $\cos(\theta/2)$:
\[2\cos\theta - 1 = 2(2\cos^2(\theta/2) - 1) - 1 = 4\cos^2(\theta/2) - 3.\]

Definimos la variable $x = |\cos(\theta/2)|.$ Dado que $\theta \in [-\pi, \pi],$ tenemos que $x \in [0, 1].$ Sustituyendo $x$ en la expresión original, obtenemos la función a maximizar en el intervalo $[0, 1]$:
\[f(x) = 2x + 2|4x^2 - 3|.\]

Dividimos el análisis en dos casos según el signo de $4x^2 - 3$:

**Caso 1:** $4x^2 - 3 \ge 0,$ lo que corresponde a $x \in \left[\frac{\sqrt{3}}{2}, 1\right].$
En este intervalo, la función es:
\[f(x) = 2x + 2(4x^2 - 3) = 8x^2 + 2x - 6.\]
Como $f(x)$ es estrictamente creciente para $x > 0,$ su máximo en este intervalo se alcanza en el extremo derecho $x = 1$:
\[f(1) = 8(1)^2 + 2(1) - 6 = 4.\]

**Caso 2:** $4x^2 - 3 < 0,$ lo que corresponde a $x \in \left[0, \frac{\sqrt{3}}{2}\right).$
En este intervalo, la función es:
\[f(x) = 2x + 2(3 - 4x^2) = -8x^2 + 2x + 6.\]
Esta es una parábola cóncava hacia abajo cuyo vértice se encuentra en:
\[x = -\frac{2}{2(-8)} = \frac{1}{8}.\]
Como $\frac{1}{8} \in \left[0, \frac{\sqrt{3}}{2}\right),$ el valor máximo en este intervalo se alcanza en $x = \frac{1}{8}$:
\[f\left(\frac{1}{8}\right) = -8\left(\frac{1}{8}\right)^2 + 2\left(\frac{1}{8}\right) + 6 = -\frac{1}{8} + \frac{1}{4} + 6 = \frac{49}{8}.\]

Comparando los valores máximos de ambos casos ($4$ y $\frac{49}{8} = 6.125$), concluimos que el valor máximo absoluto es $\frac{49}{8}.$

\boxed{\frac{49}{8}}