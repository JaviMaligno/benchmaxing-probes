## Solución

Como $x=0$ no es raíz, divido la ecuación entre $x^{10}$:

$$1+\left(\frac{13x-1}{x}\right)^{10}=0 \quad\Longrightarrow\quad \left(13-\frac{1}{x}\right)^{10}=-1.$$

Hago el cambio $w=\dfrac{1}{x}$. Entonces $13-w=\omega$, donde $\omega$ es cualquiera de las 10 raíces décimas de $-1$, todas con $|\omega|=1$. Es decir, los recíprocos de las raíces son

$$\frac{1}{r}=w=13-\omega.$$

Lo que se pide es

$$\sum_{k=1}^{5}\frac{1}{r_k\overline{r}_k}=\sum_{k=1}^{5}\left|\frac{1}{r_k}\right|^2,$$

que es la mitad de la suma sobre las **10** raíces (cada par conjugado aporta el mismo valor $|1/r|^2$). Calculo la suma completa:

$$\sum_{\omega^{10}=-1}|13-\omega|^2=\sum_{\omega}(13-\omega)(13-\overline{\omega})=\sum_{\omega}\left(169-13(\omega+\overline{\omega})+|\omega|^2\right).$$

Como las 10 raíces de $\omega^{10}=-1$ suman $0$ (y también sus conjugadas), los términos lineales se cancelan:

$$\sum_{\omega}|13-\omega|^2=10(169+1)=1700.$$

Por lo tanto, la suma pedida es la mitad:

$$\frac{1700}{2}=850.$$

$$\boxed{850}$$