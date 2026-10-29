## Resolución

**Paso 1: Transformar la ecuación con la sustitución $t = 1/x$.**

Como $x = 0$ no es raíz, divido la ecuación entre $x^{10}$:
$$1 + \left(11 - \frac{1}{x}\right)^{10} = 0.$$

Con $t = 1/x$, obtengo $(11 - t)^{10} = -1$.

**Paso 2: Describir las raíces en $t$.**

Entonces $11 - t = \omega$, donde $\omega$ recorre las 10 raíces décimas de $-1$. Es decir, los recíprocos de las raíces son
$$t_k = 11 - \omega_k, \qquad |\omega_k| = 1,\qquad \sum_{k=1}^{10}\omega_k = 0.$$

**Paso 3: Relacionar con la suma pedida.**

Observo que $\dfrac{1}{s\overline{s}} = \dfrac{1}{|s|^2} = |t|^2$ para cada raíz. La suma pedida recorre solo un representante de cada par conjugado, así que
$$\sum_{j=1}^{5}\frac{1}{s_j\overline{s}_j} = \frac{1}{2}\sum_{k=1}^{10} |t_k|^2.$$

**Paso 4: Calcular $\sum |t_k|^2$.**

$$|t_k|^2 = (11-\omega_k)(11-\overline{\omega}_k) = 121 - 11(\omega_k + \overline{\omega}_k) + |\omega_k|^2 = 122 - 22\,\mathrm{Re}(\omega_k).$$

Como las raíces de $\omega^{10} = -1$ suman cero, $\sum_k \mathrm{Re}(\omega_k) = 0$, y por tanto
$$\sum_{k=1}^{10} |t_k|^2 = 10 \cdot 122 = 1220.$$

**Paso 5: Dividir entre 2.**

$$\sum_{j=1}^{5}\frac{1}{s_j\overline{s}_j} = \frac{1220}{2} = 610.$$

$$\boxed{610}$$