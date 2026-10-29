Tomemos un hexágono regular de lado \(1\); el resultado no depende de la escala.

Casi seguramente los dos puntos son distintos y la recta determinada corta al hexágono en una cuerda de longitud \(\ell\).

Para una recta con medida invariante \(d\mu=d\theta\,dp\), parametrizando dos puntos ordenados sobre ella se obtiene que su contribución es proporcional a

\[
\int_0^\ell\int_0^\ell |a-b|\,da\,db=\frac{\ell^3}{3}.
\]

Por tanto, si un evento depende solo de la recta, su probabilidad es

\[
\frac{\displaystyle\int_{\text{evento}}\ell^3\,d\mu}
{\displaystyle\int_{\text{todas las rectas}}\ell^3\,d\mu}.
\]

Ahora calculamos el numerador. Hay \(6\) pares de lados adyacentes. En uno de ellos, los lados forman un ángulo

\[
\alpha=120^\circ,
\]

y si los extremos de la cuerda están a distancias \(x,y\in[0,1]\) del vértice común, un cálculo jacobiano da

\[
d\mu=\frac{\sin^2\alpha\,xy}{\ell^3}\,dx\,dy.
\]

Por lo tanto,

\[
\ell^3\,d\mu=\sin^2(120^\circ)\,xy\,dx\,dy
=\frac34 xy\,dx\,dy.
\]

Así, la contribución de un par de lados adyacentes es

\[
\frac34\int_0^1\int_0^1 xy\,dx\,dy
=\frac34\cdot\frac14
=\frac{3}{16}.
\]

Multiplicando por los \(6\) pares adyacentes,

\[
\text{numerador}=6\cdot\frac{3}{16}=\frac{9}{8}.
\]

Para el denominador usamos el área del hexágono:

\[
K=6\cdot \frac{\sqrt3}{4}=\frac{3\sqrt3}{2}.
\]

Como

\[
K^2=\frac13\int \ell^3\,d\mu,
\]

tenemos

\[
\int \ell^3\,d\mu=3K^2
=3\cdot\frac{27}{4}
=\frac{81}{4}.
\]

Entonces la probabilidad es

\[
\frac{\frac{9}{8}}{\frac{81}{4}}
=\frac18\cdot\frac{4}{81}\cdot 9
=\frac{1}{18}.
\]

\[
\boxed{\frac{1}{18}}
\]