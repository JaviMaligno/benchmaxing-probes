Primero factorizo el polinomio:

\[
x^8 + 63x^4 - 64
\]

Hago la sustitución \(y = x^4\):

\[
y^2 + 63y - 64 = (y+64)(y-1)
\]

Entonces:

\[
x^8 + 63x^4 - 64 = (x^4+64)(x^4-1)
\]

Factorizo cada parte:

\[
x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)
\]

Para \(x^4 + 64\), uso la identidad de Sophie Germain:

\[
x^4 + 64 = x^4 + 4\cdot 16 = (x^2 + 4x + 8)(x^2 - 4x + 8)
\]

Estos dos cuadráticos son irreducibles sobre \(\mathbb{Q}\), ya que sus discriminantes son negativos (\(16 - 32 = -16\)).

Además, \(x^2+1\) es irreducible sobre los enteros.

Por tanto, la factorización completa en polinomios monicos irreducibles es:

\[
(x-1)(x+1)(x^2+1)(x^2+4x+8)(x^2-4x+8)
\]

Ahora evaluamos cada factor en \(x=1\):

- \(x-1 \to 0\)
- \(x+1 \to 2\)
- \(x^2+1 \to 2\)
- \(x^2+4x+8 \to 13\)
- \(x^2-4x+8 \to 5\)

Sumamos:

\[
0 + 2 + 2 + 13 + 5 = 22
\]

\[
\boxed{22}
\]