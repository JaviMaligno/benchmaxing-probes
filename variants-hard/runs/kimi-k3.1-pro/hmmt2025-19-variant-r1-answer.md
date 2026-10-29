Tomemos el lado del hexágono igual a \(1\), de modo que su área es
\[
A=\frac{3\sqrt3}{2}.
\]

1. **Agrupamos los pares de puntos según la recta que determinan.**  
   Si una recta corta al hexágono en una cuerda de longitud \(\ell\), al integrar las posiciones de los dos puntos sobre dicha cuerda aparece el factor
   \[
   \int_0^\ell\int_0^\ell |x-y|\,dx\,dy=\frac{\ell^3}{3}.
   \]
   Por tanto, usando la medida de rectas \(dp\,d\theta\), la probabilidad buscada es
   \[
   \frac{\displaystyle\int_{\text{rectas favorables}}\ell^3\,dp\,d\theta}
   {3A^2}.
   \]

2. **Consideramos las rectas que cortan los dos lados incidentes en un vértice fijo.**  
   Sean \(u,v\in[0,1]\) las distancias desde ese vértice hasta los puntos de intersección. Como los lados forman un ángulo de \(120^\circ\),
   \[
   \ell^2=u^2+v^2+uv.
   \]
   Un cálculo directo del jacobiano da
   \[
   dp\,d\theta=\frac{uv\sen^2(120^\circ)}{\ell^3}\,du\,dv,
   \]
   y por ello
   \[
   \ell^3\,dp\,d\theta=\frac34uv\,du\,dv.
   \]

3. La contribución de cada vértice es, pues,
   \[
   \frac34\int_0^1\int_0^1uv\,du\,dv
   =\frac34\cdot\frac14=\frac3{16}.
   \]
   Hay seis vértices, así que
   \[
   P=\frac{6\cdot \frac3{16}}{3\left(\frac{3\sqrt3}{2}\right)^2}
   =\frac{\frac98}{\frac{81}{4}}
   =\frac1{18}.
   \]

\[
\boxed{\dfrac{1}{18}}
\]