Sea \(p=2027\). Los cuadrados perfectos entre \(1\) y \(2027\) son \(k^2\) para \(1\le k\le 45\).

Por interpolación de Lagrange,
\[
f(x)=\sum_{s\text{ cuadrado}}\prod_{\substack{1\le j\le p\\j\ne s}}\frac{x-j}{s-j}.
\]
Como \(\sum_{j=1}^p j=T=p(p+1)/2\), el coeficiente de \(x^{p-2}=x^{2025}\) es
\[
\sum_{s\text{ cuadrado}}\frac{-(T-s)}{(s-1)!\,(-1)^{p-s}(p-s)!}
=\sum_{s\text{ cuadrado}}\frac{(-1)^s(T-s)}{(s-1)!(p-s)!}.
\]
Módulo \(p\), tenemos \(T\equiv0\). Además, usando el teorema de Wilson,
\[
\frac1{(s-1)!(p-s)!}
=\frac{\binom{p-1}{s-1}}{(p-1)!}
\equiv\frac{(-1)^{s-1}}{-1}
=(-1)^s\pmod p.
\]
Por tanto, cada término es congruente con \(-s\), y el coeficiente buscado satisface
\[
\frac ab\equiv-\sum_{k=1}^{45}k^2
=-\frac{45\cdot46\cdot91}{6}
=-31395\pmod{2027}.
\]
Como \(31395=15\cdot2027+990\), obtenemos
\[
\frac ab\equiv-990\equiv1037\pmod{2027}.
\]

\[
\boxed{1037}
\]