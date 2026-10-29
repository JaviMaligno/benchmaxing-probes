Los casos degenerados (extremos exactamente en un diámetro, tres segmentos concurrentes, etc.) tienen probabilidad \(0\), así que no afectan la esperanza.

Si un segmento nuevo corta a los ya existentes en \(k\) puntos interiores, queda dividido en \(k+1\) trozos y crea \(k+1\) regiones nuevas. Los dos diámetros iniciales dejan \(4\) regiones.

**Intersecciones con los diámetros.** Para cada cuerda aleatoria, las \(6\) parejas no ordenadas de cuadrantes son igualmente probables: \(4\) adyacentes y \(2\) opuestas. Si une cuadrantes adyacentes cruza exactamente \(1\) diámetro; si une cuadrantes opuestos cruza \(2\). Por cuerda,

\[
\frac46\cdot 1+\frac26\cdot 2=\frac43.
\]

En \(25\) cuerdas esto da

\[
25\cdot \frac43=\frac{100}{3}.
\]

**Intersecciones entre dos cuerdas aleatorias.** Dos cuerdas se cruzan en el interior exactamente cuando sus cuatro extremos se alternan en la circunferencia.

Numerando los cuadrantes \(0,1,2,3\) en orden circular, hay \(6\) tipos de cuerda y \(36\) pares ordenados de tipos:

- \(2\) pares son tipos opuestos distintos, como \(\{0,2\}\) y \(\{1,3\}\): siempre se cruzan.
- \(4\) pares son tipos adyacentes sin cuadrante común, como \(\{0,1\}\) y \(\{2,3\}\): nunca se cruzan.
- Los otros \(30\) pares tienen probabilidad \(\frac12\) de cruzarse, pues el orden circular depende de un orden aleatorio dentro de un cuadrante compartido.

Por lo tanto,

\[
p=\frac{2\cdot 1+4\cdot 0+30\cdot \frac12}{36}
=\frac{17}{36}.
\]

Así, el número esperado de intersecciones entre cuerdas aleatorias es

\[
\binom{25}{2}\cdot \frac{17}{36}
=300\cdot \frac{17}{36}
=\frac{425}{3}.
\]

Finalmente,

\[
\mathbb E[R]
=4+25+\frac{100}{3}+\frac{425}{3}
=204.
\]

\[
\boxed{204}
\]