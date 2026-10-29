Voy a resolver el problema analíticamente y luego verificaré el resultado numéricamente.

**Paso 1: Parametrizar.** Como $|w|=1$, escribo $w = e^{i\theta}$ y sea $c = \cos\theta \in [-1,1]$.

**Paso 2: Simplificar el primer término.**
$$|1+w|^2 = (1+w)(1+\bar w) = 2 + 2\cos\theta \implies |1+w| = \sqrt{2(1+c)}.$$

**Paso 3: Simplificar el segundo término.** Como $|2-2w+2w^2| = 2|w^2-w+1|$ y $\bar w = w^{-1}$:
$$|w^2-w+1|^2 = (w^2-w+1)(w^{-2}-w^{-1}+1) = 3 + w^2 + w^{-2} - 2w - 2w^{-1}$$
$$= 3 + 2\cos 2\theta - 4\cos\theta = 1 + 4\cos^2\theta - 4\cos\theta = (2c-1)^2.$$
Entonces $|2-2w+2w^2| = 2|2c-1|$.

**Paso 4: Maximizar.** Hay que maximizar $f(c) = \sqrt{2(1+c)} + 2|2c-1|$ en $[-1,1]$.

- Si $c \ge \tfrac12$: $f(c) = \sqrt{2(1+c)} + 4c - 2$ es creciente ($f' > 0$), con máximo $f(1) = 4$.
- Si $c \le \tfrac12$: $f(c) = \sqrt{2(1+c)} + 2 - 4c$, que es cóncava. Con $f'(c) = \frac{1}{\sqrt{2(1+c)}} - 4 = 0$ se obtiene $\sqrt{2(1+c)} = \tfrac14$, es decir $c = -\tfrac{31}{32}$.

En ese punto: $|1+w| = \tfrac14$ y $|2-2w+2w^2| = 2\left|2\left(-\tfrac{31}{32}\right)-1\right| = \tfrac{47}{8}$, así que $f = \tfrac14 + \tfrac{47}{8} = \tfrac{49}{8} \approx 6.125$, que supera $f(-1) = 6$ y $f(1) = 4$.

Verifico numéricamente:A**\`**

```
6.12499999991854 2.890424803594424 -0.9687500025965552
6.125
```

La verificación numérica confirma el análisis: el máximo es $\approx 6.125$, alcanzado en $\cos\theta \approx -0.96875 = -\tfrac{31}{32}$.

**Resumen:** escribiendo $w = e^{i\theta}$ con $c=\cos\theta$, se tiene $|1+w| = \sqrt{2(1+c)}$ y $|w^2-w+1| = |2c-1|$, así que hay que maximizar $f(c) = \sqrt{2(1+c)} + 2|2c-1|$ en $[-1,1]$. En la rama $c \le \tfrac12$ la función es cóncava y $f'(c)=0$ da $c = -\tfrac{31}{32}$, con valor $\tfrac14 + \tfrac{47}{8} = \tfrac{49}{8}$; en la rama $c \ge \tfrac12$ el máximo es $f(1)=4$. Por lo tanto el máximo global es

$$\boxed{\dfrac{49}{8}}$$