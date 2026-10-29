

Sean \(m\), \(b\) y \(k\) las cantidades de miembros que pidieron mango, banana y kiwi, respectivamente. Tenemos

\[
m+b+k=10,\qquad m>b>k\ge 1.
\]

Buscamos las ternas posibles:

- Si \(k=1\): \(b=2,3,4\), dando \((m,b,k)=(7,2,1),(6,3,1),(5,4,1)\).
- Si \(k=2\): solo \(b=3\), dando \((m,b,k)=(5,3,2)\).
- Si \(k\ge 3\), no hay soluciones.

Como los 10 miembros son distinguibles, para cada terna contamos las asignaciones con un coeficiente multinomial:

\[
\frac{10!}{m!\,b!\,k!}.
\]

Así,

\[
\frac{10!}{7!2!1!}=360,
\]

\[
\frac{10!}{6!3!1!}=840,
\]

\[
\frac{10!}{5!4!1!}=1260,
\]

\[
\frac{10!}{5!3!2!}=2520.
\]

Sumando:

\[
N=360+840+1260+2520=4980.
\]

Finalmente,

\[
4980 \equiv 980 \pmod{1000}.
\]

\[
\boxed{980}
\]