Sea \(m=n+2\). Como \(n\) es un entero positivo, \(m\ge 3\).

La condición es que \(m\mid 3(n+3)(n^2+9)\). Expresamos todo en términos de \(m\):
\[
n=m-2,\qquad n+3=m+1,\qquad n^2+9=(m-2)^2+9=m^2-4m+13.
\]
Entonces
\[
3(n+3)(n^2+9)=3(m+1)(m^2-4m+13).
\]

Reduciendo módulo \(m\):
\[
m+1\equiv 1,\qquad m^2-4m+13\equiv 13 \pmod m.
\]
Por lo tanto,
\[
3(m+1)(m^2-4m+13)\equiv 3\cdot 1\cdot 13=39 \pmod m.
\]

Así, \(m\mid 3(n+3)(n^2+9)\) si y solo si \(m\mid 39\).

Los divisores positivos de \(39\) son
\[
1,\ 3,\ 13,\ 39.
\]
Como \(m\ge 3\), se tiene
\[
m\in\{3,13,39\}.
\]

Luego
\[
n=m-2\in\{1,11,37\}.
\]

La suma es
\[
1+11+37=49.
\]

\[
\boxed{49}
\]