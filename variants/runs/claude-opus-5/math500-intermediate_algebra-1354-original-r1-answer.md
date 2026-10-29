## Planteamiento

Como $1997$ es primo y $\omega \neq 1$, las potencias $\omega, \omega^2, \dots, \omega^{1997}$ recorren **todas** las raíces 1997-ésimas de la unidad. Ninguna vale $-1$ (pues $(-1)^{1997}=-1\neq 1$), así que todos los denominadores son no nulos.

## Emparejamiento de términos

Agrupo el término $k$ con el término $1997-k$, para $k=1,\dots,1996$. Usando $\omega^{1997-k} = \omega^{-k}$:

$$\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{-k}} = \frac{1}{1+\omega^k} + \frac{\omega^k}{\omega^k+1} = \frac{1+\omega^k}{1+\omega^k} = 1.$$

Los índices $k=1,\dots,1996$ forman $998$ parejas disjuntas $\{k, 1997-k\}$ (no hay punto fijo, ya que $1997$ es impar), y cada pareja aporta $1$:

$$\sum_{k=1}^{1996} \frac{1}{1+\omega^k} = 998.$$

## Término restante

Queda $k=1997$, donde $\omega^{1997}=1$:

$$\frac{1}{1+\omega^{1997}} = \frac{1}{2}.$$

## Total

$$998 + \frac{1}{2} = \frac{1997}{2}.$$

$$\boxed{\dfrac{1997}{2}}$$