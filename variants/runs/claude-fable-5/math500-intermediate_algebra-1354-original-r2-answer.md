Este es un problema clásico de raíces de la unidad. Lo resuelvo emparejando términos.

**Observación clave:** como $\omega^{1997} = 1$, el último término es $\frac{1}{1+\omega^{1997}} = \frac{1}{2}$.

**Emparejamiento:** para $k = 1, \dots, 1996$, emparejo el término $k$ con el término $1997 - k$. Como $\omega^{1997-k} = \omega^{-k}$, tenemos:

$$\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{-k}} = \frac{1}{1+\omega^k} + \frac{\omega^k}{\omega^k+1} = \frac{1+\omega^k}{1+\omega^k} = 1.$$

(Nótese que $1 + \omega^k \neq 0$ para todo $k$, porque si $\omega^k = -1$ entonces $\omega^{2k} = 1$, lo que exigiría que $1997 \mid 2k$; como $1997$ es impar y primo, implicaría $1997 \mid k$, imposible para $1 \le k \le 1996$.)

**Suma total:** los índices $1$ a $1996$ forman $998$ parejas, cada una sumando $1$, más el término final $\frac{1}{2}$:

$$998 + \frac{1}{2} = \frac{1997}{2}.$$

$$\boxed{\dfrac{1997}{2}}$$