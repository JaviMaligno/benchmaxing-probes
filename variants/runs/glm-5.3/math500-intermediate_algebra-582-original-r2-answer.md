# Resolución

**Paso 1: Despejar las raíces.**

De $x^{10} = -(13x-1)^{10}$, cada raíz satisface
$$x = \omega(13x-1), \qquad \omega^{10}=-1,$$
donde $\omega$ recorre las 10 raíces décimas de $-1$, es decir $\omega = e^{i\theta}$ con $\theta = \frac{(2k+1)\pi}{10}$, $k=0,\dots,9$. Despejando:
$$r_\omega = \frac{\omega}{13\omega - 1}.$$

**Paso 2: Calcular $r_\omega \overline{r_\omega}$.**

Como $|\omega|=1$, tenemos $\overline{\omega} = 1/\omega$, y la conjugada de $r_\omega$ es $r_{\overline{\omega}}$. Entonces:
$$r_\omega \overline{r_\omega} = \frac{\omega\overline{\omega}}{(13\omega-1)(13\overline{\omega}-1)} = \frac{1}{169 - 13(\omega+\overline{\omega}) + 1} = \frac{1}{170 - 26\cos\theta}.$$

Por tanto:
$$\frac{1}{r_\omega\overline{r_\omega}} = 170 - 26\cos\theta.$$

**Paso 3: Sumar sobre los 5 pares conjugados.**

Los 10 valores de $\theta$ son $\frac{(2k+1)\pi}{10}$ para $k=0,\dots,9$, que se agrupan en 5 pares $\{\theta, -\theta\}$. Cada par aporta un único término $170 - 26\cos\theta$:
$$\sum_{i=1}^{5}\frac{1}{r_i\overline{r_i}} = 5\cdot 170 - 26\Big[\cos\tfrac{\pi}{10} + \cos\tfrac{3\pi}{10} + \cos\tfrac{5\pi}{10} + \cos\tfrac{7\pi}{10} + \cos\tfrac{9\pi}{10}\Big].$$

**Paso 4: Verificar que el corchete se cancela.**

- $\cos\frac{\pi}{2} = 0$
- $\cos\frac{7\pi}{10} = -\cos\frac{3\pi}{10}$
- $\cos\frac{9\pi}{10} = -\cos\frac{\pi}{10}$

La suma de cosenos es $0$, así que:
$$\sum_{i=1}^{5}\frac{1}{r_i\overline{r_i}} = 850.$$

\boxed{850}