

Sea \(d=n+3\). Como \(n\) es entero positivo, \(d\ge 4\). Entonces \(n=d-3\), y queremos que

\[
d \mid 2(n+5)(n^2+7).
\]

Reescribimos cada factor módulo \(d\):

\[
n+5=(d-3)+5=d+2\equiv 2 \pmod d,
\]

y

\[
n^2+7=(d-3)^2+7=d^2-6d+9+7=d^2-6d+16\equiv 16 \pmod d.
\]

Por tanto,

\[
2(n+5)(n^2+7)\equiv 2\cdot 2\cdot 16=64 \pmod d.
\]

Así, la condición de divisibilidad equivale a

\[
d \mid 64.
\]

Los divisores positivos de \(64\) son

\[
1,2,4,8,16,32,64.
\]

Como \(d=n+3\ge 4\), los valores posibles son

\[
d=4,8,16,32,64.
\]

Esto da

\[
n=d-3=1,5,13,29,61.
\]

La suma es

\[
1+5+13+29+61=109.
\]

\[
\boxed{109}
\]