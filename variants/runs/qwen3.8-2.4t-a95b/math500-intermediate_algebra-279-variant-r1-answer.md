Sea $y = x^4$. Entonces el polinomio se convierte en

\[
y^2 + 63y - 64.
\]

Buscamos dos números cuyo producto sea $-64$ y cuya suma sea $63$: son $64$ y $-1$. Así que

\[
y^2 + 63y - 64 = (y + 64)(y - 1),
\]

y por tanto

\[
x^8 + 63x^4 - 64 = (x^4 + 64)(x^4 - 1).
\]

**Factorizamos $x^4 - 1$:**

\[
x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1).
\]

Estos tres factores son irreducibles sobre $\mathbb{Z}$ (los lineales trivialmente; $x^2+1$ no tiene raíces racionales).

**Factorizamos $x^4 + 64$** usando el truco de Sophie Germain:

\[
x^4 + 64 = (x^2 + 8)^2 - 16x^2 = (x^2 - 4x + 8)(x^2 + 4x + 8).
\]

Ambos cuadráticos tienen discriminante $16 - 32 = -16 < 0$, luego son irreducibles sobre $\mathbb{Z}$.

La factorización completa en irreducibles mónicos es:

\[
x^8 + 63x^4 - 64 = (x-1)(x+1)(x^2+1)(x^2-4x+8)(x^2+4x+8).
\]

Evaluamos cada factor en $x = 1$:

\[
\begin{aligned}
q_1(1) &= 1 - 1 = 0,\\
q_2(1) &= 1 + 1 = 2,\\
q_3(1) &= 1^2 + 1 = 2,\\
q_4(1) &= 1 - 4 + 8 = 5,\\
q_5(1) &= 1 + 4 + 8 = 13.
\end{aligned}
\]

Sumando:

\[
0 + 2 + 2 + 5 + 13 = 22.
\]

\[
\boxed{22}
\]