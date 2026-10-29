Para \(k<n\), dos vectores de peso \(k\) que difieren en un intercambio de coordenadas permiten generar todo vector de peso \(2\). Así:

- Si \(k\) es impar, se genera todo \(\mathbb F_2^n\), por lo que \(d_{n,k}=1\).
- Si \(k\) es par, se genera exactamente el subgrupo de peso par, por lo que \(d_{n,k}=2\).
- Si \(k=n\), cada vértice solo está unido a su complemento, de modo que \(d_{n,n}=2^{n-1}\).

Por consiguiente,
\[
\sum_{k=1}^n d_{n,k}
=(n-1)+\left\lfloor\frac{n-1}{2}\right\rfloor+2^{n-1}.
\]
Sumando para \(n=1,\dots,12\):
\[
66+30+(2^{12}-1)=66+30+4095.
\]

\[
\boxed{4191}
\]