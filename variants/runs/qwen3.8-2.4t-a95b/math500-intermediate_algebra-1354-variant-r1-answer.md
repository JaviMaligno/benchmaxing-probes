

Sea

\[
S=\sum_{k=1}^{2027}\frac{1}{1+z^k}.
\]

Como \(z^{2027}=1\) y \(2027\) es impar, ningún denominador se anula: si \(z^k=-1\), entonces elevando a \(2027\),

\[
1=(z^{2027})^k=z^{2027k}=(-1)^{2027}=-1,
\]

una contradicción.

Ahora emparejamos los términos \(k\) y \(2027-k\). Como

\[
z^{2027-k}=z^{2027}z^{-k}=z^{-k},
\]

tenemos, para cada \(k=1,\dots,1013\),

\[
\frac{1}{1+z^k}+\frac{1}{1+z^{2027-k}}
=
\frac{1}{1+z^k}+\frac{1}{1+z^{-k}}.
\]

Pero

\[
\frac{1}{1+z^{-k}}=\frac{z^k}{1+z^k},
\]

así que cada par suma

\[
\frac{1}{1+z^k}+\frac{z^k}{1+z^k}=1.
\]

Hay \(1013\) pares, que aportan \(1013\). Queda el término central sin emparejar:

\[
\frac{1}{1+z^{2027}}=\frac{1}{1+1}=\frac12.
\]

Por tanto,

\[
S=1013+\frac12=\frac{2027}{2}.
\]

\[
\boxed{\frac{2027}{2}}
\]