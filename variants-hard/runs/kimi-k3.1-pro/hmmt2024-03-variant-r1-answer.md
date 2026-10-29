Sea \(N=1000p+100q+10r+s\) y sea \(R=1000q+100r+10s+p\) el número obtenido al rotar sus cifras. Entonces
\[
R=10N-9999p.
\]

Si \(m\mid N\) y también \(m\mid R\), necesariamente \(m\mid 9999p\). Para todo \(m\) de dos cifras existe algún múltiplo de \(m\) entre \(1000\) y \(1999\), pues ese intervalo tiene longitud \(1000>m\). Tomando dicho múltiplo, cuyo primer dígito es \(p=1\), obtenemos que \(m\mid9999\).

Recíprocamente, si \(m\mid9999\), la igualdad \(R=10N-9999p\) muestra que \(m\mid N\) implica \(m\mid R\). Por tanto, los valores buscados son exactamente los divisores de dos cifras de
\[
9999=3^2\cdot11\cdot101,
\]
es decir, \(11,33,99\). Su suma es
\[
\boxed{143}
\]