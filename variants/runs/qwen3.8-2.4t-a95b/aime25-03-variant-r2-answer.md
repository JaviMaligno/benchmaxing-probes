

Los 10 miembros son distinguibles, así que contamos asignaciones según los números de cada sabor.

Sean \(m, b, k\) las cantidades de smoothies de mango, banana y kiwi. Necesitamos:

\[
m+b+k=10,\qquad m>b>k\ge 1
\]

Enumeramos las ternas posibles:

- Si \(k=1\):
  - \(b=2 \Rightarrow m=7\): \((7,2,1)\)
  - \(b=3 \Rightarrow m=6\): \((6,3,1)\)
  - \(b=4 \Rightarrow m=5\): \((5,4,1)\)

- Si \(k=2\):
  - \(b=3 \Rightarrow m=5\): \((5,3,2)\)

No hay más casos.

Para cada terna, el número de asignaciones es un coeficiente multinomial:

\[
\frac{10!}{m!\,b!\,k!}
\]

Calculamos:

\[
\frac{10!}{7!2!1!}=360
\]

\[
\frac{10!}{6!3!1!}=840
\]

\[
\frac{10!}{5!4!1!}=1260
\]

\[
\frac{10!}{5!3!2!}=2520
\]

Sumando:

\[
N=360+840+1260+2520=4980
\]

El residuo de \(4980\) dividido entre \(1000\) es:

\[
\boxed{980}
\]