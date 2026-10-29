Sean \(\alpha=\arccos x\), \(\beta=\arccos 2x\), \(\gamma=\arccos 4x\). Como \(\alpha+\beta+\gamma=\pi\),

\[
\cos\gamma=\cos(\pi-(\alpha+\beta))=-\cos(\alpha+\beta)
=\sin\alpha\sin\beta-\cos\alpha\cos\beta.
\]

Entonces

\[
4x=\sqrt{1-x^2}\sqrt{1-4x^2}-2x^2.
\]

Como \(x,2x,4x\in[-1,1]\), se tiene \(x\in[-1/4,1/4]\), y además

\[
\sqrt{(1-x^2)(1-4x^2)}=4x+2x^2=2x(x+2)\ge 0
\]

implica \(x\ge 0\). Elevando al cuadrado,

\[
(4x+2x^2)^2=(1-x^2)(1-4x^2),
\]

\[
16x^4+16x^3+16x^2=1-5x^2+4x^4,
\]

\[
16x^3+21x^2-1=0.
\]

Así \(x\) es raíz de \(f(x)=16x^3+21x^2-1\).

Este polinomio es irreducible: módulo \(7\),

\[
f(x)\equiv 2x^3+6=2(x^3+3)\pmod 7.
\]

En \(\mathbb F_7\) los cubos son \(0,1,6\), de modo que \(x^3+3\) nunca es \(0\). Por tanto \(f\) no tiene factor lineal y, al ser cúbico, es irreducible.

El polinomio es primitivo, pues \(\gcd(16,21,0,-1)=1\). Luego cualquier otro polinomio cúbico entero con la misma raíz es múltiplo entero de \(f\), y la menor suma de valores absolutos de coeficientes se alcanza con \(f\):

\[
|16|+|21|+|0|+|-1|=38.
\]

\[
\boxed{38}
\]