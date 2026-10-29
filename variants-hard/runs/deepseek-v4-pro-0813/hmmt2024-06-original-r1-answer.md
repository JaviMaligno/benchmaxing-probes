Vamos a razonar paso a paso.

Queremos los enteros positivos \(n\) con \(50 \le n \le 100\) tales que \(2n+3\) **no** divide a \(2^{n!}-1\).

Sea \(m=2n+3\). Notemos que \(n!\) es par para todo \(n\ge 2\), así que en nuestro rango \(n!\) es par. Queremos caracterizar cuándo \(m\mid 2^{n!}-1\).

Como \(\gcd(2,m)=\gcd(2,2n+3)=1\), el orden de \(2\) módulo \(m\) está bien definido. Sea

\[
d=\operatorname{ord}_m(2).
\]

Entonces \(m\mid 2^{n!}-1\) si y solo si \(d\mid n!\).

Ahora, si \(m\) es primo, por el pequeño teorema de Fermat tenemos \(d\mid m-1=2n+2\). Como \(d\mid n!\), se cumple \(d\mid \gcd(n!,2n+2)\).

Además, para \(n\ge 50\), todos los primos \(p\le n\) y todas las potencias relevantes dividen a \(n!\). En particular, como \(2n+2=2(n+1)\), se tiene

\[
2n+2 \mid n!
\]

para \(n\ge 50\). En efecto, \(n+1\le n!\) y \(\gcd(2,n+1)\) no complica nada: para \(n\ge 4\) ya es fácil ver que \(2(n+1)\mid n!\). Por ejemplo, \(2\) y \(n+1\) son factores primos con exponentes suficientemente grandes en \(n!\).

Por tanto, si \(m=2n+3\) es primo, entonces \(d\mid 2n+2\), y como \(2n+2\mid n!\), concluimos \(d\mid n!\). Luego

\[
m\mid 2^{n!}-1.
\]

Es decir, **si \(2n+3\) es primo, entonces divide a \(2^{n!}-1\)**.

Por consiguiente, los únicos posibles \(n\) para los que \(2n+3\) no divide a \(2^{n!}-1\) serán aquellos con \(2n+3\) compuesto.

Así que debemos encontrar los \(n\in[50,100]\) tales que \(2n+3\) sea compuesto.

En ese rango, \(2n+3\) recorre los impares desde

\[
2\cdot 50+3=103
\]

hasta

\[
2\cdot 100+3=203.
\]

Los impares entre \(103\) y \(203\) son exactamente \(2n+3\) con \(n=50,\dots,100\). Debemos contar cuáles son compuestos.

Listamos los primos impares en ese intervalo:

\[
103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199.
\]

Estos son \(20\) primos. Como hay

\[
100-50+1=51
\]

valores de \(n\), los compuestos son

\[
51-20=31
\]

valores de \(n\).

Ahora sumamos todos los \(n\in[50,100]\). Los valores de \(n\) correspondientes a los \(20\) primos anteriores son:

\[
\begin{aligned}
2n+3=103 &\implies n=50,\\
107 &\implies n=52,\\
109 &\implies n=53,\\
113 &\implies n=55,\\
127 &\implies n=62,\\
131 &\implies n=64,\\
137 &\implies n=67,\\
139 &\implies n=68,\\
149 &\implies n=73,\\
151 &\implies n=74,\\
157 &\implies n=77,\\
163 &\implies n=80,\\
167 &\implies n=82,\\
173 &\implies n=85,\\
179 &\implies n=88,\\
181 &\implies n=89,\\
191 &\implies n=94,\\
193 &\implies n=95,\\
197 &\implies n=97,\\
199 &\implies n=98.
\end{aligned}
\]

La suma total de \(n\) desde \(50\) hasta \(100\) es

\[
S=\frac{(50+100)\cdot 51}{2}=150\cdot 25.5=3825.
\]

La suma de los \(20\) valores de \(n\) con \(2n+3\) primo es:

\[
50+52+53+55+62+64+67+68+73+74+77+80+82+85+88+89+94+95+97+98.
\]

Sumemos por partes:

\[
50+52=102,
\]
\[
102+53=155,
\]
\[
155+55=210,
\]
\[
210+62=272,
\]
\[
272+64=336,
\]
\[
336+67=403,
\]
\[
403+68=471,
\]
\[
471+73=544,
\]
\[
544+74=618,
\]
\[
618+77=695,
\]
\[
695+80=775,
\]
\[
775+82=857,
\]
\[
857+85=942,
\]
\[
942+88=1030,
\]
\[
1030+89=1119,
\]
\[
1119+94=1213,
\]
\[
1213+95=1308,
\]
\[
1308+97=1405,
\]
\[
1405+98=1503.
\]

Entonces la suma pedida es

\[
3825-1503=2322.
\]

Por tanto, la respuesta es

\[
\boxed{2322}
\]