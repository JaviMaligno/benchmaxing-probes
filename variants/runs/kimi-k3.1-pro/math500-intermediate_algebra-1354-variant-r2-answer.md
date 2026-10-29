Agrupamos los términos correspondientes a \(k\) y \(2027-k\), para \(1\le k\le 1013\). Como \(z^{2027}=1\),
\[
\frac1{1+z^{2027-k}}
=\frac1{1+z^{-k}}
=\frac{z^k}{1+z^k}.
\]
Por tanto, cada par suma
\[
\frac1{1+z^k}+\frac{z^k}{1+z^k}=1.
\]
Hay \(1013\) pares, que abarcan los términos desde \(k=1\) hasta \(k=2026\). El último término es
\[
\frac1{1+z^{2027}}=\frac12.
\]
Así, la suma total es \(1013+\frac12\).

\[
\boxed{\frac{2027}{2}}
\]