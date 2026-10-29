Para encontrar el valor máximo de la expresión $|1 + z| + |1 - z + z^2|$ sujeto a $|z| = 1$, podemos expresar $z$ en su forma polar como $z = e^{i\theta}$, donde $\theta \in [-\pi, \pi]$.

**Paso 1: Simplificar cada término en función de $\theta$.**

Para el primer término, factorizamos $e^{i\theta/2}$:
\[
|1 + z| = |1 + e^{i\theta}| = |e^{i\theta/2}(e^{-i\theta/2} + e^{i\theta/2})| = |e^{i\theta/2}| \cdot |2\cos(\theta/2)| = 2|\cos(\theta/2)|
\]

Para el segundo término, factorizamos $z = e^{i\theta}$ (recordando que $|z| = 1$):
\[
|1 - z + z^2| = |z| \cdot |z^{-1} - 1 + z| = |e^{-i\theta} - 1 + e^{i\theta}| = |2\cos\theta - 1|
\]

**Paso 2: Expresar la función en términos de una sola variable.**

Sea $x = |\cos(\theta/2)|$. Como $\theta \in [-\pi, \pi]$, tenemos que $x \in [0, 1]$.
Usando la identidad del ángulo doble $\cos\theta = 2\cos^2(\theta/2) - 1 = 2x^2 - 1$, sustituimos en el segundo término:
\[
|2\cos\theta - 1| = |2(2x^2 - 1) - 1| = |4x^2 - 3|
\]

Por lo tanto, queremos maximizar la función:
\[
f(x) = 2x + |4x^2 - 3| \quad \text{para } x \in [0, 1]
\]

**Paso 3: Analizar la función por intervalos.**

1. **Caso 1:** $4x^2 - 3 \ge 0$, lo que corresponde a $x \in \left[\frac{\sqrt{3}}{2}, 1\right]$.
   En este intervalo, la función es:
   \[
   f(x) = 4x^2 + 2x - 3
   \]
   Dado que $f(x)$ es estrictamente creciente para $x \ge 0$, su máximo en este intervalo se alcanza en el extremo derecho $x = 1$:
   \[
   f(1) = 4(1)^2 + 2(1) - 3 = 3
   \]

2. **Caso 2:** $4x^2 - 3 < 0$, lo que corresponde a $x \in \left[0, \frac{\sqrt{3}}{2}\right)$.
   En este intervalo, la función es:
   \[
   f(x) = 2x + 3 - 4x^2 = -4x^2 + 2x + 3
   \]
   Esta es una parábola que abre hacia abajo, cuyo vértice se encuentra en:
   \[
   x = -\frac{2}{2(-4)} = \frac{1}{4}
   \]
   Como $\frac{1}{4} \in \left[0, \frac{\sqrt{3}}{2}\right)$, evaluamos la función en el vértice:
   \[
   f\left(\frac{1}{4}\right) = -4\left(\frac{1}{4}\right)^2 + 2\left(\frac{1}{4}\right) + 3 = -\frac{1}{4} + \frac{1}{2} + 3 = \frac{13}{4}
   \]

**Paso 4: Comparar los valores máximos.**

Comparando los máximos obtenidos en ambos casos, vemos que $\frac{13}{4} = 3.25 > 3$.

\boxed{\frac{13}{4}}