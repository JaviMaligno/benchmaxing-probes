

La clave está en reescribir el denominador usando la recurrencia. Tenemos

\[
b_{n+1}+3=b_n^3+7b_n^2+18b_n+18=(b_n+3)(b_n^2+4b_n+6).
\]

Entonces

\[
\frac{1}{b_n+3}-\frac{3}{b_{n+1}+3}
=
\frac{1}{b_n+3}-\frac{3}{(b_n+3)(b_n^2+4b_n+6)}
\]

\[
=
\frac{b_n^2+4b_n+6-3}{(b_n+3)(b_n^2+4b_n+6)}
=
\frac{b_n^2+4b_n+3}{(b_n+3)(b_n^2+4b_n+6)}
=
\frac{(b_n+1)(b_n+3)}{(b_n+3)(b_n^2+4b_n+6)}
=
\frac{b_n+1}{b_n^2+4b_n+6}.
\]

Por lo tanto,

\[
\frac{3^n(b_n+1)}{b_n^2+4b_n+6}
=
\frac{3^n}{b_n+3}-\frac{3^{n+1}}{b_{n+1}+3}.
\]

La suma es telescópica:

\[
\sum_{n=0}^{N}\frac{3^n(b_n+1)}{b_n^2+4b_n+6}
=
\frac{1}{b_0+3}-\frac{3^{N+1}}{b_{N+1}+3}.
\]

Como \(b_{n+1}>b_n^3\) y \(b_0=2025>1\), \(b_n\) crece muchísimo más rápido que \(3^n\), así que

\[
\lim_{N\to\infty}\frac{3^{N+1}}{b_{N+1}+3}=0.
\]

Entonces la suma infinita es

\[
\frac{1}{b_0+3}=\frac{1}{2025+3}=\frac{1}{2028}.
\]

\[
\boxed{\frac{1}{2028}}
\]