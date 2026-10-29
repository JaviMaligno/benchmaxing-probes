La probabilidad de que el recíproco de un entero positivo impar menor que 2010 tenga decimal finito.

Un número $\frac{1}{n}$ tiene decimal finito si y solo si el denominador $n$ tiene solo factores primos 2 y 5. Como $n$ es impar, no tiene factor 2, así que debe ser una potencia de 5: $n = 5^k$.

Los enteros positivos impares menores que 2010 son $1, 3, 5, \ldots, 2009$, es decir, los impares desde 1 hasta 2009. Hay $\frac{2009+1}{2} = 1005$ números en total.

Ahora contamos potencias de 5 que son impares (todas lo son) y menores que 2010:

$5^1 = 5$
$5^2 = 25$
$5^3 = 125$
$5^4 = 625$
$5^5 = 3125 > 2010$

Además, $n=1$ también da decimal finito: $\frac{1}{1} = 1$.

Por tanto, hay $4 + 1 = 5$ valores favorables: $1, 5, 25, 125, 625$.

La probabilidad es:
\[
\frac{5}{1005} = \frac{1}{201}
\]

Aquí $a = 1$ y $b = 201$, que son primos relativos. Luego:
\[
a + b = 1 + 201 = 202
\]

\boxed{202}