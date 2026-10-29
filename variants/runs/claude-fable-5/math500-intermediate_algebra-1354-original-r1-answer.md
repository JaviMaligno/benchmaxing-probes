## Solución

**Paso 1: Observar el último término.**
Como $\omega^{1997} = 1$, el último término es
$$\frac{1}{1 + \omega^{1997}} = \frac{1}{1+1} = \frac{1}{2}.$$

**Paso 2: Emparejar los términos restantes.**
Dado que 1997 es primo y $\omega \neq 1$, $\omega$ es una raíz primitiva 1997-ésima de la unidad, así que $\omega^k \neq 1$ para $k = 1, \dots, 1996$. Emparejamos el término $k$ con el término $1997 - k$, notando que $\omega^{1997-k} = \omega^{-k}$:

$$\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{-k}} = \frac{1}{1+\omega^k} + \frac{\omega^k}{\omega^k+1} = \frac{1+\omega^k}{1+\omega^k} = 1.$$

**Paso 3: Contar las parejas.**
Los índices $k = 1, \dots, 1996$ forman $\frac{1996}{2} = 998$ parejas, cada una con suma $1$.

**Paso 4: Sumar todo.**
$$998 \cdot 1 + \frac{1}{2} = \frac{1997}{2}.$$

$$\boxed{\dfrac{1997}{2}}$$