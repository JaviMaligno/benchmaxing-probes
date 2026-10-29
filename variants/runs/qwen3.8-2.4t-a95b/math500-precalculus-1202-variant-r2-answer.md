

Sea  
\[
A=\arccos x,\qquad B=\arccos 2x,\qquad C=\arccos 4x.
\]
Entonces \(A+B+C=\pi\), luego
\[
A+B=\pi-C.
\]

Tomando cosenos:
\[
\cos(A+B)=\cos(\pi-C)=-\cos C=-4x.
\]

Pero
\[
\cos(A+B)=\cos A\cos B-\sin A\sin B.
\]
Como \(\cos A=x\), \(\cos B=2x\), \(\cos C=4x\), y los senos son no negativos,
\[
\cos(A+B)=2x^2-\sqrt{(1-x^2)(1-4x^2)}.
\]
Así,
\[
2x^2-\sqrt{(1-x^2)(1-4x^2)}=-4x,
\]
por lo que
\[
\sqrt{(1-x^2)(1-4x^2)}=2x^2+4x.
\]

Elevando al cuadrado:
\[
(1-x^2)(1-4x^2)=(2x^2+4x)^2.
\]
Expandiendo:
\[
1-5x^2+4x^4=4x^4+16x^3+16x^2.
\]
Cancelando \(4x^4\):
\[
1=16x^3+21x^2,
\]
es decir,
\[
16x^3+21x^2-1=0.
\]

Este polinomio es primitivo y no tiene raíces racionales; por tanto, es el polinomio mínimo de \(x\) sobre \(\mathbb{Q}\). Cualquier polinomio cúbico entero que tenga a \(x\) como raíz debe ser un múltiplo entero de
\[
16x^3+21x^2-1.
\]

Para este polinomio,
\[
|a|+|b|+|c|+|d|=16+21+0+1=38.
\]

\[
\boxed{38}
\]