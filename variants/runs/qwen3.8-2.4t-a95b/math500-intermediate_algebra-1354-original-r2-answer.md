

Sea \(n=1997\). Como \(\omega^{1997}=1\), tenemos \(\omega^{1997-k}=\omega^{-k}\).

Además, ningún denominador se anula: si \(1+\omega^k=0\), entonces \(\omega^k=-1\), pero eso implicaría que una potencia de \(\omega\) tiene orden \(2\), imposible porque el orden divide a \(1997\), que es impar.

Para cada \(k=1,2,\dots,1996\), emparejamos el término \(k\) con el término \(1997-k\):

\[
\frac{1}{1+\omega^k}+\frac{1}{1+\omega^{1997-k}}
=
\frac{1}{1+\omega^k}+\frac{1}{1+\omega^{-k}}.
\]

Ahora,

\[
\frac{1}{1+\omega^{-k}}
=
\frac{1}{1+\frac{1}{\omega^k}}
=
\frac{\omega^k}{1+\omega^k}.
\]

Por tanto,

\[
\frac{1}{1+\omega^k}+\frac{1}{1+\omega^{-k}}
=
\frac{1}{1+\omega^k}+\frac{\omega^k}{1+\omega^k}
=
1.
\]

Hay \(1996\) términos desde \(k=1\) hasta \(k=1996\), que forman \(998\) pares, cada uno con suma \(1\). Luego queda el término final:

\[
\frac{1}{1+\omega^{1997}}=\frac{1}{1+1}=\frac12.
\]

Así, la suma total es

\[
998+\frac12=\frac{1997}{2}.
\]

\[
\boxed{\frac{1997}{2}}
\]