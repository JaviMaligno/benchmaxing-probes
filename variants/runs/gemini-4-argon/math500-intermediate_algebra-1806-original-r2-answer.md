Para hallar el valor máximo de la expresión dada, podemos utilizar la forma trigonométrica de un número complejo de módulo $1$.

**Paso 1: Expresar $z$ en forma exponencial/trigonométrica**
Como $|z| = 1$, podemos escribir $z = e^{i\theta} = \cos\theta + i\sin\theta$ para algún ángulo $\theta \in [-\pi, \pi]$.

Calculamos cada término de la suma utilizando el hecho de que $|w| = |w \cdot e^{-i\alpha}|$ para cualquier $\alpha \in \mathbb{R}$:

1. Para el primer término:
   $$|1 + z| = |e^{-i\theta/2}(1 + e^{i\theta})| = |e^{-i\theta/2} + e^{i\theta/2}| = \left|2\cos\left(\frac{\theta}{2}\right)\right|$$

2. Para el segundo término:
   $$|1 - z + z^2| = |z^{-1}(1 - z + z^2)| = |z^{-1} - 1 + z| = |e^{-i\theta} + e^{i\theta} - 1| = |2\cos\theta - 1|$$

**Paso 2: Expresar la suma en términos de una sola variable**
Sea $t = |1 + z| = 2\left|\cos\left(\frac{\theta}{2}\right)\right|$. Dado que $\left|\cos\left(\frac{\theta}{2}\right)\right| \in [0, 1]$, tenemos que $t \in [0, 2]$.

Usando la identidad del ángulo doble $\cos\theta = 2\cos^2\left(\frac{\theta}{2}\right) - 1$, podemos escribir:
$$2\cos\theta = 4\cos^2\left(\frac{\theta}{2}\right) - 2 = t^2 - 2$$

Sustituyendo esto en el segundo término:
$$|1 - z + z^2| = |2\cos\theta - 1| = |t^2 - 3|$$

Por lo tanto, queremos maximizar la función:
$$f(t) = t + |t^2 - 3| \quad \text{para } t \in [0, 2]$$

**Paso 3: Analizar por casos en el intervalo $[0, 2]$**

- **Caso 1: $t \in [0, \sqrt{3}]$**
  En este intervalo, $t^2 - 3 \le 0$, por lo que $|t^2 - 3| = 3 - t^2$. La función es:
  $$f(t) = t + 3 - t^2 = -\left(t - \frac{1}{2}\right)^2 + \frac{13}{4}$$
  Esta parábola abre hacia abajo y alcanza su vértice en $t = \frac{1}{2}$. Como $\frac{1}{2} \in [0, \sqrt{3}]$, el valor máximo en este intervalo es $\frac{13}{4}$.

- **Caso 2: $t \in [\sqrt{3}, 2]$**
  En este intervalo, $t^2 - 3 \ge 0$, por lo que $|t^2 - 3| = t^2 - 3$. La función es:
  $$f(t) = t^2 + t - 3$$
  Como $f(t)$ es estrictamente creciente para $t > 0$, su valor máximo en $[\sqrt{3}, 2]$ se alcanza en el extremo $t = 2$:
  $$f(2) = 2^2 + 2 - 3 = 3$$

**Conclusión:**
Comparando los máximos de ambos intervalos, dado que $\frac{13}{4} = 3.25 > 3$, el valor máximo absoluto es $\frac{13}{4}$.

\boxed{\frac{13}{4}}