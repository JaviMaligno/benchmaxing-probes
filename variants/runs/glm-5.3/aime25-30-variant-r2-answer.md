Sea  
\[
P_k(x)=(x-8)(x-50)(x-72)(x-k),
\]
de modo que \(g(x)=P_k(x)/x\).

Supongamos que el mínimo se alcanza en exactamente dos números positivos distintos \(a,b\), con valor mínimo \(m\). Definimos
\[
Q(x)=P_k(x)-mx.
\]
Como \(Q(x)=x(g(x)-m)\), en \(x=a,b\) se tiene \(Q=0\). Además, \(P_k=xg\), así que
\[
Q'(x)=P_k'(x)-m=g(x)+xg'(x)-m.
\]
En un mínimo interior, \(g(a)=g(b)=m\) y \(g'(a)=g'(b)=0\), luego \(Q'(a)=Q'(b)=0\). Por lo tanto, \(a\) y \(b\) son raíces dobles de la cuártica \(Q\), y como tiene grado \(4\),
\[
Q(x)=(x-a)^2(x-b)^2.
\]

Sea \(s=a+b\), \(t=ab\). Entonces
\[
(x-a)^2(x-b)^2=(x^2-sx+t)^2
=x^4-2sx^3+(s^2+2t)x^2-2stx+t^2.
\]

Por otro lado,
\[
P_k(x)=x^4-(130+k)x^3+(4576+130k)x^2-(28800+4576k)x+28800k.
\]
Comparando coeficientes de \(x^3\), \(x^2\) y el constante:
\[
130+k=2s,\qquad 4576+130k=s^2+2t,\qquad 28800k=t^2.
\]
De la primera, \(s=\frac{k+130}{2}\). Sustituyendo en la segunda,
\[
t=\frac{-k^2+260k+1404}{8}.
\]
Como \(a,b>0\), tenemos \(t>0\), y de \(t^2=28800k\),
\[
t=120\sqrt{2k}.
\]
Sea \(y=\sqrt{2k}>0\). Entonces \(k=y^2/2\) y \(t=120y\), por lo que
\[
120y=\frac{-y^4/4+130y^2+1404}{8}.
\]
Multiplicando por \(32\) y reordenando:
\[
y^4-520y^2+3840y-5616=0.
\]
Esta ecuación se factoriza como
\[
(y-2)(y-6)(y-18)(y+26)=0.
\]
Como \(y>0\), tenemos \(y=2,6,18\). Así,
\[
k=\frac{y^2}{2}=2,18,162.
\]
Estos tres valores efectivamente producen dos raíces dobles positivas \(a,b\), y en cada caso
\[
g(x)-m=\frac{(x-a)^2(x-b)^2}{x}\ge 0,
\]
con igualdad exactamente en \(x=a,b\).

La suma pedida es
\[
2+18+162=182.
\]

\[
\boxed{182}
\]