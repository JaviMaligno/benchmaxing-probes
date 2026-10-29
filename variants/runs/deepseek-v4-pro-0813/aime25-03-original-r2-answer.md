Vamos a resolver el problema paso a paso.

Sean:

- \(c\): número de jugadores que eligieron chocolate.
- \(v\): número de jugadores que eligieron vainilla.
- \(f\): número de jugadores que eligieron fresa.

Condiciones:

1. \(c + v + f = 9\).
2. \(c > v > f \ge 1\).

Como \(f \ge 1\), veamos las posibles particiones de 9 con \(c>v>f\ge 1\).

---

**Hallamos las ternas posibles:**

Probemos \(f=1\):

\[
v \ge 2,\quad c > v,\quad c+v+1=9 \Rightarrow c+v=8.
\]

Con \(c>v\) y \(v>1\):

- \(v=2 \Rightarrow c=6\) → \((6,2,1)\)
- \(v=3 \Rightarrow c=5\) → \((5,3,1)\)

\(v=4 \Rightarrow c=4\), pero necesitamos \(c>v\), no sirve.

Probemos \(f=2\):

\[
c+v=7,\quad v>2,\quad c>v.
\]

- \(v=3 \Rightarrow c=4\) → \((4,3,2)\)

\(v=4 \Rightarrow c=3\), no sirve.

Probemos \(f=3\):

\[
c+v=6,\quad v>3 \Rightarrow v\ge 4,\quad c>v \Rightarrow c\ge 5.
\]

Pero \(c+v\ge 9>6\), no hay solución.

Por lo tanto, las ternas válidas son:

\[
(6,2,1),\quad (5,3,1),\quad (4,3,2).
\]

---

**Contamos las asignaciones para cada terna.**

Los jugadores son distinguibles. El número de formas de asignar \(c\) chocolates, \(v\) vainillas y \(f\) fresas a 9 jugadores es el coeficiente multinomial:

\[
\frac{9!}{c!\,v!\,f!}.
\]

---

1. Para \((6,2,1)\):

\[
\frac{9!}{6!\,2!\,1!} = \frac{362880}{1440\cdot 2\cdot 1} = 252.
\]

2. Para \((5,3,1)\):

\[
\frac{9!}{5!\,3!\,1!} = \frac{362880}{120\cdot 6\cdot 1} = 504.
\]

3. Para \((4,3,2)\):

\[
\frac{9!}{4!\,3!\,2!} = \frac{362880}{24\cdot 6\cdot 2} = 1260.
\]

---

**Sumamos:**

\[
N = 252 + 504 + 1260 = 2016.
\]

---

**Hallamos el residuo módulo 1000:**

\[
2016 \bmod 1000 = 16.
\]

\[
\boxed{16}
\]