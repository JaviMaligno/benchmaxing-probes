

Sea \(f(x)=-\dfrac{1}{1+x}\), de modo que \(b_{k+1}=f(b_k)\).

Entonces
\[
b_3=f(f(b_1)).
\]
Calculamos \(f(f(x))\):
\[
f(f(x))=f\left(-\frac{1}{1+x}\right)
=-\frac{1}{1-\frac{1}{1+x}}
=-\frac{1}{\frac{x}{1+x}}
=-\frac{1+x}{x}.
\]

Como \(b_3=b_1\), si \(x=b_1\), tenemos
\[
x=-\frac{1+x}{x}.
\]
Multiplicando por \(x\):
\[
x^2=-1-x,
\]
así que
\[
x^2+x+1=0.
\]

Esta ecuación implica que \(x\) es una raíz cúbica de la unidad distinta de \(1\), por lo tanto
\[
x^3=1.
\]

Además, como \(x^2+x+1=0\), se tiene \(1+x=-x^2\), y entonces
\[
b_2=-\frac{1}{1+x}=-\frac{1}{-x^2}=\frac{1}{x^2}=x=b_1.
\]
Por tanto, la sucesión es constante y \(b_9=b_1\).

Finalmente,
\[
(b_9)^9=(b_1)^9=(b_1^3)^3=1.
\]

\[
\boxed{1}
\]