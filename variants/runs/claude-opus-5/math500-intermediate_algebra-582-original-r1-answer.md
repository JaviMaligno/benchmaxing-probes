## Planteamiento

Como $x=0$ no es raíz, divido entre $x^{10}$:

$$1 + \left(\frac{13x-1}{x}\right)^{10} = 0 \quad\Longrightarrow\quad \left(13 - \frac1x\right)^{10} = -1.$$

Sea $y = \dfrac1x$. Entonces $13 - y = \zeta$, donde $\zeta$ recorre las diez raíces de $\zeta^{10} = -1$, es decir

$$\zeta_k = e^{i\pi(2k+1)/10},\qquad k=0,1,\dots,9.$$

Así $y = 13 - \zeta_k$, y las diez raíces $y$ vienen en pares conjugados igual que las $x$.

## Cálculo de cada término

Si $y_j = 1/r_j$, entonces $\overline{y}_j = 1/\overline{r}_j$, y por tanto

$$\frac{1}{r_j \overline{r}_j} = y_j \overline{y}_j = (13-\zeta)(13-\overline{\zeta}) = 169 - 13(\zeta + \overline{\zeta}) + |\zeta|^2 = 170 - 26\cos\theta,$$

con $\theta = \pi(2k+1)/10$ y $|\zeta| = 1$.

## Suma

Los cinco pares conjugados corresponden a los cinco $\zeta$ del semiplano superior, con ángulos $\theta = \frac{\pi}{10}, \frac{3\pi}{10}, \frac{5\pi}{10}, \frac{7\pi}{10}, \frac{9\pi}{10}$. Estos ángulos son simétricos respecto de $\pi/2$, de modo que sus cosenos se cancelan por pares ($\cos\frac{\pi}{10} = -\cos\frac{9\pi}{10}$, $\cos\frac{3\pi}{10} = -\cos\frac{7\pi}{10}$, $\cos\frac{5\pi}{10}=0$):

$$\sum \cos\theta = 0.$$

Por lo tanto

$$\sum_{j=1}^{5} \frac{1}{r_j \overline{r}_j} = 5\cdot 170 - 26\cdot 0 = 850.$$

\boxed{850}