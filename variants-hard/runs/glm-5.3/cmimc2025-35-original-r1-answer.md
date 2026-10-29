Para \(x\) fijo, sea \(Y=f(x)\), uniforme en \(\{1,\dots,25\}\).

- Si \(Y=x\), entonces \(f(f(x))=f(x)=x\), so \((f(f(x))-x)^2=0\).
- Si \(Y\ne x\), que ocurre con probabilidad \(24/25\), entonces \(f(Y)\) es uniforme en \(\{1,\dots,25\}\).

Sea \(U\) uniforme en \(\{1,\dots,25\}\). Entonces

\[
\mathbb E[(U-x)^2]=\mathbb E[U^2]-2x\mathbb E[U]+x^2.
\]

Aquí

\[
\mathbb E[U]=13,\qquad \mathbb E[U^2]=\frac{26\cdot 51}{6}=221.
\]

Así,

\[
\mathbb E[(f(f(x))-x)^2]=\frac{24}{25}(221-26x+x^2).
\]

Sumando sobre \(x=1,\dots,25\),

\[
\mathbb E\left[\sum_{x=1}^{25}(f(f(x))-x)^2\right]
=\frac{24}{25}\sum_{x=1}^{25}(221-26x+x^2).
\]

Ahora,

\[
\sum_{x=1}^{25}221=5525,
\]

\[
\sum_{x=1}^{25}x=325,
\]

\[
\sum_{x=1}^{25}x^2=\frac{25\cdot 26\cdot 51}{6}=5525.
\]

Por lo tanto,

\[
\sum_{x=1}^{25}(221-26x+x^2)
=5525-26(325)+5525
=2600.
\]

Entonces,

\[
\frac{24}{25}\cdot 2600=2496.
\]

\[
\boxed{2496}
\]