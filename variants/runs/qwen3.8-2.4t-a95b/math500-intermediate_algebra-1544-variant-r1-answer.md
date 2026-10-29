

Sea \(\phi(t)=t^2-4t+6\). La condición dice que \(\phi\) envía cada raíz de la ecuación cuadrática a otra raíz de la misma ecuación. Consideramos las raíces en \(\mathbb C\), como es usual para polinomios.

Primero hallamos los puntos fijos de \(\phi\):

\[
\phi(t)=t \iff t^2-4t+6=t \iff t^2-5t+6=0 \iff t=2 \text{ o } t=3.
\]

### Caso 1: raíz doble
Si la ecuación tiene una única raíz \(t\) con multiplicidad 2, entonces debe cumplirse \(\phi(t)=t\). Así, \(t=2\) o \(t=3\). Esto da dos ecuaciones:

\[
(x-2)^2=x^2-4x+4,
\qquad
(x-3)^2=x^2-6x+9.
\]

### Caso 2: dos raíces distintas \(a,b\)
Cada raíz debe ser enviada a \(a\) o \(b\). Hay tres posibilidades.

#### a) Ambas raíces son puntos fijos
Entonces las raíces son \(2\) y \(3\), dando

\[
(x-2)(x-3)=x^2-5x+6.
\]

#### b) Ambas raíces se envían a la misma raíz
Supongamos \(\phi(a)=\phi(b)=a\). Entonces \(a\) es punto fijo.

- Si \(a=2\), \(\phi(b)=2\) implica \((b-2)^2=0\), así que \(b=2\), contradicción.
- Si \(a=3\), \(\phi(b)=3\) implica \(b^2-4b+3=0\), así que \(b=1\) o \(b=3\). Con \(b=1\) obtenemos las raíces \(\{1,3\}\).

Esto da

\[
(x-1)(x-3)=x^2-4x+3.
\]

#### c) Las raíces se intercambian
Si \(\phi(a)=b\) y \(\phi(b)=a\), entonces

\[
b-a=\phi(a)-\phi(b)=(a-b)(a+b-4).
\]

Como \(a\neq b\), obtenemos \(a+b=3\). Luego \(b=3-a\), y usando \(\phi(a)=b\):

\[
a^2-4a+6=3-a
\iff a^2-3a+3=0.
\]

Así que las raíces son las de

\[
x^2-3x+3=0.
\]

En total, las ecuaciones son:

\[
x^2-4x+4,\quad x^2-6x+9,\quad x^2-5x+6,\quad x^2-4x+3,\quad x^2-3x+3.
\]

Por lo tanto, hay

\[
\boxed{5}
\]