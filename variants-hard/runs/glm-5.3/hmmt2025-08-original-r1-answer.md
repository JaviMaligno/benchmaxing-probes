Sea \(\alpha=\frac{1}{\pi}\) y \(\{x\}\) la parte fraccionaria. Como
\[
\frac{2^n}{2\pi}=2^{n-1}\alpha,
\]
definimos \(\theta_n=\{2^{n-1}\alpha\}\). Entonces
\[
\sin(2^n)=\sin(2\pi\theta_n),
\]
de modo que el signo es \(+1\) si \(0<\theta_n<\tfrac12\), y \(-1\) si \(\tfrac12<\theta_n<1\).

Escribamos \(\alpha\) en binario:
\[
\alpha=\sum_{k=1}^{\infty}\frac{b_k}{2^k},\qquad b_k\in\{0,1\}.
\]
Como \(\alpha\) es irracional, \(\theta_n\) nunca es \(0\) ni \(\tfrac12\), y
\[
\theta_n=\{2^{n-1}\alpha\}=0.b_n b_{n+1}\cdots{}_2.
\]
Por lo tanto,
\[
\operatorname{sgn}(\sin(2^n))=1-2b_n.
\]
Así,
\[
\sum_{n=1}^{\infty}\frac{\operatorname{sgn}(\sin(2^n))}{2^n}
=\sum_{n=1}^{\infty}\frac{1-2b_n}{2^n}
=1-2\sum_{n=1}^{\infty}\frac{b_n}{2^n}
=1-2\alpha.
\]
Como \(\alpha=\frac{1}{\pi}\), el valor es

\[
\boxed{1-\frac{2}{\pi}}
\]