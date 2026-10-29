

Para que la ecuación

\[
\log(kx)=2\log(x+3)
\]

tenga sentido real, necesitamos

\[
kx>0 \quad \text{y} \quad x+3>0.
\]

Usando propiedades de logaritmos,

\[
2\log(x+3)=\log((x+3)^2),
\]

así que la ecuación equivale a

\[
\log(kx)=\log((x+3)^2).
\]

Como el logaritmo es inyectivo, esto implica

\[
kx=(x+3)^2.
\]

Reordenando,

\[
x^2+(6-k)x+9=0.
\]

Además, debemos respetar el dominio según el signo de \(k\):

- Si \(k>0\), entonces \(kx>0\) implica \(x>0\).
- Si \(k<0\), entonces \(kx>0\) implica \(x<0\), y junto con \(x>-3\), se requiere \(-3<x<0\).
- Si \(k=0\), no hay soluciones porque \(\log(0)\) no está definido.

Analicemos.

### Caso \(k>0\)

La ecuación cuadrática tiene raíces reales si

\[
\Delta=(6-k)^2-36=k(k-12)\ge 0.
\]

Como \(k>0\), esto ocurre cuando \(k\ge 12\).

Para \(k\ge 12\), el producto de las raíces es \(9>0\) y la suma es \(k-6>0\), así que ambas raíces son positivas.

- Si \(k=12\), hay una raíz doble: \(x=3\). Esto da exactamente una solución real.
- Si \(k>12\), hay dos raíces positivas distintas, así que hay dos soluciones reales.

Para \(1\le k\le 11\), no hay raíces reales.

Por tanto, entre los enteros positivos solo funciona

\[
k=12.
\]

### Caso \(k<0\)

Sea

\[
f(x)=x^2+(6-k)x+9.
\]

Evaluamos en los extremos del intervalo permitido \((-3,0)\):

\[
f(-3)=3k<0,
\]

porque \(k<0\), y

\[
f(0)=9>0.
\]

Por continuidad, hay al menos una raíz en \((-3,0)\).

Además, como \(k<0\), el discriminante

\[
\Delta=k(k-12)
\]

es positivo, así que hay dos raíces reales. El producto de las raíces es \(9>0\) y la suma es \(k-6<0\), por lo que ambas raíces son negativas.

Como \(f(-3)<0\) y \(f(x)\to +\infty\) cuando \(x\to -\infty\), la otra raíz está en \((-\infty,-3)\), fuera del dominio.

Por tanto, cada entero negativo \(k\) produce exactamente una solución real.

En el intervalo \([-250,400]\), los enteros negativos son

\[
-250,-249,\dots,-1,
\]

que son \(250\) enteros.

Agregando \(k=12\), obtenemos

\[
250+1=251.
\]

\[
\boxed{251}
\]