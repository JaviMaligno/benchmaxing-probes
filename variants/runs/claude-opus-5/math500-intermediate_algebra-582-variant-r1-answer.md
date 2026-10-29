## Planteamiento

Dividimos la ecuación entre $x^{10}$ (nótese que $x=0$ no es raíz):

$$1 + \left(\frac{11x-1}{x}\right)^{10} = 0 \quad\Longrightarrow\quad \left(11 - \frac1x\right)^{10} = -1.$$

Con el cambio $y = \dfrac1x$ queda $(11-y)^{10} = -1$, es decir

$$y = 11 - \zeta, \qquad \zeta^{10} = -1.$$

## Cálculo de la suma

Si $s$ es raíz, entonces $\frac1s = 11-\zeta$ y $\frac1{\bar s} = 11-\bar\zeta$, luego

$$\frac{1}{s\bar s} = |11-\zeta|^2 = 121 - 11(\zeta+\bar\zeta) + \zeta\bar\zeta = 122 - 22\,\mathrm{Re}(\zeta),$$

usando $|\zeta| = 1$.

Los diez valores de $\zeta$ se agrupan en cinco pares conjugados, y cada par da el mismo valor de $|11-\zeta|^2$. Por tanto la suma pedida es la mitad de la suma sobre las diez raíces:

$$\sum_{k=1}^{5}\frac{1}{s_k\bar s_k} = \frac12\sum_{\zeta^{10}=-1}\bigl(122 - 22\,\mathrm{Re}(\zeta)\bigr).$$

Como $\zeta^{10}+1=0$ no tiene término en $\zeta^9$, la suma de todas las raíces es $0$, y en particular $\sum \mathrm{Re}(\zeta) = 0$. Entonces

$$\frac12\bigl(10\cdot 122 - 22\cdot 0\bigr) = \frac{1220}{2} = 610.$$

$$\boxed{610}$$