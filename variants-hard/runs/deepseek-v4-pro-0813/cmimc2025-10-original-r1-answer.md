Sea \(x_n=a_n+1\). Entonces

\[
x_{n+1}=a_{n+1}+1
=a_n^3+5a_n^2+10a_n+7
=x_n^3+2x_n^2+3x_n+1.
\]

Por tanto,

\[
x_{n+1}+1=x_n^3+2x_n^2+3x_n+2
=(x_n+1)(x_n^2+x_n+2).
\]

Ahora observamos que

\[
\frac{x_n}{x_n^2+x_n+2}
=
\frac{1}{x_n+1}-\frac{2}{x_{n+1}+1}.
\]

En efecto, usando \(x_{n+1}+1=(x_n+1)(x_n^2+x_n+2)\):

\[
\frac{1}{x_n+1}-\frac{2}{(x_n+1)(x_n^2+x_n+2)}
=
\frac{x_n^2+x_n+2-2}{(x_n+1)(x_n^2+x_n+2)}
=
\frac{x_n}{x_n^2+x_n+2}.
\]

Como \(a_n+1=x_n\), la suma pedida es

\[
\sum_{n=0}^{\infty}2^n\left(
\frac{1}{x_n+1}-\frac{2}{x_{n+1}+1}
\right).
\]

Esto telescopa:

\[
\sum_{n=0}^{N}2^n\left(
\frac{1}{x_n+1}-\frac{2}{x_{n+1}+1}
\right)
=
\frac{1}{x_0+1}-\frac{2^{N+1}}{x_{N+1}+1}.
\]

Dado que \(x_n\to\infty\), el último término tiende a \(0\). Además,

\[
x_0=a_0+1=2025.
\]

Por lo tanto,

\[
\sum_{n=0}^{\infty}\frac{2^n(a_n+1)}{a_n^2+3a_n+4}
=
\frac{1}{2026}.
\]

\[
\boxed{\frac{1}{2026}}
\]