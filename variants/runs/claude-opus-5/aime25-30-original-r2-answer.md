## Planteamiento

Si el mínimo se alcanza en exactamente dos puntos $p,q>0$ con valor común $c$, entonces el polinomio

$$(x-18)(x-72)(x-98)(x-k) - cx$$

es mónico de grado 4 y tiene raíces dobles en $p$ y $q$, luego

$$(x-18)(x-72)(x-98)(x-k) - cx = (x-p)^2(x-q)^2.$$

## Comparación de coeficientes

Con $s=p+q$, $t=pq$, el lado derecho es $x^4-2sx^3+(s^2+2t)x^2-2stx+t^2$. El término lineal solo fija $c$, así que las condiciones útiles son:

- $x^3$: $\;188+k = 2s$
- $x^2$: $\;s^2+2t = 18\cdot72+18\cdot98+72\cdot98+188k = 10116+188k$
- $x^0$: $\;t^2 = 18\cdot72\cdot98\,k = 127008\,k$

De la última, como $t=pq>0$: $t=252\sqrt{2k}$. Sustituyendo $s=\frac{188+k}{2}$:

$$\frac{(188+k)^2}{4}+504\sqrt{2k}=10116+188k$$

$$k^2-376k-5120+2016\sqrt{2k}=0.$$

## Resolución

Con $k=2u^2$, $u>0$ (entonces $\sqrt{2k}=2u$):

$$4u^4-752u^2+4032u-5120=0 \;\Longrightarrow\; u^4-188u^2+1008u-1280=0.$$

Factorizando: $u=2$ y $u=4$ son raíces, y

$$u^4-188u^2+1008u-1280=(u-2)(u-4)(u^2+6u-160)=(u-2)(u-4)(u-10)(u+16).$$

Las raíces positivas son $u=2,4,10$, es decir

$$k=8,\quad k=32,\quad k=200,$$

exactamente tres valores positivos, como afirma el enunciado. Su suma es $8+32+200=240$.

\boxed{240}