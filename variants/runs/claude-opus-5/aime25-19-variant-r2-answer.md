## Solución

**Simplificación del término general**

$$\frac{\log_k(7^{k^2-1})}{\log_{k+1}(7^{k^2-4})} = \frac{(k^2-1)\,\dfrac{\ln 7}{\ln k}}{(k^2-4)\,\dfrac{\ln 7}{\ln(k+1)}} = \frac{k^2-1}{k^2-4}\cdot\frac{\ln(k+1)}{\ln k}$$

**Parte logarítmica (telescópica)**

$$\prod_{k=3}^{80}\frac{\ln(k+1)}{\ln k} = \frac{\ln 81}{\ln 3} = \log_3 81 = 4$$

**Parte racional**

$$\frac{k^2-1}{k^2-4} = \frac{(k-1)(k+1)}{(k-2)(k+2)}$$

$$\prod_{k=3}^{80}\frac{k-1}{k-2} = \frac{2\cdot3\cdots79}{1\cdot2\cdots78} = 79, \qquad \prod_{k=3}^{80}\frac{k+1}{k+2} = \frac{4\cdot5\cdots81}{5\cdot6\cdots82} = \frac{4}{82} = \frac{2}{41}$$

Producto racional: $79\cdot\dfrac{2}{41} = \dfrac{158}{41}$.

**Total**

$$4\cdot\frac{158}{41} = \frac{632}{41}$$

Como $41$ es primo y no divide a $632$, la fracción es irreducible: $m=632$, $n=41$, luego $m+n=673$.

\boxed{673}