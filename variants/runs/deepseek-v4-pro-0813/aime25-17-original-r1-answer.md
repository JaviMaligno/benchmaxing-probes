Vamos a razonar paso a paso.

Queremos hallar todos los enteros positivos $n$ tales que $n+2$ divide a

\[
3(n+3)(n^2+9).
\]

Como $n+2$ y $3$ son primos entre sí salvo que $n+2$ sea múltiplo de $3$, conviene trabajar con congruencias módulo $n+2$.

Observamos que si $n+2\mid 3(n+3)(n^2+9)$, entonces

\[
3(n+3)(n^2+9)\equiv 0 \pmod{n+2}.
\]

Notemos que módulo $n+2$:

\[
n+3 \equiv 1 \pmod{n+2}.
\]

Además,

\[
n \equiv -2 \pmod{n+2},
\]

por lo que

\[
n^2+9 \equiv (-2)^2+9 = 4+9 = 13 \pmod{n+2}.
\]

Por tanto,

\[
3(n+3)(n^2+9) \equiv 3\cdot 1 \cdot 13 = 39 \pmod{n+2}.
\]

Así, la condición de divisibilidad equivale a

\[
n+2 \mid 39.
\]

Los divisores positivos de $39$ son

\[
1,3,13,39.
\]

Como $n$ es un entero positivo, $n+2\ge 3$. Luego las posibilidades son:

\[
n+2 = 3,\ 13,\ 39.
\]

Es decir,

\[
n = 1,\ 11,\ 37.
\]

Verifiquemos rápidamente:

- Para $n=1$: $n+2=3$ divide a $3(4)(10)=120$. Sí.
- Para $n=11$: $n+2=13$ divide a $3(14)(130)=5460$. Sí.
- Para $n=37$: $n+2=39$ divide a $3(40)(1378)$. Sí.

La suma de estos valores es

\[
1+11+37 = 49.
\]

Por lo tanto, la suma pedida es

\[
\boxed{49}
\]