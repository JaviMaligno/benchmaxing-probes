## Solución

**Reescritura de la ecuación.** Sumo 4 a ambos lados, repartiendo un 1 a cada fracción:

$$\sum_{k=1}^{4}\left(\frac{k}{x^2-k}+1\right) = 2010x \quad\Longrightarrow\quad \sum_{k=1}^{4}\frac{x^2}{x^2-k} = 2010x.$$

Es decir,

$$x^2\sum_{k=1}^{4}\frac{1}{x^2-k} = 2010x.$$

**Forma polinómica.** Multiplicando la ecuación original por $\prod_{k=1}^{4}(x^2-k)$ se obtiene:

$$\sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j) = (2010x-4)\prod_{k=1}^{4}(x^2-k).$$

El lado izquierdo tiene grado 6, mientras que el derecho tiene grado 9. Al pasar todo a un lado, el polinomio resultante es de grado 9:

$$P(x) = (2010x-4)\prod_{k=1}^{4}(x^2-k) - \sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j) = 0.$$

**Coeficientes principales.** El producto $\prod_{k=1}^{4}(x^2-k) = x^8 - 10x^6 + \cdots$ solo tiene potencias pares, así que:

- Coeficiente de $x^9$: proviene de $2010x\cdot x^8$, es decir, $2010$.
- Coeficiente de $x^8$: proviene de $-4\cdot x^8$, es decir, $-4$ (el término $2010x$ multiplicado por potencias pares solo da potencias impares, y el lado izquierdo de grado 6 no contribuye).

**Vieta.** La suma de las 9 raíces complejas es:

$$-\frac{-4}{2010} = \frac{4}{2010} = \frac{2}{1005}.$$

(Ninguna raíz de $P$ coincide con $x^2=k$, pues sustituir $x^2=k$ en $P$ da $-k\prod_{j\neq k}(k-j)\neq 0$, así que las 9 raíces son soluciones genuinas de la ecuación original.)

$$\boxed{\dfrac{2}{1005}}$$