

Numeramos los cuadrantes cíclicamente como \(1,2,3,4\). Ignoramos casos degenerados de probabilidad cero (extremos coincidentes, cuerdas que pasan por el centro, tres segmentos concurrentes, etc.).

Al añadir un segmento que corta a los anteriores en \(k\) puntos interiores, el segmento queda dividido en \(k+1\) trozos, y cada trozo divide una región existente. Por tanto, aumenta el número de regiones en \(k+1\).

Los dos diámetros iniciales dividen el disco en \(4\) regiones. Luego, al añadir las \(16\) cuerdas aleatorias,

\[
\mathbb{E}[R]
=4+16+\mathbb{E}[\text{cortes con los diámetros}]
+\mathbb{E}[\text{cruces entre cuerdas}].
\]

Cada cuerda elige un par de cuadrantes no ordenado uniformemente entre los \(\binom{4}{2}=6\) pares posibles. Hay \(4\) pares adyacentes y \(2\) pares opuestos, así que

\[
P(\text{adyacentes})=\frac{2}{3},\qquad P(\text{opuestos})=\frac{1}{3}.
\]

- Si los cuadrantes son adyacentes, la cuerda cruza exactamente \(1\) diámetro.
- Si son opuestos, cruza los \(2\) diámetros.

Por tanto, el número esperado de cruces con diámetros por cuerda es

\[
\frac{2}{3}\cdot 1+\frac{1}{3}\cdot 2=\frac{4}{3}.
\]

Para \(16\) cuerdas:

\[
\mathbb{E}[\text{cortes con diámetros}]=16\cdot \frac{4}{3}=\frac{64}{3}.
\]

Ahora calculamos la probabilidad \(p\) de que dos cuerdas aleatorias se crucen.

Si la primera cuerda une cuadrantes adyacentes, digamos \(\{1,2\}\), entonces para la segunda cuerda hay \(6\) pares de cuadrantes posibles:

- Con \(\{3,4\}\), no hay cruce: probabilidad \(0\).
- Con los otros \(5\) pares, el cruce depende de una comparación de orden equiprobable entre extremos dentro de algún cuadrante compartido, así que la probabilidad es \(1/2\).

Entonces

\[
p_{\text{ady}}=\frac{0+5\cdot \frac12}{6}=\frac{5}{12}.
\]

Si la primera cuerda une cuadrantes opuestos, digamos \(\{1,3\}\):

- Con \(\{2,4\}\), los cuadrantes alternan y el cruce es seguro: probabilidad \(1\).
- Con los otros \(5\) pares, la probabilidad de cruce es \(1/2\).

Entonces

\[
p_{\text{op}}=\frac{1+5\cdot \frac12}{6}=\frac{7}{12}.
\]

Como la primera cuerda es adyacente con probabilidad \(2/3\) y opuesta con probabilidad \(1/3\),

\[
p=\frac{2}{3}\cdot \frac{5}{12}+\frac{1}{3}\cdot \frac{7}{12}
=\frac{17}{36}.
\]

El número esperado de cruces entre pares de cuerdas es

\[
\binom{16}{2}\cdot \frac{17}{36}
=120\cdot \frac{17}{36}
=\frac{170}{3}.
\]

Finalmente,

\[
\mathbb{E}[R]
=4+16+\frac{64}{3}+\frac{170}{3}
=20+\frac{234}{3}
=20+78
=98.
\]

\[
\boxed{98}
\]