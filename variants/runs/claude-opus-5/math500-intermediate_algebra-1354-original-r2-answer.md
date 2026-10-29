## Razonamiento

Como $1997$ es primo y $\omega \neq 1$, los valores $\omega, \omega^2, \dots, \omega^{1997}$ recorren **todas** las raíces 1997-ésimas de la unidad.

**Término final:** $\omega^{1997} = 1$, así que $\dfrac{1}{1+\omega^{1997}} = \dfrac{1}{2}$.

**Los demás términos se emparejan:** para $k = 1, \dots, 1996$, emparejamos $k$ con $1997-k$, notando que $\omega^{1997-k} = \omega^{-k}$:

$$\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{-k}} = \frac{1}{1+\omega^k} + \frac{\omega^k}{\omega^k+1} = \frac{1+\omega^k}{1+\omega^k} = 1.$$

Hay $1996$ términos, es decir $998$ parejas, cada una con suma $1$, lo que aporta $998$.

**Total:**
$$998 + \frac{1}{2} = \frac{1997}{2}.$$

$\boxed{\dfrac{1997}{2}}$