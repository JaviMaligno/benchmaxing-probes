

Sea

\[
N=\underline{p}\,\underline{q}\,\underline{r}\,\underline{s}=1000p+100q+10r+s
\]

un número de cuatro dígitos múltiplo de \(m\), y sea

\[
N'=\underline{q}\,\underline{r}\,\underline{s}\,\underline{p}=1000q+100r+10s+p.
\]

Observamos que

\[
10N=10000p+1000q+100r+10s,
\]

por lo que

\[
N'=10N-9999p.
\]

Si \(m\mid N\) y además la propiedad exige \(m\mid N'\), entonces

\[
m\mid (10N-N')=9999p.
\]

Ahora, para cualquier \(m\) de dos dígitos, existe un múltiplo de \(m\) de cuatro dígitos cuyo primer dígito es \(1\). En efecto, tomando

\[
N=m\left\lceil \frac{1000}{m}\right\rceil,
\]

se tiene

\[
1000\le N<1000+m\le 1099,
\]

así que \(N\) empieza con dígito \(1\). Para ese múltiplo, \(p=1\), y la condición implica

\[
m\mid 9999.
\]

Recíprocamente, si \(m\mid 9999\), entonces para cualquier múltiplo \(N\) de \(m\),

\[
N'=10N-9999p
\]

también es múltiplo de \(m\), pues \(m\mid 10N\) y \(m\mid 9999p\). Así que los \(m\) buscados son exactamente los divisores de dos dígitos de \(9999\).

Factorizamos:

\[
9999=9\cdot 1111=3^2\cdot 11\cdot 101.
\]

Sus divisores de dos dígitos son

\[
11,\;33,\;99.
\]

La suma pedida es

\[
11+33+99=143.
\]

\[
\boxed{143}
\]