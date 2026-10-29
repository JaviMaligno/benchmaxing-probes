## Resolución

**Paso 1: Transformar la ecuación.** Como $x=0$ no es raíz, divido entre $x^{10}$:

$$1 + \left(\frac{11x-1}{x}\right)^{10} = 0 \quad\Longrightarrow\quad \left(11 - \frac{1}{x}\right)^{10} = -1.$$

**Paso 2: Cambio de variable.** Sea $y = \frac{1}{x}$. Entonces $11 - y = \omega$, donde $\omega$ es una raíz décima de $-1$ (es decir, $|\omega| = 1$). Así, los recíprocos de las raíces son

$$y = 11 - \omega,$$

con $\omega$ recorriendo las 10 raíces de $\omega^{10} = -1$.

**Paso 3: Expresar la suma pedida.** Observo que

$$\frac{1}{s_k \overline{s}_k} = \frac{1}{s_k}\cdot\overline{\left(\frac{1}{s_k}\right)} = |y_k|^2.$$

La suma sobre las **10** raíces (contando cada par conjugado dos veces) es:

$$\sum_{\omega^{10}=-1} (11-\omega)(11-\overline{\omega}) = \sum_{\omega} \left(121 - 11(\omega + \overline{\omega}) + |\omega|^2\right) = \sum_{\omega} \left(122 - 22\,\mathrm{Re}\,\omega\right).$$

**Paso 4: Usar la simetría.** Las 10 raíces décimas de $-1$ suman cero (son los ceros de $\omega^{10}+1$, cuyo coeficiente de $\omega^9$ es $0$), de modo que $\sum_\omega \mathrm{Re}\,\omega = 0$. Por lo tanto:

$$\sum_{\text{10 raíces}} \frac{1}{s\overline{s}} = 10 \cdot 122 = 1220.$$

**Paso 5: Ajustar el conteo.** La suma pedida solo incluye cada par conjugado **una vez** (nótese que $\frac{1}{s\overline{s}}$ toma el mismo valor para $s$ y para $\overline{s}$), así que es la mitad:

$$\frac{1220}{2} = 610.$$

$$\boxed{610}$$