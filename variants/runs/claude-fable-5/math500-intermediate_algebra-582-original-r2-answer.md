Las raíces no son cero (x = 0 no satisface la ecuación), así que podemos dividir entre $x^{10}$:

$$\left(\frac{13x-1}{x}\right)^{10} = -1 \quad\Longrightarrow\quad \left(13 - \frac1x\right)^{10} = -1.$$

Entonces, para cada raíz $r$, se cumple $13 - \frac1r = \omega$, donde $\omega$ es una de las 10 raíces décimas de $-1$ (todas con $|\omega| = 1$). Es decir:

$$\frac1r = 13 - \omega.$$

Para cada raíz, el término que nos interesa es:

$$\frac{1}{r\overline{r}} = \frac1r \cdot \overline{\left(\frac1r\right)} = (13-\omega)(13-\overline{\omega}) = 169 - 13(\omega + \overline{\omega}) + |\omega|^2 = 170 - 26\,\operatorname{Re}(\omega).$$

Las 10 raíces décimas de $-1$ vienen en pares conjugados $\omega_k, \overline{\omega}_k$ (que corresponden a los pares $r_k, \overline{r}_k$), y su suma total es $0$ (son las raíces de $z^{10}+1=0$, cuyo coeficiente de $z^9$ es cero). Por lo tanto:

$$\sum_{\text{las }10\text{ raíces}} \operatorname{Re}(\omega) = 0 \quad\Longrightarrow\quad 2\sum_{k=1}^{5} \operatorname{Re}(\omega_k) = 0 \quad\Longrightarrow\quad \sum_{k=1}^{5} \operatorname{Re}(\omega_k) = 0.$$

Sumando sobre los 5 pares:

$$\sum_{k=1}^{5} \frac{1}{r_k\overline{r}_k} = \sum_{k=1}^{5}\bigl(170 - 26\,\operatorname{Re}(\omega_k)\bigr) = 5 \cdot 170 - 26 \cdot 0 = 850.$$

$$\boxed{850}$$