Vamos a simplificar el producto término a término.

Para un término general con base \(k\), tenemos:

\[
\log_k(7^{k^2-1}) = (k^2-1)\log_k 7
\]

y para el denominador:

\[
\log_{k+1}(7^{k^2-4}) = (k^2-4)\log_{k+1}7.
\]

Además, por cambio de base:

\[
\log_k 7 = \frac{1}{\log_7 k}, \qquad \log_{k+1} 7 = \frac{1}{\log_7(k+1)}.
\]

Entonces cada factor del producto es:

\[
\frac{\log_k(7^{k^2-1})}{\log_{k+1}(7^{k^2-4})}
= \frac{(k^2-1)\cdot\dfrac{1}{\log_7 k}}{(k^2-4)\cdot\dfrac{1}{\log_7(k+1)}}
= \frac{k^2-1}{k^2-4}\cdot \frac{\log_7(k+1)}{\log_7 k}.
\]

Ahora, por las propiedades de los logaritmos:

\[
\frac{\log_7(k+1)}{\log_7 k} = \log_k(k+1).
\]

Por tanto, el producto completo es:

\[
\prod_{k=3}^{80} \frac{k^2-1}{k^2-4} \cdot \prod_{k=3}^{80} \log_k(k+1).
\]

El segundo producto es telescópico:

\[
\prod_{k=3}^{80} \log_k(k+1)
= \log_3 4 \cdot \log_4 5 \cdots \log_{80} 81
= \log_3 81
= 4,
\]

porque \(81=3^4\).

Ahora simplificamos el primer producto. Observamos que:

\[
k^2-1=(k-1)(k+1), \qquad k^2-4=(k-2)(k+2).
\]

Entonces:

\[
\prod_{k=3}^{80} \frac{(k-1)(k+1)}{(k-2)(k+2)}.
\]

Este producto se telescopa agrupando factores según \(k-2\). Reescribiendo:

\[
\frac{k^2-1}{k^2-4}
= \frac{k-1}{k-2}\cdot \frac{k+1}{k+2}.
\]

Así:

\[
\prod_{k=3}^{80}\frac{k-1}{k-2}\cdot \prod_{k=3}^{80}\frac{k+1}{k+2}.
\]

El primer producto es:

\[
\prod_{k=3}^{80}\frac{k-1}{k-2}
= \frac{2}{1}\cdot \frac{3}{2}\cdot \frac{4}{3}\cdots \frac{79}{78}
= 79.
\]

El segundo producto es:

\[
\prod_{k=3}^{80}\frac{k+1}{k+2}
= \frac{4}{5}\cdot \frac{5}{6}\cdots \frac{81}{82}
= \frac{4}{82}
= \frac{2}{41}.
\]

Por lo tanto:

\[
\prod_{k=3}^{80} \frac{k^2-1}{k^2-4}
= 79\cdot \frac{2}{41}
= \frac{158}{41}.
\]

Multiplicando por el valor \(4\) del producto de logaritmos:

\[
\frac{158}{41}\cdot 4
= \frac{632}{41}.
\]

La fracción \(\frac{632}{41}\) ya está en su forma irreducible, porque \(41\) es primo y no divide a \(632\).

Finalmente:

\[
m+n = 632+41 = 673.
\]

\[
\boxed{673}
\]