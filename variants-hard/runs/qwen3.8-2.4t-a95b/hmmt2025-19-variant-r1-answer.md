

Sea \(H\) el hexágono regular, con vértices \(V_1,\dots,V_6\). Ignoramos casos de probabilidad cero, como que la recta pase exactamente por un vértice.

Una recta que pasa por dos puntos interiores de un hexágono convexo lo corta en una cuerda. Esa recta corta dos lados adyacentes si y sólo si corta los dos lados que inciden en algún vértice \(V_i\); equivalentemente, “corta” ese vértice del hexágono.

Sea \(T_i\) el triángulo formado por \(V_{i-1},V_i,V_{i+1}\). Si la cuerda corta los dos lados incidentes en \(V_i\), entonces toda la cuerda está contenida en \(T_i\), por convexidad. Por tanto, los dos puntos aleatorios deben estar en \(T_i\).

Recíprocamente, si ambos puntos están en \(T_i\), entonces dentro del triángulo \(T_i\) la recta puede cortar uno de los tres pares de lados posibles. El par deseado es el formado por los dos lados de \(T_i\) que también son lados del hexágono.

En cualquier triángulo, la probabilidad de que la recta determinada por dos puntos interiores uniformes corte un par de lados prefijado es \(1/3\). Esto se debe a que la propiedad es invariante bajo transformaciones afines, y en un triángulo equilátero los tres pares de lados son simétricos; además, siempre se corta exactamente un par de lados.

Así, para un vértice fijo \(V_i\),

\[
\mathbb{P}(E_i)=\left(\frac{|T_i|}{|H|}\right)^2\cdot \frac13.
\]

Si el lado del hexágono mide \(a\), entonces

\[
|T_i|=\frac12 a^2\sin 120^\circ=\frac{\sqrt3}{4}a^2,
\]

mientras que

\[
|H|=6\cdot \frac{\sqrt3}{4}a^2=\frac{3\sqrt3}{2}a^2.
\]

Por tanto,

\[
\frac{|T_i|}{|H|}=\frac16.
\]

Luego

\[
\mathbb{P}(E_i)=\left(\frac16\right)^2\cdot\frac13=\frac1{108}.
\]

Hay 6 vértices, y estos sucesos son mutuamente excluyentes salvo conjuntos de probabilidad cero. Por tanto, la probabilidad pedida es

\[
6\cdot \frac1{108}=\frac1{18}.
\]

\[
\boxed{\frac{1}{18}}
\]