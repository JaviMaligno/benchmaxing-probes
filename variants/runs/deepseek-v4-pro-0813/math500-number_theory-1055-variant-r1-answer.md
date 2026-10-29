Vamos a razonar paso a paso.

- Tienes **nueve bolsas** de monedas de plata.
- Cada bolsa tiene la **misma cantidad** de monedas. Llamémosla \(x\).
- Entonces, antes de encontrar la bolsa nueva, tienes \(9x\) monedas.
- Encuentras una bolsa de **47 monedas**.
- Ahora tienes \(9x + 47\) monedas en total.
- Redistribuyes **todas** las monedas entre **diez bolsas** de modo que las diez tengan la misma cantidad.
- Por lo tanto, el total \(9x + 47\) debe ser divisible entre 10.

Además, se dice que tienes **más de 300 monedas**, es decir:

\[
9x + 47 > 300
\]

Como \(x\) es entero:

\[
9x > 253
\]

\[
x > 28.111\ldots
\]

Por tanto, \(x \ge 29\).

Ahora buscamos la condición de divisibilidad:

\[
9x + 47 \equiv 0 \pmod{10}
\]

Reducimos módulo 10:

\[
9x + 47 \equiv -x + 7 \pmod{10}
\]

Porque \(9 \equiv -1\) y \(47 \equiv 7\).

Entonces:

\[
-x + 7 \equiv 0 \pmod{10}
\]

\[
x \equiv 7 \pmod{10}
\]

Es decir, \(x\) es de la forma:

\[
x = 10k + 7
\]

Pero también \(x \ge 29\).

El menor \(x\) que cumpla \(x \equiv 7 \pmod{10}\) y \(x \ge 29\) es:

- \(x = 27\) no sirve porque \(27 < 29\).
- \(x = 37\) sí sirve.

Entonces \(x = 37\).

El número de monedas **antes** de encontrar la bolsa de 47 era:

\[
9x = 9 \cdot 37 = 333
\]

Verificamos:

- Monedas totales: \(333 + 47 = 380\).
- Repartidas entre 10 bolsas: \(380 / 10 = 38\) por bolsa.
- \(380 > 300\).

Todo cumple.

El menor número de monedas que podías tener antes de encontrar la bolsa era:

\[
\boxed{333}
\]