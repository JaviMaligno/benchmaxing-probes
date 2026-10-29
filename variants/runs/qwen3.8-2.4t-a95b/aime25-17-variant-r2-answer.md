

Sea \(d=n+3\). Entonces \(n=d-3\), con \(d\ge 4\).

Queremos que
\[
n+3 \mid 2(n+5)(n^2+7),
\]
es decir,
\[
d \mid 2(d+2)\bigl((d-3)^2+7\bigr).
\]

Reducimos módulo \(d\):

\[
d+2 \equiv 2 \pmod d,
\]
y
\[
(d-3)^2+7=d^2-6d+16 \equiv 16 \pmod d.
\]

Por lo tanto,
\[
2(n+5)(n^2+7) \equiv 2\cdot 2\cdot 16=64 \pmod d.
\]

Así que la condición equivale a
\[
d \mid 64.
\]

Como \(d=n+3\ge 4\), los divisores positivos posibles de \(64\) son
\[
d\in\{4,8,16,32,64\}.
\]

Entonces
\[
n=d-3\in\{1,5,13,29,61\}.
\]

La suma es
\[
1+5+13+29+61=109.
\]

\[
\boxed{109}
\]