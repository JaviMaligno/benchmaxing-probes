

Para que la gráfica de \(y=f(x)\) corte a toda recta horizontal, el rango de \(f\) debe ser todo \(\mathbb{R}\).

La función es

\[
f(x)=
\begin{cases}
ax^2, & x\ge a,\\
ax+2a, & x<a.
\end{cases}
\]

Consideramos el signo de \(a\).

### Caso 1: \(a>0\)

Para \(x\ge a\), como \(a>0\),

\[
ax^2 \ge a\cdot a^2 = a^3,
\]

así que el rango de esa parte es

\[
[a^3,\infty).
\]

Para \(x<a\), la función lineal \(ax+2a\) tiene pendiente positiva. Cuando \(x\to -\infty\), tiende a \(-\infty\), y cuando \(x\to a^{-}\), tiende a

\[
a^2+2a.
\]

Como \(x<a\) es estricto, ese valor no está incluido. El rango de esa parte es

\[
(-\infty, a^2+2a).
\]

Para cubrir todo \(\mathbb{R}\), necesitamos que los dos intervalos se toquen o se traslapen:

\[
a^3 \le a^2+2a.
\]

Como \(a>0\), dividimos entre \(a\):

\[
a^2 \le a+2
\]

\[
a^2-a-2 \le 0
\]

\[
(a-2)(a+1)\le 0.
\]

Con \(a>0\), esto da

\[
0<a\le 2.
\]

### Caso 2: \(a<0\)

Este caso también puede funcionar para algunos valores, pero buscamos el mayor valor de \(a\), así que basta comparar con el máximo obtenido en el caso positivo.

El mayor valor posible en el caso \(a>0\) es \(a=2\).

Comprobamos \(a=2\):

\[
f(x)=
\begin{cases}
2x^2, & x\ge 2,\\
2x+4, & x<2.
\end{cases}
\]

Para \(x\ge 2\), el rango es \([8,\infty)\).  
Para \(x<2\), el rango es \((-\infty,8)\).

La unión es todo \(\mathbb{R}\), por lo que \(a=2\) sí cumple.

\[
\boxed{2}
\]