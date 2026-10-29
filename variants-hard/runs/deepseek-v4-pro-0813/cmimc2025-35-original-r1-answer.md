Vamos a razonar paso a paso.

Sea $f$ una función uniformemente aleatoria de $\{1,2,\dots,25\}$ en sí mismo. Queremos calcular

$$
\mathbb{E}\left[\sum_{x=1}^{25}(f(f(x))-x)^2\right].
$$

Por linealidad de la esperanza, basta calcular $\mathbb{E}[(f(f(x))-x)^2]$ para un $x$ fijo y multiplicar por $25$.

Fijemos $x$. Sea $Y = f(x)$ y $Z = f(f(x)) = f(Y)$. Como $f$ es uniformemente aleatoria, $Y$ es uniforme en $\{1,\dots,25\}$, y condicionado a $Y=y$, $Z=f(y)$ es uniforme en $\{1,\dots,25\}$ e independiente de $x$.

Queremos $\mathbb{E}[(Z-x)^2]$. Como $Z$ es uniforme en $\{1,\dots,25\}$:

$$
\mathbb{E}[Z] = \frac{1+25}{2} = 13.
$$

$$
\mathbb{E}[Z^2] = \frac{1}{25}\sum_{k=1}^{25} k^2 = \frac{1}{25}\cdot \frac{25\cdot 26\cdot 51}{6} = \frac{26\cdot 51}{6} = 221.
$$

Entonces:

$$
\mathbb{E}[(Z-x)^2] = \mathbb{E}[Z^2] - 2x\,\mathbb{E}[Z] + x^2 = 221 - 26x + x^2.
$$

Ahora sumamos sobre $x=1,\dots,25$:

$$
\sum_{x=1}^{25}(221 - 26x + x^2) = 25\cdot 221 - 26\sum_{x=1}^{25}x + \sum_{x=1}^{25}x^2.
$$

Calculamos:

$$
\sum_{x=1}^{25}x = \frac{25\cdot 26}{2} = 325,
$$

$$
\sum_{x=1}^{25}x^2 = \frac{25\cdot 26\cdot 51}{6} = 5525.
$$

Por lo tanto:

$$
25\cdot 221 - 26\cdot 325 + 5525 = 5525 - 8450 + 5525 = 2600.
$$

La respuesta es:

$$
\boxed{2600}
$$