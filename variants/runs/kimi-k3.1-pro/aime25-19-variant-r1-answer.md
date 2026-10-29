Usando \(\log_a(7^b)=\frac{b\ln 7}{\ln a}\), cada factor se simplifica:
\[
\frac{\log_k(7^{k^2-1})}{\log_{k+1}(7^{k^2-4})}
=\frac{k^2-1}{k^2-4}\cdot\frac{\ln(k+1)}{\ln k}
=\frac{(k-1)(k+1)}{(k-2)(k+2)}\log_k(k+1).
\]
Los logaritmos forman un producto telescópico:
\[
\prod_{k=3}^{80}\log_k(k+1)
=\frac{\ln81}{\ln3}=4.
\]
La parte racional también se telescopiza:
\[
\prod_{k=3}^{80}\frac{k-1}{k-2}=\frac{79}{2},
\qquad
\prod_{k=3}^{80}\frac{k+1}{k+2}=\frac{4}{82}=\frac{2}{41}.
\]
Por tanto, el producto vale
\[
4\cdot\frac{79}{2}\cdot\frac{2}{41}
=\frac{316}{41}.
\]
Como \(\gcd(316,41)=1\), se tiene \(m+n=316+41\).

\[
\boxed{357}
\]