

Sea \(f_i(j)=g(i,j)\). Entonces cada fila \(f_i\) es una tupla de 5 valores.

**Fila \(i=0\):**

\[
f_0(j)=\operatorname{rem}_5(j+1)
\]

\[
f_0=(1,2,3,4,0).
\]

**Fila \(i=1\):**

\[
f_1(0)=f_0(2)=3
\]

Luego aplicamos \(f_1(j)=f_0(f_1(j-1))\):

\[
f_1=(3,4,0,1,2).
\]

**Fila \(i=2\):**

\[
f_2(0)=f_1(2)=0
\]

\[
f_2=(0,3,1,4,2).
\]

**Fila \(i=3\):**

\[
f_3(0)=f_2(2)=1
\]

\[
f_3=(1,3,4,2,1).
\]

**Fila \(i=4\):**

\[
f_4(0)=f_3(2)=4
\]

\[
f_4=(4,1,3,2,4).
\]

**Fila \(i=5\):**

\[
f_5(0)=f_4(2)=3
\]

\[
f_5=(3,2,3,2,3).
\]

**Fila \(i=6\):**

\[
f_6(0)=f_5(2)=3
\]

\[
f_6=(3,2,3,2,3).
\]

Como \(f_6=f_5\), la recursión queda estable: para todo \(i\ge 5\),

\[
f_i=(3,2,3,2,3).
\]

En particular,

\[
g(2024,3)=f_{2024}(3)=2.
\]

\[
\boxed{2}
\]