

Sea

\[
S=\sum_{k=1}^{1997}\frac{1}{1+\omega^k}.
\]

Como \(\omega^{1997}=1\), tenemos \(\omega^{1997-k}=\omega^{-k}\).

Además, ningún denominador se anula: si \(1+\omega^k=0\), entonces \(\omega^k=-1\), pero \((-1)^{1997}=-1\neq 1\), contradiciendo \((\omega^k)^{1997}=1\).

Para cada \(k=1,2,\dots,998\), emparejamos el término \(k\) con el término \(1997-k\):

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

Hay \(998\) pares, así que su contribución es \(998\).

Queda el término central \(k=1997\):

\[
\frac{1}{1+\omega^{1997}}=\frac{1}{1+1}=\frac12.
\]

Entonces,

\[
S=998+\frac12=\frac{1997}{2}.
\]

\[
\boxed{\frac{1997}{2}}
\]