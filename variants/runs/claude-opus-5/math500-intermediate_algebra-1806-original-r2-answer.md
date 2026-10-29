## Planteamiento

Escribo $z = e^{i\theta}$, con $x = \cos\theta \in [-1,1]$.

**Primer término:**
$$|1+z|^2 = (1+z)(1+\bar z) = 2 + 2\cos\theta \implies |1+z| = \sqrt{2+2x}$$

**Segundo término:** como $|z| = 1$, puedo factorizar $z$:
$$|1 - z + z^2| = |z|\cdot\left|\tfrac{1}{z} - 1 + z\right| = |\bar z + z - 1| = |2\cos\theta - 1| = |2x-1|$$

Hay que maximizar $f(x) = \sqrt{2+2x} + |2x-1|$.

## Caso $x \ge 1/2$

$f(x) = \sqrt{2+2x} + 2x - 1$ es creciente, así que el máximo está en $x=1$:
$$f(1) = 2 + 1 = 3$$

## Caso $x < 1/2$

$f(x) = \sqrt{2+2x} + 1 - 2x$. Sustituyo $t = \sqrt{2+2x}$, de modo que $x = \frac{t^2-2}{2}$ y $t \in [0,\sqrt{3})$:
$$f = t + 1 - (t^2 - 2) = -t^2 + t + 3$$

Es una parábola invertida con vértice en $t = \tfrac12$:
$$f = -\tfrac14 + \tfrac12 + 3 = \tfrac{13}{4}$$

Ese valor es admisible: $t = \tfrac12$ corresponde a $2+2x = \tfrac14$, es decir $x = -\tfrac78 \in [-1, \tfrac12)$.

## Conclusión

Como $\tfrac{13}{4} = 3.25 > 3$, el máximo se alcanza con $\cos\theta = -\tfrac78$, dando $|1+z| = \tfrac12$ y $|1-z+z^2| = \tfrac{11}{4}$.

\boxed{\dfrac{13}{4}}