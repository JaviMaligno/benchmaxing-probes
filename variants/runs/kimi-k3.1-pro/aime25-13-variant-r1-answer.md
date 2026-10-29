Al añadir un segmento que corta a los anteriores en \(k\) puntos interiores distintos, el número de regiones aumenta en \(k+1\). Los dos diámetros iniciales crean \(4\) regiones.

Numeremos los cuadrantes cíclicamente. Cada cuerda aleatoria tiene sus extremos en uno de los \(6\) pares no ordenados de cuadrantes distintos, todos equiprobables:

- En \(4\) pares los cuadrantes son adyacentes, y la cuerda corta exactamente un diámetro.
- En \(2\) pares son opuestos, y corta ambos diámetros.

Así, el número esperado de diámetros cortados por cada cuerda es
\[
d=\frac{4\cdot1+2\cdot2}{6}=\frac43.
\]

Dos cuerdas se cortan dentro del disco si y solo si sus extremos se alternan sobre la circunferencia. Considerando los \(36\) pares ordenados de tipos de cuadrantes para dos cuerdas:

- En \(30\) casos los pares de cuadrantes no son disjuntos, y la probabilidad de corte es \(\tfrac12\).
- En \(2\) casos son \(\{1,3\}\) y \(\{2,4\}\), y las cuerdas siempre se cortan.
- En los \(4\) casos restantes nunca se cortan.

Por tanto, la probabilidad de corte entre dos cuerdas aleatorias es
\[
p=\frac{30(\tfrac12)+2}{36}=\frac{17}{36}.
\]

Sumando los aumentos esperados de regiones:
\[
\mathbb E[R]
=4+16+16d+\binom{16}{2}p
=20+16\cdot\frac43+120\cdot\frac{17}{36}
=98.
\]

\[
\boxed{98}
\]