Como \(1997\) es primo y \(\omega^{1997}=1\) con \(\omega\neq 1\), el orden de \(\omega\) es exactamente \(1997\). Por lo tanto,

\[
\omega,\omega^2,\dots,\omega^{1997}
\]

son todas las raíces de \(x^{1997}-1\).

Sea

\[
x^{1997}-1=\prod_{k=1}^{1997}(x-\omega^k).
\]

Tomando derivada logarítmica,

\[
\frac{1997x^{1996}}{x^{1997}-1}
=
\sum_{k=1}^{1997}\frac{1}{x-\omega^k}.
\]

Evaluamos en \(x=-1\):

\[
\frac{1997(-1)^{1996}}{(-1)^{1997}-1}
=
\sum_{k=1}^{1997}\frac{1}{-1-\omega^k}.
\]

Esto da

\[
\frac{1997}{-2}
=
-\sum_{k=1}^{1997}\frac{1}{1+\omega^k}.
\]

Por lo tanto,

\[
\sum_{k=1}^{1997}\frac{1}{1+\omega^k}
=
\frac{1997}{2}.
\]

\[
\boxed{\frac{1997}{2}}
\]