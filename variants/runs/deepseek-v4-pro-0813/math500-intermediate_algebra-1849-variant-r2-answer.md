La ecuación está definida para valores reales si

\[
kx>0 \quad\text{y}\quad x+3>0.
\]

Usando la inyectividad del logaritmo:

\[
\log(kx)=2\log(x+3)=\log((x+3)^2)
\]

implica

\[
kx=(x+3)^2.
\]

Como \((x+3)^2>0\), la condición \(kx>0\) se cumple automáticamente si \(x+3>0\). Así que solo necesitamos que las soluciones de la cuadrática

\[
x^2+(6-k)x+9=0
\]

satisfagan \(x>-3\).

El discriminante es

\[
\Delta=(6-k)^2-36=k(k-12).
\]

- Si \(0<k<12\), no hay soluciones reales.
- Si \(k=12\), hay una raíz doble \(x=3\), que es válida. Cuenta como una solución.
- Si \(k=0\), el logaritmo no está definido, no cuenta.
- Si \(k>12\), las dos raíces son positivas, luego ambas cumplen \(x>-3\): hay dos soluciones.
- Si \(k<0\), la cuadrática tiene dos raíces reales negativas. Evaluando en \(x=-3\):

\[
Q(-3)=9-3(6-k)+9=3k<0,
\]

y como \(Q(0)=9>0\), una raíz está en \((-3,0)\), válida, y la otra es menor que \(-3\), no válida. Por tanto, hay exactamente una solución para cada entero negativo \(k\).

Los enteros \(k\) en \([-250,400]\) que funcionan son:

\[
-250,-249,\dots,-1
\]

que son \(250\) enteros, más \(k=12\).

Por lo tanto, el total es

\[
250+1=251.
\]

\[
\boxed{251}
\]