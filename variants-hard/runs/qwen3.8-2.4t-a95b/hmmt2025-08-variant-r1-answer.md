

Sea  
\[
\alpha=\frac{3}{2\pi}.
\]
Entonces
\[
3\cdot 2^n = 2\pi\,(2^n\alpha),
\]
por lo que el signo de \(\sin(3\cdot 2^n)\) depende solo de la parte fraccionaria de \(2^n\alpha\):

\[
\sin(2\pi x)>0 \iff \{x\}\in(0,1/2),
\]
\[
\sin(2\pi x)<0 \iff \{x\}\in(1/2,1).
\]

Como \(\pi\) es irracional, \(\alpha\) también lo es, así que nunca tenemos \(\{2^n\alpha\}=0\) ni \(1/2\).

Escribamos la expansión binaria de \(\alpha\):
\[
\alpha=0.b_1b_2b_3\ldots \quad (b_k\in\{0,1\}).
\]
Al multiplicar por \(2^n\), la parte fraccionaria es
\[
\{2^n\alpha\}=0.b_{n+1}b_{n+2}b_{n+3}\ldots
\]
Por tanto,
\[
\{2^n\alpha\}<\frac12 \iff b_{n+1}=0,
\]
y
\[
\{2^n\alpha\}>\frac12 \iff b_{n+1}=1.
\]
Así,
\[
\operatorname{sgn}\left(\sin(3\cdot 2^n)\right)=1-2b_{n+1}.
\]

Entonces la suma es
\[
\sum_{n=1}^{\infty}\frac{1-2b_{n+1}}{2^n}
=
\sum_{n=1}^{\infty}\frac1{2^n}
-
2\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n}.
\]
La primera suma es \(1\). Para la segunda,
\[
\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n}
=
2\sum_{m=2}^{\infty}\frac{b_m}{2^m}.
\]
Como \(\pi>3\), tenemos
\[
\alpha=\frac{3}{2\pi}<\frac12,
\]
por lo que \(b_1=0\). Luego
\[
\sum_{m=2}^{\infty}\frac{b_m}{2^m}=\alpha.
\]
Por tanto,
\[
\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n}=2\alpha.
\]
Finalmente,
\[
\sum_{n=1}^{\infty} \frac{\operatorname{sgn}\left(\sin\left(3\cdot 2^{n}\right)\right)}{2^{n}}
=
1-2(2\alpha)
=
1-4\alpha
=
1-\frac{6}{\pi}.
\]

\[
\boxed{1-\frac{6}{\pi}}
\]