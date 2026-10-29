Sea

\[
t=\frac{x}{11x-1}.
\]

Como \(x=\frac1{11}\) no es raíz, esta transformación es válida en las raíces. La ecuación se convierte en

\[
t^{10}=-1.
\]

Los diez valores de \(t\) son las raíces de \(t^{10}+1=0\), y cada raíz \(x\) correspondiente es

\[
x=\frac{t}{11t-1}.
\]

Como los coeficientes de esta expresión son reales, los pares conjugados de \(x\) vienen de pares conjugados de \(t\). Además \(|t|=1\), así que para cada par

\[
x\overline{x}
=\frac{t}{11t-1}\cdot \frac{\overline t}{11\overline t-1}
=\frac{1}{|11t-1|^2}.
\]

Por lo tanto,

\[
\frac1{x\overline{x}}=|11t-1|^2.
\]

Ahora,

\[
|11t-1|^2=(11t-1)(11\overline t-1)
=122-11(t+\overline t).
\]

Sumando sobre los cinco pares conjugados, los términos \(t+\overline t\) recorren todas las diez raíces de \(t^{10}+1=0\). Su suma total es \(0\), porque el coeficiente de \(t^9\) en \(t^{10}+1\) es \(0\). Así,

\[
\sum_{i=1}^5 \frac1{s_i\overline{s_i}}
=5\cdot 122=610.
\]

\[
\boxed{610}
\]