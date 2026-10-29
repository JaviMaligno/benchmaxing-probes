Vamos a resolverlo paso a paso.

Buscamos el mayor entero $n < 2010$ que cumpla:

\[
\begin{aligned}
n &\equiv 5 \pmod 7,\\
n &\equiv 10 \pmod {11},\\
n &\equiv 10 \pmod {13}.
\end{aligned}
\]

**Paso 1: Combinar las congruencias con módulos 11 y 13.**

Como $10 \equiv -1 \pmod {11}$ y $10 \equiv -3 \pmod {13}$, trabajamos con:

\[
n \equiv 10 \pmod {11},\qquad n \equiv 10 \pmod {13}.
\]

Aunque los restos son iguales, los módulos son distintos, así que usamos el teorema chino del resto.

Escribimos:

\[
n = 11a + 10.
\]

Sustituyendo en la segunda:

\[
11a + 10 \equiv 10 \pmod {13}
\]

\[
11a \equiv 0 \pmod {13}.
\]

Como $\gcd(11, 13) = 1$:

\[
a \equiv 0 \pmod {13}.
\]

Entonces $a = 13k$, y por tanto:

\[
n = 11(13k) + 10 = 143k + 10.
\]

Así:

\[
n \equiv 10 \pmod {143}.
\]

**Paso 2: Combinar con la congruencia módulo 7.**

Ahora:

\[
n \equiv 10 \pmod {143},
\]

\[
n \equiv 5 \pmod 7.
\]

Escribimos:

\[
n = 143k + 10.
\]

Sustituimos en la congruencia módulo 7. Como $143 = 7 \cdot 20 + 3$, tenemos $143 \equiv 3 \pmod 7$ y $10 \equiv 3 \pmod 7$:

\[
3k + 3 \equiv 5 \pmod 7.
\]

\[
3k \equiv 2 \pmod 7.
\]

El inverso de $3$ módulo $7$ es $5$, porque $3 \cdot 5 = 15 \equiv 1 \pmod 7$.

\[
k \equiv 2 \cdot 5 = 10 \equiv 3 \pmod 7.
\]

Por tanto $k = 7t + 3$.

**Paso 3: Solución general.**

\[
n = 143(7t + 3) + 10 = 1001t + 429 + 10 = 1001t + 439.
\]

Es decir:

\[
n \equiv 439 \pmod {1001}.
\]

Las soluciones positivas menores que $2010$ son:

\[
439,\ 439 + 1001 = 1440,\ 1440 + 1001 = 2441.
\]

La última supera $2010$, así que las válidas son $439$ y $1440$.

La mayor menor que $2010$ es:

\[
\boxed{1440}
\]