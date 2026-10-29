Sea $w$ un número complejo con $|w| = 1$. Podemos escribir $w = e^{i\theta}$ para algún ángulo real $\theta$.

Primero, simplificamos el primer término de la expresión:
\[|1 + w| = |1 + e^{i\theta}| = \left|e^{i\theta/2}\left(e^{-i\theta/2} + e^{i\theta/2}\right)\right| = 2\left|\cos\left(\frac{\theta}{2}\right)\right|.\]

Ahora, simplificamos el segundo término factorizando $w$:
\[|2 - 2w + 2w^2| = 2|w| \cdot |w^{-1} - 1 + w| = 2|e^{-i\theta} + e^{i\theta} - 1| = 2|2\cos\theta - 1|.\]

Usando la identidad del ángulo doble $\cos\theta = 2\cos^2(\theta/2) - 1$, sea $x = |\cos(\theta/2)|$. Como $\theta$ es real, tenemos que $x \in [0, 1]$ y $\cos\theta = 2x^2 - 1$. Sustituyendo esto en nuestra expresión original, obtenemos una función de $x$:
\[f(x) = 2x + 2|2(2x^2 - 1) - 1| = 2x + 2|4x^2 - 3|.\]

Analizamos el valor máximo de $f(x)$ en el intervalo $[0, 1]$ dividiendo en dos casos según el signo de $4x^2 - 3$:

**Caso 1:** $4x^2 - 3 \ge 0$, es decir, $x \in \left[\frac{\sqrt{3}}{2}, 1\right]$.
En este intervalo, la función es:
\[f(x) = 2x + 2(4x^2 - 3) = 8x^2 + 2x - 6.\]
Dado que esta función es estrictamente creciente para $x > 0$, su máximo en este intervalo se alcanza en $x = 1$:
\[f(1) = 8(1)^2 + 2(1) - 6 = 4.\]

**Caso 2:** $4x^2 - 3 < 0$, es decir, $x \in \left[0, \frac{\sqrt{3}}{2}\right)$.
En este intervalo, la función es:
\[f(x) = 2x + 2(3 - 4x^2) = -8x^2 + 2x + 6.\]
Esta es una parábola que se abre hacia abajo, cuyo vértice se encuentra en:
\[x = -\frac{2}{2(-8)} = \frac{1}{8}.\]
Como $\frac{1}{8} \in \left[0, \frac{\sqrt{3}}{2}\right)$, el valor máximo en este intervalo se alcanza en $x = \frac{1}{8}$:
\[f\left(\frac{1}{8}\right) = -8\left(\frac{1}{8}\right)^2 + 2\left(\frac{1}{8}\right) + 6 = -\frac{1}{8} + \frac{1}{4} + 6 = 6 + \frac{1}{8} = \frac{49}{8}.\]

Comparando los valores máximos de ambos casos, vemos que $\frac{49}{8} > 4$.

\boxed{\frac{49}{8}}