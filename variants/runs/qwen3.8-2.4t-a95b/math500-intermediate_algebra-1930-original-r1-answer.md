

Como el polinomio es recíproco y $x=0$ no es raíz, dividimos entre $x^2$:

\[
x^2+ax-b+\frac{a}{x}+\frac{1}{x^2}=0.
\]

Sea

\[
y=x+\frac1x.
\]

Entonces

\[
x^2+\frac1{x^2}=y^2-2,
\]

por lo que la ecuación se convierte en

\[
y^2+ay-(b+2)=0.
\]

Para que exista una raíz real $x$, se necesita que alguna raíz real $y$ cumpla $|y|\ge 2$, pues $x+\frac1x\in(-\infty,-2]\cup[2,\infty)$ para $x\in\mathbb R\setminus\{0\}$.

La ecuación cuadrática en $y$ tiene raíces de signos opuestos porque su producto es $-(b+2)<0$.

La raíz positiva cumple $y_+\ge 2$ si y solo si

\[
4+2a-(b+2)\le 0 \iff b\ge 2+2a,
\]

lo cual es imposible en $[0,1]^2$.

La raíz negativa cumple $y_-\le -2$ si y solo si

\[
4-2a-(b+2)\le 0 \iff b\ge 2-2a.
\]

Así,

\[
S=\{(a,b)\in[0,1]^2: b\ge 2-2a\}.
\]

Esta región existe solo cuando $2-2a\le 1$, es decir $a\ge \frac12$. Por tanto, el área es

\[
\int_{1/2}^1 \bigl(1-(2-2a)\bigr)\,da
=
\int_{1/2}^1 (2a-1)\,da
=
\left[a^2-a\right]_{1/2}^1
=
\frac14.
\]

\[
\boxed{\frac14}
\]