Sean los 18 segmentos: los 2 diámetros y las 16 cuerdas adicionales.

Cada vez que se añade una cuerda nueva, si esta corta a \(k\) segmentos anteriores en su interior, aumenta el número de regiones en \(k+1\). Como los dos diámetros iniciales dividen el disco en \(4\) regiones, el número esperado de regiones es

\[
4+16+\mathbb E[I_{\text{diág-cuerdas}}]+\mathbb E[I_{\text{cuerda-cuerda}}].
\]

1. **Intersecciones cuerda–diámetro.**  
   Fijado un diámetro, una cuerda lo corta si sus extremos están en semicírculos opuestos. Dados dos cuadrantes distintos, hay \(\binom42=6\) pares posibles no ordenados, y \(4\) de ellos unen un cuadrante superior con uno inferior. Así,

\[
p=\frac46=\frac23.
\]

Hay \(16\cdot 2=32\) pares cuerda–diámetro, luego

\[
\mathbb E[I_{\text{diág-cuerdas}}]=32\cdot\frac23=\frac{64}{3}.
\]

2. **Intersecciones cuerda–cuerda.**  
   Una cuerda une cuadrantes adyacentes con probabilidad \(\frac23\), y cuadrantes opuestos con probabilidad \(\frac13\). Analizando por casos:

   - Si la primera cuerda une cuadrantes adyacentes, la probabilidad condicional de cortar a la segunda es
     \[
     \frac23\cdot\frac38+\frac13\cdot\frac12=\frac5{12}.
     \]
   - Si la primera cuerda une cuadrantes opuestos, esa probabilidad condicional es
     \[
     \frac23\cdot\frac12+\frac13\cdot\frac34=\frac7{12}.
     \]

   Por tanto,

\[
p_{cc}=\frac23\cdot\frac5{12}+\frac13\cdot\frac7{12}
=\frac{17}{36}.
\]

Hay \(\binom{16}{2}=120\) pares de cuerdas, así que

\[
\mathbb E[I_{\text{cuerda-cuerda}}]
=120\cdot\frac{17}{36}
=\frac{170}{3}.
\]

3. **Número esperado de regiones.**

\[
\mathbb E[R]
=20+\frac{64}{3}+\frac{170}{3}
=20+78
=98.
\]

\[
\boxed{98}
\]