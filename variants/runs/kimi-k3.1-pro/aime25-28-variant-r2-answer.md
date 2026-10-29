Escribamos \(y_k=\frac{a_k}{b_k}\) en fracción irreducible. Como
\[
y_{k+1}=\frac{a_k^2-a_kb_k+b_k^2}{3a_kb_k},
\]
se comprueba por inducción que \(a_k\equiv1\pmod3\), \(b_k\equiv-1\pmod3\), y que el único factor común entre el numerador y el denominador es \(3\). Por tanto,
\[
a_{k+1}=\frac{a_k^2-a_kb_k+b_k^2}{3},
\qquad b_{k+1}=a_kb_k.
\]

Definimos \(s_k=a_k+b_k\). Entonces
\[
s_{k+1}
=\frac{a_k^2-a_kb_k+b_k^2+3a_kb_k}{3}
=\frac{(a_k+b_k)^2}{3}
=\frac{s_k^2}{3}.
\]
Como \(s_1=19+14=33=3\cdot11\), obtenemos
\[
s_k=3\cdot11^{2^{k-1}}.
\]
Así,
\[
m+n=s_{2025}=3\cdot11^{2^{2024}}.
\]

Para calcularlo módulo \(1000\), observamos que \(11^{50}\equiv1\pmod{1000}\). Además, \(2^{2024}\equiv16\pmod{50}\), ya que \(2024=4+20\cdot101\) y \(2^{n+20}\equiv2^n\pmod{50}\) para \(n\ge1\). Por consiguiente,
\[
11^{2^{2024}}\equiv11^{16}\equiv161\pmod{1000},
\]
y finalmente
\[
m+n\equiv3\cdot161\equiv\boxed{483}.
\]