El problema pide la suma de todos los posibles valores de $\theta$ para $z = re^{i\theta}$ (con $r>0$) que son raíces de

\[
z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0.
\]

El polinomio es una suma geométrica con razón $-z$:

\[
\frac{1 + z^9}{1+z}.
\]

Entonces la ecuación es

\[
\frac{z^9 + 1}{z+1} = 0,
\]

lo que implica

\[
z^9 = -1,
\qquad z \neq -1.
\]

Las soluciones de $z^9 = -1$ son

\[
z = e^{i\left(\frac{(2k+1)\pi}{9}\right)},
\qquad k=0,1,\dots,8.
\]

La única solución que corresponde a $z=-1$ es cuando $(2k+1)\pi/9 = \pi$, es decir $2k+1=9$, o sea $k=4$. Como $z\neq -1$, excluimos $k=4$.

Así, los posibles valores de $\theta$ son

\[
\theta_k = \frac{(2k+1)\pi}{9},
\qquad k=0,1,2,3,5,6,7,8.
\]

Los valores son:

\[
\frac{\pi}{9}, \frac{3\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}, \frac{11\pi}{9}, \frac{13\pi}{9}, \frac{15\pi}{9}, \frac{17\pi}{9}.
\]

Sumamos:

\[
\frac{\pi}{9}(1+3+5+7+11+13+15+17)
= \frac{\pi}{9} \cdot 72
= 8\pi.
\]

Por lo tanto, la suma de todos los posibles valores de $\theta$ es

\[
\boxed{8\pi}
\]