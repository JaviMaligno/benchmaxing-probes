## Planteamiento

Sea $x>0$ tal que:
- $P(F) = \frac{1}{6} + x$
- $P(\text{cara opuesta}) = \frac{1}{6} - x$
- Las otras cuatro caras: $\frac{1}{6}$ cada una

Esto es consistente, pues la suma de probabilidades sigue siendo $1$.

## Probabilidad de que la suma sea 7

Dos caras suman 7 exactamente cuando son valores opuestos. Si $F$ muestra el número $f$, entonces:

$$P(\text{suma}=7) = \sum_{a=1}^{6} P(a)\,P(7-a)$$

Los términos se agrupan así: dos términos involucran la pareja $\{f, 7-f\}$ (en ambos órdenes), y los cuatro restantes corresponden a caras con probabilidad $\frac{1}{6}$:

$$P = 2\left(\frac{1}{6}+x\right)\left(\frac{1}{6}-x\right) + 4\cdot\frac{1}{36}$$

$$P = 2\left(\frac{1}{36}-x^2\right) + \frac{4}{36} = \frac{6}{36} - 2x^2 = \frac{1}{6} - 2x^2$$

## Resolución

$$\frac{1}{6} - 2x^2 = \frac{71}{450}$$

Con $\frac{1}{6} = \frac{75}{450}$:

$$2x^2 = \frac{75-71}{450} = \frac{4}{450} = \frac{2}{225} \quad\Longrightarrow\quad x^2 = \frac{1}{225} \quad\Longrightarrow\quad x = \frac{1}{15}$$

Por tanto:

$$P(F) = \frac{1}{6} + \frac{1}{15} = \frac{5}{30} + \frac{2}{30} = \frac{7}{30}$$

Como $\gcd(7,30)=1$, tenemos $m=7$, $n=30$, de donde $m+n=37$.

\boxed{37}