Sea \(f(x)=\dfrac{P(x)}{Q(x)}\), con \(P,Q\) polinomios cuadráticos.

Para \(n=1,2,3,4,5\) se cumple
\[
P(n)=n^3Q(n).
\]
Entonces el polinomio
\[
H(x)=P(x)-x^3Q(x)
\]
tiene raíces \(1,2,3,4,5\). Como \(H\) tiene grado a lo sumo \(5\),
\[
H(x)=k(x-1)(x-2)(x-3)(x-4)(x-5).
\]

Desarrollando:
\[
(x-1)(x-2)(x-3)(x-4)(x-5)=x^5-15x^4+85x^3-225x^2+274x-120.
\]

Si \(Q(x)=ax^2+bx+c\), entonces
\[
H(x)=P(x)-x^3Q(x)=-ax^5-bx^4-cx^3+(\text{términos de grado}\le 2).
\]
Comparando coeficientes:
\[
-a=k,\qquad -b=-15k,\qquad -c=85k.
\]
Por tanto
\[
Q(0)=c=-85k.
\]

Además, el término constante de \(H\) es
\[
H(0)=P(0)-0=-120k,
\]
luego \(P(0)=-120k\).

Así,
\[
f(0)=\frac{P(0)}{Q(0)}=\frac{-120k}{-85k}=\frac{24}{17}.
\]

\[
\boxed{\frac{24}{17}}
\]