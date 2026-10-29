## Solución

La suma es geométrica alternante:

$$\sum_{k=0}^{8}(-z)^k = \frac{1-(-z)^9}{1-(-z)} = \frac{1+z^9}{1+z}$$

Por tanto, las raíces satisfacen $z^9 = -1$ con $z \neq -1$.

Como $|z|^9 = 1$ implica $r = 1$, los argumentos son:

$$\theta = \frac{(2k+1)\pi}{9}, \quad k = 0,1,\dots,8$$

excluyendo $k=4$ (que da $\theta = \pi$, es decir $z=-1$).

Los valores son $\frac{\pi}{9}, \frac{3\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}, \frac{11\pi}{9}, \frac{13\pi}{9}, \frac{15\pi}{9}, \frac{17\pi}{9}$.

La suma de los numeradores: $(1+3+\cdots+17) - 9 = 81 - 9 = 72$, luego la suma es $\frac{72\pi}{9} = 8\pi$.

\boxed{8\pi}