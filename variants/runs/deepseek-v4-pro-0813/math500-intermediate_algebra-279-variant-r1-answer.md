Voy a factorizar el polinomio.

Sea \( y = x^4 \). Entonces

\[
x^8 + 63x^4 - 64 = y^2 + 63y - 64.
\]

Resuelvo la cuadrática en \(y\):

\[
y^2 + 63y - 64 = (y - 1)(y + 64).
\]

Luego

\[
x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64).
\]

Factorizo cada factor:

\[
x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1),
\]

\[
x^4 + 64 = (x^2 + 8)^2 - 16x^2 = (x^2 + 4x + 8)(x^2 - 4x + 8).
\]

Cada uno de estos factores es irreducible sobre \(\mathbb{Z}\):

- \(x - 1\),
- \(x + 1\),
- \(x^2 + 1\),
- \(x^2 + 4x + 8\),
- \(x^2 - 4x + 8\).

Evaluamos cada factor en \(x = 1\):

\[
x - 1 \mapsto 0,
\]
\[
x + 1 \mapsto 2,
\]
\[
x^2 + 1 \mapsto 2,
\]
\[
x^2 + 4x + 8 \mapsto 13,
\]
\[
x^2 - 4x + 8 \mapsto 5.
\]

La suma es

\[
0 + 2 + 2 + 13 + 5 = 22.
\]

\[
\boxed{22}
\]