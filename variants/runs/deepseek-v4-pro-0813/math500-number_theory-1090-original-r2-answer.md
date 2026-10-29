Primero, un número racional $\frac{1}{n}$ tiene un desarrollo decimal finito si y solo si la descomposición en factores primos de $n$ (reducida) solo contiene potencias de 2 y de 5.

Como aquí tomamos $n$ como un entero positivo impar menor que 2010, el factor 2 no puede aparecer en $n$. Por tanto, $\frac{1}{n}$ será decimal finito únicamente cuando $n$ tenga solo potencias de 5, es decir, cuando
\[
n = 5^k
\]
para algún entero $k \ge 0$, con $n < 2010$.

Calculemos las potencias de 5 menores que 2010:
\[
5^0 = 1,\quad 5^1 = 5,\quad 5^2 = 25,\quad 5^3 = 125,\quad 5^4 = 625.
\]
Como $5^5 = 3125 > 2010$, las potencias válidas son $1, 5, 25, 125, 625$, es decir, hay 5 enteros impares positivos menores que 2010 cuyo recíproco es decimal finito.

Ahora contamos cuántos enteros positivos impares hay menores que 2010. Los enteros positivos impares desde 1 hasta 2009 son:
\[
1, 3, 5, \dots, 2009.
\]
La cantidad es
\[
\frac{2009 - 1}{2} + 1 = \frac{2008}{2} + 1 = 1004 + 1 = 1005.
\]

Por lo tanto, la probabilidad pedida es
\[
\frac{5}{1005} = \frac{1}{201}.
\]
Así, $a = 1$ y $b = 201$, que son primos relativos.

Entonces,
\[
a + b = 1 + 201 = 202.
\]

\[
\boxed{202}
\]