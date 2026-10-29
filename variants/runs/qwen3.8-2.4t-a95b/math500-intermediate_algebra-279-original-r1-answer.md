

Sea \(y=x^4\). Entonces

\[
x^8+3x^4-4 = y^2+3y-4=(y-1)(y+4).
\]

Volviendo a \(x\):

\[
x^8+3x^4-4=(x^4-1)(x^4+4).
\]

Factorizamos cada parte sobre los enteros:

\[
x^4-1=(x^2-1)(x^2+1)=(x-1)(x+1)(x^2+1).
\]

Para \(x^4+4\), usamos la identidad de Sophie Germain:

\[
x^4+4=(x^2+2)^2-(2x)^2=(x^2-2x+2)(x^2+2x+2).
\]

Ambos cuadráticos son irreducibles sobre \(\mathbb{Z}\), pues sus discriminantes son

\[
(-2)^2-4(2)=-4,\qquad 2^2-4(2)=-4.
\]

Así, la factorización en factores mónicos irreducibles es

\[
(x-1)(x+1)(x^2+1)(x^2-2x+2)(x^2+2x+2).
\]

Evaluamos en \(x=1\):

\[
p_1(1)=0,\quad
p_2(1)=2,\quad
p_3(1)=2,\quad
p_4(1)=1,\quad
p_5(1)=5.
\]

La suma es

\[
0+2+2+1+5=10.
\]

\[
\boxed{10}
\]