

Sea \(n=2027\), que es impar. Como \(z^{2027}=1\), tenemos \(z^{2027-k}=z^{-k}\).

Primero, ningún denominador se anula: si \(z^k=-1\), entonces
\[
1=(z^{2027})^k=(z^k)^{2027}=(-1)^{2027}=-1,
\]
una contradicción.

Ahora emparejamos el término \(k\) con el término \(2027-k\), para \(k=1,2,\dots,1013\):
\[
\frac{1}{1+z^k}+\frac{1}{1+z^{2027-k}}
=
\frac{1}{1+z^k}+\frac{1}{1+z^{-k}}.
\]
Pero
\[
\frac{1}{1+z^{-k}}
=
\frac{1}{1+\frac1{z^k}}
=
\frac{z^k}{1+z^k},
\]
así que
\[
\frac{1}{1+z^k}+\frac{1}{1+z^{-k}}
=
\frac{1+z^k}{1+z^k}=1.
\]

Hay \(1013\) pares, cada uno suma \(1\). Además queda el término \(k=2027\):
\[
\frac{1}{1+z^{2027}}=\frac{1}{1+1}=\frac12.
\]

Por tanto, la suma total es
\[
1013+\frac12=\frac{2027}{2}.
\]

\[
\boxed{\frac{2027}{2}}
\]