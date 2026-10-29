

Sea  
\[
A(t)=(t-1)(t-2)(t-3)(t-4)=t^4-10t^3+35t^2-50t+24.
\]
Entonces
\[
\frac{A'(t)}{A(t)}=\sum_{k=1}^4 \frac1{t-k}.
\]

Para \(x\) tal que \(A(x^2)\neq 0\), usamos
\[
\frac{k}{x^2-k}=\frac{x^2}{x^2-k}-1.
\]
Así,
\[
\sum_{k=1}^4 \frac{k}{x^2-k}
= x^2\sum_{k=1}^4\frac1{x^2-k}-4
= x^2\frac{A'(x^2)}{A(x^2)}-4.
\]

La ecuación dada se convierte en
\[
x^2\frac{A'(x^2)}{A(x^2)}-4=2010x-4,
\]
es decir,
\[
x^2A'(x^2)=2010x\,A(x^2).
\]

Al multiplicar, obtenemos el polinomio
\[
F(x)=2010x\,A(x^2)-x^2A'(x^2)=0.
\]
Los puntos donde \(A(x^2)=0\) no son raíces de \(F\), porque \(A\) tiene raíces simples; por tanto no aparecen soluciones extrañas.

Ahora,
\[
A(x^2)=x^8-10x^6+35x^4-50x^2+24,
\]
y
\[
A'(x^2)=4x^6-30x^4+70x^2-50.
\]
Luego
\[
F(x)=2010x(x^8-10x^6+\cdots)-x^2(4x^6-30x^4+\cdots).
\]
Los términos de mayor grado son
\[
F(x)=2010x^9-4x^8+\text{términos de grado }\le 7.
\]

Así, \(F\) tiene grado \(9\), coeficiente principal \(2010\) y coeficiente de \(x^8\) igual a \(-4\). Por las fórmulas de Vieta, la suma de todas las raíces complejas es
\[
-\frac{-4}{2010}=\frac{4}{2010}=\frac{2}{1005}.
\]

\[
\boxed{\frac{2}{1005}}
\]