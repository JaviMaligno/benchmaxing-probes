

Sea

\[
a_n=\operatorname{sgn}(\sin(2^n)).
\]

Como \(\pi\) es irracional, \(2^n\) nunca es múltiplo de \(\pi\), así que \(a_n\neq 0\).

Para \(x>0\) no múltiplo de \(\pi\), si \(k=\lfloor x/\pi\rfloor\), entonces \(x\in(k\pi,(k+1)\pi)\), y el signo de \(\sin x\) alterna:

\[
\operatorname{sgn}(\sin x)=(-1)^k.
\]

Por tanto,

\[
a_n=(-1)^{\lfloor 2^n/\pi\rfloor}.
\]

Ahora sea \(\beta=1/\pi\). Como \(0<\beta<1\) y es irracional, tiene expansión binaria

\[
\beta=\sum_{n=1}^{\infty}\frac{b_n}{2^n},\qquad b_n\in\{0,1\}.
\]

Entonces

\[
\left\lfloor 2^n\beta\right\rfloor
=
b_1 2^{n-1}+b_2 2^{n-2}+\cdots+b_n.
\]

La paridad de este entero es exactamente \(b_n\), porque todos los términos anteriores son pares. Así,

\[
a_n=(-1)^{b_n}=1-2b_n.
\]

Luego

\[
\sum_{n=1}^{\infty}\frac{\operatorname{sgn}(\sin(2^n))}{2^n}
=
\sum_{n=1}^{\infty}\frac{1-2b_n}{2^n}
=
\sum_{n=1}^{\infty}\frac1{2^n}
-
2\sum_{n=1}^{\infty}\frac{b_n}{2^n}.
\]

La primera suma es \(1\), y la segunda es \(\beta=1/\pi\). Por tanto,

\[
\boxed{1-\frac{2}{\pi}}
\]