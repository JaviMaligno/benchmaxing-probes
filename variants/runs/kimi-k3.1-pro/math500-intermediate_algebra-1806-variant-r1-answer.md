Sea \(w=e^{i\theta}\) y \(x=\cos\theta\). Como \(|w|=1\), tenemos \(w^{-1}=\overline w\), por lo que
\[
|1+w|=\sqrt{2+2x},
\]
y
\[
|2-2w+2w^2|
=2|w^{-1}-1+w|
=2|2\cos\theta-1|
=2|2x-1|.
\]
Así, debemos maximizar
\[
F(x)=\sqrt{2+2x}+2|2x-1|,\qquad -1\le x\le1.
\]

Si \(x\ge \tfrac12\), entonces \(F(x)=\sqrt{2+2x}+4x-2\), que es creciente y alcanza como máximo \(F(1)=4\).

Si \(-1\le x\le\tfrac12\), entonces
\[
F(x)=\sqrt{2+2x}+2-4x,
\qquad
F'(x)=\frac1{\sqrt{2+2x}}-4.
\]
El máximo se produce cuando \(F'(x)=0\), es decir,
\[
\sqrt{2+2x}=\frac14
\quad\Longrightarrow\quad
x=-\frac{31}{32}.
\]
En ese punto,
\[
F\!\left(-\frac{31}{32}\right)
=\frac14+2+\frac{31}{8}
=\frac{49}{8}.
\]
Este valor es alcanzable, por ejemplo, con \(w=\dfrac{-31+3i\sqrt7}{32}\).

\[
\boxed{\frac{49}{8}}
\]