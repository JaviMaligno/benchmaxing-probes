

Sea \(f(x)=-\dfrac{1}{1+x}\), de modo que \(b_{k+1}=f(b_k)\).

La condición \(b_3=b_1\) significa

\[
f(f(b_1))=b_1.
\]

Calculamos \(f(f(x))\):

\[
f(x)=-\frac{1}{1+x},
\]

\[
1+f(x)=1-\frac{1}{1+x}=\frac{x}{1+x},
\]

\[
f(f(x))=-\frac{1}{\frac{x}{1+x}}=-\frac{1+x}{x}.
\]

Entonces

\[
-\frac{1+b_1}{b_1}=b_1.
\]

Multiplicando por \(b_1\):

\[
-(1+b_1)=b_1^2,
\]

\[
b_1^2+b_1+1=0.
\]

Esta ecuación implica que \(b_1\) es una raíz cúbica de la unidad distinta de \(1\), por lo que

\[
b_1^3=1.
\]

Además, de \(b_1^2+b_1+1=0\) se tiene \(b_1(1+b_1)=-1\), así que

\[
b_2=-\frac{1}{1+b_1}=b_1.
\]

Por tanto, la sucesión es constante: \(b_n=b_1\) para todo \(n\). En particular,

\[
b_9=b_1.
\]

Luego

\[
(b_9)^9=(b_1)^9=(b_1^3)^3=1^3=1.
\]

\[
\boxed{1}
\]