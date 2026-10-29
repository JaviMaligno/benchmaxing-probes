Sea \(b_n=a_n+1\). Entonces \(b_0=2025\) y

\[
a_{n+1}=a_n^3+5a_n^2+10a_n+6
\]

se reescribe, usando \(a_n=b_n-1\), como

\[
b_{n+1}=b_n^3+2b_n^2+3b_n+1.
\]

Luego

\[
b_{n+1}+1=b_n^3+2b_n^2+3b_n+2=(b_n+1)(b_n^2+b_n+2).
\]

Además,

\[
a_n^2+3a_n+4=(b_n-1)^2+3(b_n-1)+4=b_n^2+b_n+2.
\]

Por tanto el término general de la suma es

\[
\frac{2^n(a_n+1)}{a_n^2+3a_n+2}
=
\frac{2^n b_n}{b_n^2+b_n+2}.
\]

Ahora observamos la identidad

\[
\frac{b_n}{b_n^2+b_n+2}
=
\frac{1}{b_n+1}-\frac{2}{b_{n+1}+1},
\]

porque

\[
\frac{1}{b_n+1}-\frac{2}{(b_n+1)(b_n^2+b_n+2)}
=
\frac{b_n^2+b_n}{(b_n+1)(b_n^2+b_n+2)}
=
\frac{b_n}{b_n^2+b_n+2}.
\]

Así, la suma parcial hasta \(N\) es telescópica:

\[
\sum_{n=0}^{N}\frac{2^n(a_n+1)}{a_n^2+3a_n+4}
=
\sum_{n=0}^{N}\left(\frac{2^n}{b_n+1}-\frac{2^{n+1}}{b_{n+1}+1}\right)
=
\frac{1}{b_0+1}-\frac{2^{N+1}}{b_{N+1}+1}.
\]

Como \(b_n\) crece súper exponencialmente, se tiene

\[
\lim_{N\to\infty}\frac{2^{N+1}}{b_{N+1}+1}=0.
\]

Finalmente,

\[
\sum_{n=0}^{\infty}\frac{2^n(a_n+1)}{a_n^2+3a_n+4}
=
\frac{1}{b_0+1}
=
\frac{1}{2025+1}
=
\frac{1}{2026}.
\]

\[
\boxed{\frac{1}{2026}}
\]